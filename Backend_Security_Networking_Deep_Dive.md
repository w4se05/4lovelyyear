# 🔐 Backend, Security & Networking — Deep Dive Notes

> **Format:** Obsidian-compatible Markdown  
> **Tags:** #security #networking #database #backend #infrastructure

---

## Table of Contents

1. [[#Row Level Security (RLS)]]
2. [[#Presigned URLs]]
3. [[#Node.js Proxy vs Edge Model]]
4. [[#URL to Page — Every Step]]
5. [[#TCP Three-Way Handshake]]
6. [[#HTTPS and Encryption in Transit]]
7. [[#The 7 OSI Layers]]
8. [[#Attack Layers — SQL Injection, SYN Flood, ARP Spoof]]
9. [[#Internet Exchange Points & DE-CIX]]
10. [[#DNS Resolution — Full Deep Dive]]

---

## Row Level Security (RLS)

### What Is It?

Row Level Security is a database-level access control mechanism — available natively in **PostgreSQL** (and Supabase, AWS RDS, etc.) — that restricts **which rows** a user can `SELECT`, `INSERT`, `UPDATE`, or `DELETE`, based on the identity of the executing role.

Unlike application-level filtering (e.g. `WHERE user_id = $1` in your query), RLS is enforced **inside the database engine itself**, before any data is returned to the caller.

You enable it per-table:

```sql
ALTER TABLE documents ENABLE ROW LEVEL SECURITY;
```

Then you attach **policies** — boolean expressions that the query planner evaluates for every row:

```sql
CREATE POLICY user_sees_own_documents
  ON documents
  FOR SELECT
  USING (auth.uid() = owner_id);
```

### Where Is a Policy Evaluated?

RLS policies are evaluated **inside the PostgreSQL executor**, at the row-scan phase of query execution. The planner injects the policy predicate as an additional `WHERE` clause to every qualifying query. This happens:

- **After** the query is parsed and planned
- **Before** rows are returned to the client
- **At the database process level**, not the application server

The policy runs in the **security context of the database role** that issued the query — typically `authenticated` in Supabase, or whatever role was `SET` before execution.

### Why Can't an Attacker Bypass RLS by Calling the API Directly?

This is the critical security guarantee. The attack scenario:

> An attacker reverse-engineers your frontend JavaScript, finds the Supabase URL and `anon` API key (both are public by design), and calls the REST API directly using `curl` or Postman.

Here's why this still doesn't work:

1. **The API key (`anon` key) does not grant elevated database privileges.** It maps to the `anon` PostgreSQL role, which has only the permissions you explicitly granted.
2. **The JWT in the `Authorization` header is verified by Supabase/PostgREST**, which then calls `SET LOCAL role = 'authenticated'` and `SET LOCAL request.jwt.claims = '...'` before executing any SQL.
3. **RLS policies read from those session variables** — e.g. `auth.uid()` resolves to the `sub` claim in the JWT. Without a valid, Supabase-signed JWT containing the victim's `user_id`, the attacker's `auth.uid()` returns their own UID (or null), and the policy filters them out.
4. **The database doesn't trust the application** — it trusts its own role system and the cryptographically signed JWT. There is no way to lie about your identity to the database without forging Supabase's JWT secret.

**In short:** the guarantee is cryptographic + architectural. The attacker cannot present a valid JWT for another user without knowing Supabase's JWT signing secret.

### SQL Policy — Hide Inactive Documents from Public Queries

```sql
-- Enable RLS on the table first
ALTER TABLE documents ENABLE ROW LEVEL SECURITY;

-- Force RLS even for the table owner (important!)
ALTER TABLE documents FORCE ROW LEVEL SECURITY;

-- Policy: only active documents are visible to public/anonymous roles
CREATE POLICY hide_inactive_documents
  ON documents
  FOR SELECT
  USING (is_active = true);

-- If you also want authenticated users to see their OWN inactive docs:
CREATE POLICY owner_sees_own_inactive
  ON documents
  FOR SELECT
  USING (
    is_active = true
    OR (is_active = false AND owner_id = auth.uid())
  );
```

> [!note] Policy Logic
> The `USING` clause is a predicate evaluated against every row. If it returns `false`, the row is silently excluded — the client never sees it, not even as a "permission denied" error. This prevents information leakage.

---

### Follow-Up Questions & Answers

#### ❓ What is the difference between `USING` and `WITH CHECK` in a policy?

- **`USING`** controls which rows are **visible** (applies to `SELECT` and the target-rows phase of `UPDATE`/`DELETE`).
- **`WITH CHECK`** controls which rows can be **written** (applies to `INSERT` and `UPDATE`). It validates the *new* row state after the write.

Example: prevent users from transferring ownership to someone else:

```sql
CREATE POLICY users_own_their_rows
  ON documents
  FOR ALL
  USING (owner_id = auth.uid())
  WITH CHECK (owner_id = auth.uid());
```

Without `WITH CHECK`, a user could `UPDATE documents SET owner_id = attacker_id WHERE id = $1` and the write would succeed (since the old row passed `USING`), but the new row would now be invisible to them and owned by the attacker — a silent data hijack.

#### ❓ What happens if NO policy is defined on a table with RLS enabled?

PostgreSQL defaults to **deny all**. With RLS enabled and no matching policy, no rows are returned (for `SELECT`) and no writes succeed. This is a safe-by-default posture — you must explicitly grant access, not restrict it.

#### ❓ Can a `SECURITY DEFINER` function bypass RLS?

Yes — this is a critical footgun. A function marked `SECURITY DEFINER` executes with the privileges of the **function owner** (typically a superuser or `postgres` role), not the calling user. If the owner bypasses RLS (e.g. they are a superuser), the function can see all rows regardless of policies.

**Mitigation:**

```sql
-- Explicitly set the search path and drop to a safe role
CREATE FUNCTION get_active_docs()
  RETURNS SETOF documents
  LANGUAGE sql
  SECURITY DEFINER
  SET search_path = public
AS $$
  SELECT * FROM documents WHERE is_active = true;
$$;
```

Alternatively, use `SECURITY INVOKER` (the default) whenever possible.

---

## Presigned URLs

### What Is a Presigned URL?

A presigned URL is a time-limited, cryptographically signed URL that grants **temporary, scoped access** to a private resource in object storage (S3, GCS, R2, Supabase Storage, etc.) **without requiring the requester to have credentials**.

A typical S3 presigned URL looks like:

```
https://my-bucket.s3.amazonaws.com/invoices/2024-01.pdf
  ?X-Amz-Algorithm=AWS4-HMAC-SHA256
  &X-Amz-Credential=AKIAIOSFODNN7EXAMPLE%2F20240101%2Fus-east-1%2Fs3%2Faws4_request
  &X-Amz-Date=20240101T120000Z
  &X-Amz-Expires=3600
  &X-Amz-SignedHeaders=host
  &X-Amz-Signature=<HMAC-SHA256 signature>
```

### What Cryptographic Guarantee Does It Provide?

The signature is computed using **HMAC-SHA256** over a canonical string that encodes:

- The HTTP method (GET, PUT, etc.)
- The bucket and object key
- The expiration time
- The signing date and credential scope
- The `host` header

The signing key is derived from the **AWS Secret Access Key** using a key-derivation chain: `HMAC(HMAC(HMAC(HMAC("AWS4" + secret, date), region), service), "aws4_request")`.

This means:

1. **Integrity** — any tampering with the URL (changing the object path, extending the expiry, changing the method) invalidates the signature. AWS rejects the request.
2. **Authenticity** — only someone with the AWS secret key could have produced the signature. A third party cannot generate a valid presigned URL for your bucket.
3. **Non-transferable scope** — the URL is only valid for the specific object, method, and time window encoded in it.

### Why Does TTL Matter from a Security Perspective?

The TTL (`X-Amz-Expires`) is the **only thing limiting the blast radius** if the URL is leaked. Once a presigned URL is generated, it cannot be revoked without either:

- Rotating the signing credentials (global disruption)
- Deleting/moving the object
- Using S3 Object Lock / bucket policies to reject old signatures

**Attack scenario:** A presigned URL for a sensitive PDF is embedded in an email. The email is forwarded. The recipient clicks the link 3 days later. If TTL was 7 days, the object is now exposed.

**Best practices:**

| Use Case | Recommended TTL |
|---|---|
| Direct browser download | 5–15 minutes |
| Background job processing | 1–2 hours |
| Email delivery link | Avoid — use short-lived redirect |
| PUT upload from client | 10–30 minutes |

---

### Follow-Up Questions & Answers

#### ❓ Can the same presigned URL be used multiple times?

By default, **yes** — a presigned URL can be used unlimited times within its TTL. AWS S3 does not natively support single-use presigned URLs. To enforce one-time use, you must implement it at the application layer: log each URL's `jti` (URL hash), check it on first use, and delete the object or update a "consumed" flag.

#### ❓ What is the difference between a presigned URL and a signed cookie?

A **presigned URL** authorizes a single object per URL. A **CloudFront signed cookie** (or AWS signed cookie) authorizes access to **multiple objects** matching a path pattern (e.g. `media/user-123/*`), across a browser session. Signed cookies are better for streaming media or protecting entire directory trees; presigned URLs are better for discrete file access or S3 direct uploads.

#### ❓ Does HTTPS add any security on top of the cryptographic signature?

Yes — HTTPS prevents the presigned URL from being **intercepted in transit** (man-in-the-middle). Without HTTPS, an attacker on the same network could capture the URL from a plaintext HTTP request and reuse it within the TTL window. HTTPS encrypts the URL string itself (including query parameters), so the signature is not visible to a network observer. The signature guarantees integrity; HTTPS guarantees confidentiality in transit — they are complementary, not redundant.

---

## Node.js Proxy vs Edge Model

### The Two Architectures

**Node.js Proxy Model:**
```
Client → Node.js Server (your code) → Supabase / S3 / DB
```
Every request routes through your application server, which acts as a proxy. The server holds credentials, validates the request, and forwards it.

**Edge Model (e.g. Supabase RLS + direct client access, Cloudflare Workers, Next.js Edge Runtime):**
```
Client → Edge Function (near user, stateless) → DB / Storage
         ↑ RLS enforced at DB layer
```
The client calls the data store (somewhat) directly, protected by cryptographic tokens and database-level policies evaluated at the edge or at the DB.

### Attack Surfaces the Node.js Proxy Model Has That the Edge Model Eliminates

| Attack Surface | Node.js Proxy | Edge Model |
|---|---|---|
| **Server-Side Request Forgery (SSRF)** | High risk — attacker tricks your Node server into making internal requests | Reduced — edge functions have restricted internal network access |
| **Dependency supply chain attacks** | All `npm` packages on the server are in-scope | Minimal dependency surface in edge runtimes |
| **Credential exposure on server** | DB password, AWS keys, JWT secrets all live on server | Credentials managed by platform (e.g. Supabase anon key is already public) |
| **Persistent process memory attacks** | Long-running Node process can be exploited for memory inspection | Edge functions are stateless, ephemeral, short-lived per request |
| **Horizontal movement** | Compromised server can pivot to other internal services | Edge functions have no persistent network identity or internal routes |
| **DoS via resource exhaustion** | Single Node process can be OOM-killed or CPU-starved | Edge auto-scales; no shared process to exhaust |
| **Path traversal via proxy logic** | Bugs in URL forwarding can expose unintended resources | No forwarding layer to exploit |

---

### Follow-Up Questions & Answers

#### ❓ Does the edge model completely eliminate the need for a backend?

No. The edge model reduces the *attack surface* for data access, but you still need a backend (or serverless functions) for: sending emails, processing payments, running scheduled jobs, calling third-party APIs with secret keys, performing complex business logic that shouldn't be exposed to clients, and enforcing non-data-layer rules. The edge model shifts *where* security is enforced, not whether backend logic exists.

#### ❓ What is the main operational downside of the Node.js proxy model?

**Latency and scalability cost.** Every database query must round-trip through your server. Under high load, the server becomes a bottleneck. The edge model allows the client to talk more directly to the data layer (via RLS), reducing round-trips. Also, the Node proxy model requires you to maintain, patch, and scale your own server infrastructure.

#### ❓ How does Cloudflare Workers' security model differ from a traditional Node.js server?

Cloudflare Workers run in **V8 isolates**, not Node.js processes. Each request gets its own isolate — there is no shared memory between requests, no file system access, no `require()` of arbitrary packages, and no persistent OS process. This eliminates entire categories of attacks: process memory inspection, persistent backdoors, and most SSRF vectors. The tradeoff is a more restricted runtime — no native modules, limited CPU time per request, and no direct TCP connections (only HTTP/WebSocket APIs).

---

## URL to Page — Every Step

When you type `https://www.example.com/path?q=1` and press Enter, here is every step:

### 1. Browser Input Parsing
The browser parses the URL into: scheme (`https`), host (`www.example.com`), path (`/path`), query (`q=1`). It checks for any browser-level redirects, HSTS preload lists, or cached responses.

### 2. DNS Resolution
- Browser checks its **DNS cache** (TTL-aware).
- If not cached → checks **OS resolver cache** (`/etc/hosts`, local resolver).
- If not cached → queries the **configured DNS resolver** (ISP, 8.8.8.8, 1.1.1.1).
- Resolver performs **recursive resolution** (see DNS section below).
- Returns an **IP address** (e.g. `93.184.216.34`).

### 3. TCP Connection (Three-Way Handshake)
The OS networking stack opens a TCP connection to port `443` on the resolved IP. SYN → SYN-ACK → ACK (see TCP section below).

### 4. TLS Handshake (HTTPS)
Layered on top of TCP:
1. **ClientHello** — browser sends supported TLS versions, cipher suites, `SNI` (Server Name Indication — the hostname).
2. **ServerHello** — server selects cipher suite, sends its **TLS certificate chain**.
3. **Certificate Verification** — browser validates certificate against trusted CAs (built into OS/browser), checks `CN`/`SAN` matches hostname, checks revocation (OCSP/CRL).
4. **Key Exchange** — using ECDHE (Elliptic Curve Diffie-Hellman Ephemeral), both sides derive a shared session key **without the key ever being transmitted**.
5. **Finished** — both sides confirm with a MAC; encrypted channel is established.

### 5. HTTP Request Sent
Over the encrypted TLS channel, the browser sends:

```http
GET /path?q=1 HTTP/2
Host: www.example.com
Accept: text/html,application/xhtml+xml
Accept-Language: en-US
Cookie: session=...
```

### 6. Server Processing
The request hits: load balancer → web server (nginx/Caddy) → application server → database (if needed). Response is assembled.

### 7. HTTP Response Received

```http
HTTP/2 200 OK
Content-Type: text/html; charset=UTF-8
Content-Encoding: gzip
Cache-Control: max-age=3600

<compressed HTML>
```

### 8. Browser Parsing & Rendering
- HTML is parsed into the **DOM tree**.
- CSS is parsed into the **CSSOM tree**.
- DOM + CSSOM → **Render Tree**.
- **Layout** (reflow) — calculate element positions and sizes.
- **Paint** — draw pixels.
- **Compositing** — GPU layers assembled and displayed.
- JavaScript is executed (may trigger further requests, DOM mutations, re-renders).

### 9. Sub-Resource Loading
For each `<script>`, `<link>`, `<img>`, `<iframe>` etc.:
- DNS lookup (often already cached)
- TCP + TLS (HTTP/2 multiplexes over existing connections where possible)
- Fetch and render

---

### Follow-Up Questions & Answers

#### ❓ What is HSTS and how does it affect the first step?

**HTTP Strict Transport Security** is a response header (`Strict-Transport-Security: max-age=31536000; includeSubDomains`) that tells the browser: "for this domain, always use HTTPS, never HTTP, for the next N seconds." The browser stores this in its HSTS cache. On subsequent visits, it **upgrades `http://` to `https://` before even sending a request**, eliminating the window where an attacker could intercept an initial HTTP redirect. The **HSTS preload list** goes further — browsers ship with a hardcoded list of domains that are always-HTTPS, meaning even the very first visit is protected.

#### ❓ What is the purpose of HTTP/2 multiplexing and how does it change the sub-resource loading step?

HTTP/1.1 requires one request per TCP connection (or one at a time per connection). Browsers work around this by opening 6 parallel connections per origin. HTTP/2 multiplexes **multiple streams over a single TCP connection** using binary framing. This eliminates head-of-line blocking at the HTTP layer, reduces connection overhead, and allows **server push** (server proactively sends sub-resources before the browser requests them). In practice, this means page load requires far fewer TCP handshakes.

#### ❓ What happens if the DNS response is poisoned?

In a **DNS cache poisoning attack**, a malicious resolver injects a forged DNS record pointing `www.example.com` to an attacker-controlled IP. The browser then opens a TCP+TLS connection to the attacker's server. However, **TLS certificate validation stops this attack** — the attacker's server cannot present a valid certificate for `www.example.com` (they don't control the CA-issued cert). The browser will show a certificate error and block the connection. This is why HTTPS + PKI is the critical defence against DNS poisoning. **DNSSEC** adds cryptographic signing to DNS records themselves, preventing injection at the DNS layer.

---

## TCP Three-Way Handshake

### The Three Steps

```
Client                          Server
  |                               |
  |------- SYN (seq=x) ---------->|    Step 1
  |                               |
  |<------ SYN-ACK (seq=y,       |    Step 2
  |         ack=x+1) -------------|
  |                               |
  |------- ACK (ack=y+1) -------->|    Step 3
  |                               |
  |  [Connection Established]     |
```

**Step 1 — SYN (Synchronize):**
The client picks a random **Initial Sequence Number** (ISN, e.g. `x = 1000`) and sends a TCP segment with the `SYN` flag set. This says: "I want to open a connection; my sequence numbers will start at 1000."

**Step 2 — SYN-ACK (Synchronize-Acknowledge):**
The server picks its own ISN (`y = 5000`) and responds with both `SYN` and `ACK` flags set. `ack = x+1 = 1001` acknowledges the client's SYN (consuming sequence number 1000). The server also sets `seq = y = 5000`, saying: "My sequence numbers start at 5000."

**Step 3 — ACK (Acknowledge):**
The client acknowledges the server's SYN: `ack = y+1 = 5001`. Now both sides have synchronized sequence numbers and the connection is fully established.

### Why Random ISNs?
If sequence numbers were predictable (e.g. always 0), an off-path attacker could inject forged TCP segments by guessing the sequence number. Randomized ISNs prevent **TCP sequence number prediction attacks**.

### What Happens After?
Both sides maintain sliding window buffers. Every segment is acknowledged. Lost segments are retransmitted. TCP is a **reliable, ordered, byte-stream** protocol — the application sees a contiguous stream regardless of packet reordering or loss.

---

### Follow-Up Questions & Answers

#### ❓ What is a TCP SYN flood attack and how does SYN cookies mitigate it?

In a **SYN flood**, an attacker sends millions of SYN packets with **spoofed source IPs**. The server allocates a half-open connection entry for each, exhausting its connection table (backlog queue). Legitimate connections are refused.

**SYN cookies** solve this by making the server **stateless** during the handshake: instead of allocating a table entry, the server encodes the connection state (timestamp, MSS, hash of source IP/port/ISN) into the ISN of the SYN-ACK. Only when the client's ACK arrives (with `ack = ISN+1`) does the server reconstruct the state and allocate resources. Spoofed IPs never complete the handshake (they never receive the SYN-ACK), so no state is wasted.

#### ❓ What is the difference between a TCP FIN and RST termination?

- **FIN (graceful close):** One side sends FIN, the other ACKs, then sends its own FIN, which is ACKed — a **four-way teardown**. Both sides have flushed their send buffers. Half-close is possible (one direction closes while the other stays open).
- **RST (reset):** An abrupt, immediate termination. No buffered data is flushed. Used when a connection is in an invalid state, a port is unreachable, or a firewall is killing connections. The receiving side immediately closes. No acknowledgment is sent.

#### ❓ Why does TCP have a TIME_WAIT state after connection close?

After the final ACK of the four-way teardown, the **active closer** enters `TIME_WAIT` for **2 × MSL** (Maximum Segment Lifetime, typically 60–120 seconds). This serves two purposes:
1. **Delayed duplicate suppression** — ensures any late-arriving segments from the old connection (carrying the same port tuple) are discarded before a new connection reuses those ports.
2. **Reliable last ACK** — if the last ACK is lost, the remote side will retransmit its FIN; `TIME_WAIT` allows the closer to re-send the ACK. Without it, a retransmitted FIN might arrive on a *new* connection sharing the same 4-tuple and corrupt it.

---

## HTTPS and Encryption in Transit

### Why HTTPS Prevents Reading HTTP Requests in Transit

**Unencrypted HTTP:** the HTTP request (headers, URL path, query string, cookies, request body) is transmitted as plaintext TCP bytes. Anyone on the network path — your ISP, a coffee shop router, a government tap, a compromised middlebox — can read every byte.

**HTTPS (HTTP over TLS):** the TLS layer establishes an **encrypted tunnel** before any HTTP data is sent. Here's what happens:

1. **Key Exchange (ECDHE):** Client and server each generate an ephemeral elliptic curve key pair. They exchange public keys. Using the Diffie-Hellman protocol, both independently compute the same **shared secret** without it ever being transmitted. An eavesdropper sees only the public keys — from these, deriving the shared secret requires solving the **Elliptic Curve Discrete Logarithm Problem**, computationally infeasible with current hardware.

2. **Session Keys Derived:** From the shared secret, both sides derive symmetric keys (AES-256-GCM or ChaCha20-Poly1305) for bulk encryption. Symmetric encryption is orders of magnitude faster than asymmetric.

3. **Everything Is Encrypted:** The HTTP request line, all headers, the body, and even the URL path (after the hostname) are encrypted. A network observer sees only:
   - The destination IP and port (from IP/TCP headers — these cannot be encrypted without a VPN)
   - The **SNI** (Server Name Indication) in the TLS ClientHello — reveals the hostname (e.g. `www.example.com`) but not the path
   - The approximate size and timing of traffic

4. **AEAD Provides Integrity:** AES-GCM and ChaCha20-Poly1305 are **Authenticated Encryption with Associated Data** algorithms. Any tampering with the ciphertext produces an authentication tag mismatch, and the decryption fails with an error. A MITM cannot silently modify your request.

5. **Forward Secrecy:** The `E` in ECDHE stands for Ephemeral. Each session uses a new key pair, so even if the server's **long-term private key** is later compromised, past sessions cannot be decrypted (the ephemeral keys were discarded). This is **Perfect Forward Secrecy (PFS)**.

---

### Follow-Up Questions & Answers

#### ❓ What does a TLS certificate actually prove?

A TLS certificate is a **digitally signed statement** by a Certificate Authority (CA) that says: "I, DigiCert/Let's Encrypt/etc., have verified that the entity controlling this private key also controls the domain `example.com`." The certificate contains the domain name(s), the server's public key, validity dates, and the CA's signature. Your browser ships with a **trust store** — a list of ~150 root CAs. The signature chain is validated up to a trusted root. This proves you are talking to the legitimate owner of the domain, not a MitM — **as long as the CA system is not compromised.**

#### ❓ What is certificate pinning and when is it appropriate?

**Certificate pinning** is a mechanism where a client (typically a mobile app) hardcodes the expected certificate (or public key hash) for a specific server, refusing connections if the presented certificate doesn't match — even if it was validly issued by a trusted CA. This protects against CA compromise or misissuance. It's appropriate for high-security mobile apps (banking, VPNs) but **inappropriate for websites** (because you can't update browser pin lists easily and legitimate certificate rotations would break the app). It's increasingly replaced by **Certificate Transparency** logs + CAA DNS records.

#### ❓ What is the difference between TLS 1.2 and TLS 1.3 from a security standpoint?

| Aspect | TLS 1.2 | TLS 1.3 |
|---|---|---|
| Handshake round trips | 2 RTT | 1 RTT (0-RTT available for resumption) |
| Key exchange | RSA or DH (static possible) | ECDHE only (forward secrecy mandatory) |
| Cipher suites | Many, including weak (RC4, 3DES, MD5) | Only strong AEAD ciphers |
| Forward secrecy | Optional | Mandatory |
| Downgrade attack resistance | Weak (POODLE, BEAST exploited this) | Strong — removed all legacy mechanisms |
| Encrypted handshake | Certificate sent in plaintext | Certificate encrypted after key exchange |

TLS 1.3 eliminates ~20 years of accumulated legacy and is strictly more secure.

---

## The 7 OSI Layers

### Overview

The OSI (Open Systems Interconnection) model is a conceptual framework that standardizes the functions of a networking system into seven abstraction layers.

| # | Layer | Protocol Examples | Real-World Example |
|---|---|---|---|
| 7 | **Application** | HTTP, HTTPS, DNS, SMTP, FTP, SSH | Your browser making a `GET /` request to a web server |
| 6 | **Presentation** | TLS/SSL, MIME, JPEG, gzip | TLS encrypting the HTTP payload; gzip compressing the response body |
| 5 | **Session** | NetBIOS, RPC, SIP | A VoIP call maintaining a session state between two phones |
| 4 | **Transport** | TCP, UDP, QUIC | TCP breaking a file download into numbered segments and reassembling them |
| 3 | **Network** | IP (IPv4/IPv6), ICMP, BGP, OSPF | A router forwarding an IP packet across the internet toward `8.8.8.8` |
| 2 | **Data Link** | Ethernet, Wi-Fi (802.11), ARP | A switch using a MAC address table to forward a frame to the correct port |
| 1 | **Physical** | Ethernet cable, fiber optic, radio waves | Fiber optic cable carrying light pulses between Frankfurt and New York |

> [!tip] Mnemonic
> **A**ll **P**eople **S**eem **T**o **N**eed **D**ata **P**rocessing
> (Application → Physical, top to bottom)

### In Practice: TCP/IP vs OSI

The real internet uses the **TCP/IP model** (4 layers), which roughly maps as:
- Application → OSI layers 5+6+7
- Transport → OSI layer 4
- Internet → OSI layer 3
- Link → OSI layers 1+2

The OSI model is still the gold standard for **diagnosing and discussing** where in a stack a problem or attack occurs.

---

### Follow-Up Questions & Answers

#### ❓ Why is TLS considered Layer 6 (Presentation) but often discussed at Layer 4/5?

Technically, TLS provides **presentation-layer services** (encryption, encoding). But it operates **between** TCP (Layer 4) and HTTP (Layer 7), and its session management spans Layer 5. In practice, engineers say "TLS operates between Layer 4 and Layer 7" or just call it "Layer 4.5." The OSI model's strict boundaries don't map cleanly to modern protocol stacks — QUIC (used by HTTP/3), for example, bundles transport, security, and multiplexing in a single protocol that spans layers 4–6.

#### ❓ At what layer does a firewall operate?

It depends on the type:
- **Packet filter firewall** — Layer 3/4 (IP addresses, TCP/UDP ports)
- **Stateful firewall** — Layer 4 (tracks TCP connection state, allows established sessions)
- **Application firewall / WAF** — Layer 7 (inspects HTTP payloads, SQL injection patterns, XSS, etc.)

A WAF stopping SQL injection operates at Layer 7; a firewall blocking SYN floods operates at Layer 4.

#### ❓ What is ARP and why does it bridge Layer 2 and Layer 3?

**ARP (Address Resolution Protocol)** maps a Layer 3 IP address to a Layer 2 MAC address within a local network segment. When your computer wants to send a packet to `192.168.1.1`, it broadcasts "Who has 192.168.1.1?" on the local Ethernet segment. The gateway responds with its MAC address. ARP lives at the boundary of Layer 2 and 3 — it's sometimes called a "Layer 2.5" protocol. Because ARP is stateless and unauthenticated, it's vulnerable to **ARP spoofing** (see below).

---

## Attack Layers — SQL Injection, SYN Flood, ARP Spoof

### At Which OSI Layer Does Each Attack Occur?

#### SQL Injection → **Layer 7 (Application)**

SQL injection is a purely application-layer attack. The attacker crafts a malicious payload inside an HTTP request body or query string:

```
GET /users?id=1 OR 1=1--
```

This input travels through all lower layers untouched (encrypted at Layer 6 by TLS, segmented at Layer 4 by TCP). The attack only manifests when the **application processes the input and concatenates it into a SQL query without parameterization**. No network-layer defence can stop it — you need input validation, parameterized queries, and ORMs at Layer 7.

#### TCP SYN Flood → **Layer 4 (Transport)**

A SYN flood exploits the TCP state machine at Layer 4. The attacker sends millions of SYN packets (valid TCP segments) with spoofed source IPs. The server's TCP stack allocates half-open connection state for each. This is a **resource exhaustion attack against the OS networking stack** — it has nothing to do with the application. Mitigations (SYN cookies, rate limiting, firewall rules) all operate at Layer 3/4.

#### ARP Spoofing → **Layer 2 (Data Link)**

ARP spoofing attacks the layer 2 address resolution table. The attacker broadcasts **gratuitous ARP replies** claiming "I am `192.168.1.1`, and my MAC address is `AA:BB:CC:DD:EE:FF`." Hosts on the local network update their ARP caches, redirecting traffic through the attacker's machine (**man-in-the-middle**). This attack works below IP and TCP — it's invisible to Layer 3+ defences. Mitigations include **Dynamic ARP Inspection (DAI)** on managed switches (Layer 2), and end-to-end encryption (HTTPS/TLS ensures MitM can't read traffic even if ARP is poisoned).

---

### Follow-Up Questions & Answers

#### ❓ What is a second-order SQL injection and why is it harder to detect?

In a standard SQL injection, the payload is injected and executed in the **same request**. In a **second-order (stored) SQL injection**, the malicious payload is safely stored in the database (because it's escaped on write), but later **retrieved and used unsafely** in a subsequent query — often in a completely different code path. Example: a username of `admin'--` is stored safely but later embedded unescaped into a password-reset query. WAFs and input validation at the entry point miss it because the payload looks harmless at insertion time.

#### ❓ What is the difference between a SYN flood and a UDP flood?

A **SYN flood** exploits TCP's stateful handshake — the server must allocate resources for half-open connections. A **UDP flood** is a volumetric attack — it overwhelms the target's **bandwidth** by sending massive amounts of UDP traffic (UDP is stateless, so no handshake needed; the attacker just saturates the pipe). UDP floods often target services like DNS (port 53) or NTP (port 123) via **amplification attacks**: a small UDP request elicits a large response, amplifying the attack volume (NTP `monlist` command returns 206× amplification).

#### ❓ How does 802.1X port authentication defend against ARP spoofing?

**802.1X** is an IEEE standard for port-based network access control. Devices must authenticate (via EAP — Extensible Authentication Protocol) to a RADIUS server before the switch enables their port. This prevents an attacker from **plugging a rogue device into a network port** and launching ARP spoofing. Combined with **Dynamic ARP Inspection (DAI)** — which validates ARP packets against a DHCP snooping binding table — it eliminates both the device-entry and the ARP-spoofing attack vectors at Layer 2.

---

## Internet Exchange Points & DE-CIX

### What Is an Internet Exchange Point?

An **Internet Exchange Point (IXP)** is a physical infrastructure where independent networks (**Autonomous Systems**, identified by ASNs) interconnect and exchange internet traffic directly — without routing through upstream transit providers.

Without IXPs, traffic between two German networks might route: Network A → German ISP → Frankfurt → Amsterdam → London → New York → back to Frankfurt → Network B. IXPs short-circuit this.

**Technically:** An IXP is a large Layer 2 **switched fabric** — typically hundreds of Ethernet switches in a data center, all interconnected. Member networks connect their routers to the IXP switch fabric and exchange routes via **BGP (Border Gateway Protocol)**. Traffic flows directly between members at Layer 2 (Ethernet) speed, with no third-party IP hop.

### What Does DE-CIX Actually Do?

**DE-CIX** (Deutscher Commercial Internet Exchange), headquartered in Frankfurt, is the **world's largest IXP by peak traffic** — regularly exceeding **14–17 Tbps** of throughput.

**Operationally, DE-CIX:**

1. **Operates a carrier-neutral Layer 2 switch fabric** across multiple data centers in the Frankfurt area (and globally — DE-CIX has 39+ locations worldwide: New York, Mumbai, Madrid, Dubai, etc.).

2. **Provides BGP route servers** — instead of each member needing to establish bilateral BGP sessions with every other member (O(n²) sessions for 1000+ members), members peer with DE-CIX's route servers, which redistribute routes. Members can selectively accept/reject routes via BGP communities.

3. **Hosts 1000+ member networks** — ISPs, CDNs (Cloudflare, Akamai, Fastly), cloud providers (AWS, Google, Microsoft), telecom carriers, enterprise networks.

4. **Why Frankfurt?** Frankfurt is geographically central in Europe, has exceptional data center density (Interxion/Digital Realty, Equinix FR campuses), sits at the intersection of major submarine cable landing points and terrestrial fiber routes, and benefits from Germany's legal framework. It is the **network gravity center of continental Europe** — traffic naturally pools here because latency is minimized.

5. **Economic function:** By enabling **settlement-free peering**, IXPs save networks enormous transit costs. Transit bandwidth (paying a Tier-1 carrier like Deutsche Telekom or NTT to carry your traffic) costs ~$0.50–2/Mbps/month. Peering at DE-CIX costs a flat port fee regardless of volume.

---

### Follow-Up Questions & Answers

#### ❓ What is the difference between peering and transit?

- **Transit:** You pay an upstream provider (a Tier-1 or Tier-2 ISP) to carry your traffic to any destination on the internet. They have full routing tables and will forward your packets anywhere. Cost: per-Mbps or per-GB.
- **Peering:** Two networks agree to exchange traffic **between their own customers** at no cost (settlement-free) or at reduced cost. You only reach the other network's customers, not the whole internet. IXPs make peering scalable by providing a shared fabric for many bilateral peers.
- **Tier-1 networks** (AT&T, NTT, Telia, Lumen) only peer (never buy transit) — they have agreements with every other Tier-1, giving them full global reach for free.

#### ❓ How does BGP work at a high level and why is it called the "protocol that runs the internet"?

**BGP (Border Gateway Protocol)** is the **path-vector routing protocol** used between Autonomous Systems. Each AS announces the IP prefixes it owns (e.g. "I own `93.184.216.0/24`") to its BGP peers. Peers propagate these announcements, prepending their ASN to the path. The result: every AS builds a **global routing table** of ~900,000+ IPv4 prefixes, each with a path of ASNs to reach it. BGP is called "the protocol that runs the internet" because **all inter-AS routing decisions** — including IXP peering — are made via BGP. It is also notoriously fragile: a misconfigured BGP announcement (prefix hijacking) can reroute or blackhole internet traffic globally, as seen in incidents involving Pakistan Telecom (2008) and Amazon Route 53 (2018).

#### ❓ What is a BGP prefix hijack and what happened in the Amazon Route 53 incident?

A **BGP prefix hijack** occurs when an AS announces a more-specific prefix (e.g. `/25` vs the legitimate `/24`) or the same prefix as another AS. Because BGP prefers more-specific routes, traffic destined for the legitimate AS gets rerouted to the hijacker. In April 2018, attackers hijacked **Amazon Route 53 DNS** by announcing `205.251.196.0/24` (an AWS prefix) from a small ISP. DNS queries for `myetherwallet.com` resolved to the attacker's server, which served a phishing site. Users who ignored TLS certificate warnings lost cryptocurrency. The attack lasted ~2 hours. **RPKI (Resource Public Key Infrastructure)** — which cryptographically signs route origin authorizations — is the standardized defence, but adoption remains incomplete.

---

## DNS Resolution — Full Deep Dive

### The Full Recursive Resolution Process

When your browser needs to resolve `www.example.com`:

```
Browser
  → OS Stub Resolver
    → Recursive Resolver (e.g. 8.8.8.8)
      → Root Nameserver (.)
        → TLD Nameserver (.com)
          → Authoritative Nameserver (example.com)
            ← A record: 93.184.216.34
          ←
        ←
      ←
    ←
  ← 93.184.216.34
```

**Step-by-step:**

1. **Browser cache** — checks if `www.example.com` was recently resolved (TTL not expired).
2. **OS cache** — checks `/etc/hosts` and the OS resolver cache.
3. **Stub resolver → Recursive resolver** — the OS sends a UDP (or TCP, or DNS-over-HTTPS) query to the configured resolver (e.g. `8.8.8.8`).
4. **Recursive resolver → Root nameservers** — there are **13 root nameserver clusters** (A through M root), operated by ICANN, VeriSign, NASA, etc. The resolver asks: "Who handles `.com`?" Root responds with **TLD nameserver addresses** for `.com` (operated by Verisign).
5. **Recursive resolver → TLD nameserver** — asks: "Who handles `example.com`?" TLD nameserver returns the **authoritative nameserver** for `example.com` (e.g. `ns1.example.com`).
6. **Recursive resolver → Authoritative nameserver** — asks: "What is the A record for `www.example.com`?" Authoritative nameserver returns the IP address.
7. **Response cached at TTL** — resolver caches the answer for the record's TTL (can be 300 seconds to 86400 seconds). Browser caches it too.
8. **Response returned to stub resolver → browser.**

### Key Record Types

| Record | Purpose | Example |
|---|---|---|
| `A` | IPv4 address | `www.example.com → 93.184.216.34` |
| `AAAA` | IPv6 address | `www.example.com → 2606:2800:220:1:248:1893:25c8:1946` |
| `CNAME` | Alias to another name | `blog.example.com → example.ghost.io` |
| `MX` | Mail exchanger | `example.com → mail.example.com (priority 10)` |
| `TXT` | Arbitrary text | SPF, DKIM, domain verification tokens |
| `NS` | Nameserver delegation | `example.com → ns1.example.com` |
| `SOA` | Start of Authority | Zone metadata, serial number, TTL |
| `PTR` | Reverse DNS | `34.216.184.93.in-addr.arpa → www.example.com` |
| `SRV` | Service location | `_sip._tcp.example.com → priority weight port target` |

---

### Follow-Up Questions & Answers

#### ❓ What is DNS-over-HTTPS (DoH) and why is it controversial?

**DNS-over-HTTPS** sends DNS queries as HTTPS requests (typically to `https://cloudflare-dns.com/dns-query` or `https://dns.google/dns-query`). This encrypts DNS traffic, preventing your ISP or network observer from seeing which domains you're resolving — a significant privacy improvement over plaintext UDP DNS. **Controversy:** DoH centralizes DNS queries to a small number of large resolvers (Cloudflare, Google), undermining the distributed nature of DNS. Enterprise network administrators lose visibility into employee DNS activity (used for security monitoring). Governments in some jurisdictions cannot enforce DNS-based content filtering. Firefox and Chrome enabling DoH by default bypasses corporate DNS policies, causing IT security concerns.

#### ❓ What is a negative cache and why does it matter?

A **negative cache** entry records that a DNS name **does not exist** (NXDOMAIN response) or has no records of a requested type. These are also cached for the **TTL specified in the SOA record's NXDOMAIN TTL field**. This matters operationally: if you delete a domain's DNS record and someone queries it immediately, their resolver caches the NXDOMAIN. Even after you re-add the record, resolvers that cached the NXDOMAIN continue returning "not found" until their negative TTL expires. This is why DNS propagation after deletions can be slow.

#### ❓ What is DNSSEC and what attack does it prevent?

**DNSSEC (DNS Security Extensions)** adds cryptographic signing to DNS records. Each zone has a public/private key pair. Records are signed with the private key; resolvers verify signatures using the public key, which is itself signed by the parent zone (`.com` signs `example.com`'s key, the root zone signs `.com`'s key) — creating a **chain of trust** from the root. DNSSEC prevents **DNS cache poisoning** (Kaminsky attack): an attacker cannot forge a DNS response because they cannot produce a valid signature without the zone's private key. However, DNSSEC does **not** encrypt DNS traffic (DoH/DoT do that) — it only ensures authenticity and integrity of responses.

---

*Generated: 2026 — covers PostgreSQL RLS, Supabase, AWS S3 presigned URLs, TLS 1.3, TCP/IP, OSI model, DE-CIX, DNS, BGP*
