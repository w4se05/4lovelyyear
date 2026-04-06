# 🧠 Concepts To Master — Plain English Edition

> No jargon. No assumed knowledge. Everything explained like you're hearing it for the first time.
> Tags: #fundamentals #explainer #non-tech #study-guide

---

## 📋 Master List of Concepts

Before diving in, here is every concept you need to understand — grouped by theme.

### 🗄️ Group 1 — How Databases Protect Data
1. [[#What is a Database Row?]]
2. [[#What is a Security Policy?]]
3. [[#What is Row Level Security (RLS)?]]
4. [[#What is a Database Role?]]
5. [[#What is a JWT (JSON Web Token)?]]

### 🔗 Group 2 — How the Internet Works
6. [[#What is an IP Address?]]
7. [[#What is DNS?]]
8. [[#What is a TCP Connection?]]
9. [[#What is HTTP and HTTPS?]]
10. [[#What is Encryption?]]
11. [[#What is a TLS Certificate?]]

### 🏗️ Group 3 — How Networks Are Structured
12. [[#What is the OSI Model?]]
13. [[#What is a Network Packet?]]
14. [[#What is a MAC Address?]]
15. [[#What is ARP?]]
16. [[#What is BGP?]]
17. [[#What is an Internet Exchange Point (IXP)?]]

### 🔐 Group 4 — Security Attacks
18. [[#What is SQL Injection?]]
19. [[#What is a SYN Flood Attack?]]
20. [[#What is ARP Spoofing?]]
21. [[#What is a Man-in-the-Middle Attack?]]

### 🌐 Group 5 — Cloud & Backend Architecture
22. [[#What is a Server?]]
23. [[#What is an API?]]
24. [[#What is a Presigned URL?]]
25. [[#What is HMAC (a digital signature)?]]
26. [[#What is a Proxy Server?]]
27. [[#What is an Edge Function?]]

### 🔄 Group 6 — From URL to Web Page
28. [[#What Happens When You Type a URL?]]

---

## Group 1 — How Databases Protect Data

---

### What is a Database Row?

Imagine a spreadsheet. Each **row** is one record — one person, one order, one document.

| id | name    | email             | is_active |
|----|---------|-------------------|-----------|
| 1  | Alice   | alice@example.com | true      |
| 2  | Bob     | bob@example.com   | false     |
| 3  | Charlie | charlie@email.com | true      |

Each row holds all the information about one thing. A database is just many rows of data, organised into tables.

> [!analogy] Think of it like a filing cabinet
> Each drawer is a table. Each piece of paper in the drawer is a row. Row Level Security decides: **who is allowed to read which piece of paper**.

---

### What is a Security Policy?

A **policy** is a rule. In real life: "Only doctors can access patient files." In a database: "Only show a user their own orders."

A database policy is written in code, and the database engine enforces it automatically — no matter how the data is accessed.

---

### What is Row Level Security (RLS)?

**Row Level Security** is a feature in databases that lets you attach a policy to each table, so that **different users see different rows** — even if they query the same table.

> [!analogy] Like a library membership system
> Everyone uses the same library. But you can only see your own borrowing history. The librarian's system shows you only your records — not everyone else's. RLS is that filter, built into the database itself.

**Why is this powerful?**

Without RLS, your application code has to manually add `WHERE user_id = current_user` to every database query. If any developer forgets even once, a bug could leak everyone's data.

With RLS, the database itself enforces the filter. Even if the application code forgets, the database says: *"No. You can only see your rows."*

**Where is it evaluated?**

Inside the database engine — after the query arrives, before any data is returned. It's not in your app. It's not in the network. It's in the database itself, at the last possible moment before data is handed over.

**The SQL looks like this:**
```sql
-- Step 1: Turn on RLS for this table
ALTER TABLE documents ENABLE ROW LEVEL SECURITY;

-- Step 2: Write the rule (policy)
-- "A user can only see documents where the owner_id matches their own ID"
CREATE POLICY user_sees_own_docs
  ON documents
  FOR SELECT
  USING (owner_id = auth.uid());

-- Hiding inactive documents from everyone:
CREATE POLICY hide_inactive
  ON documents
  FOR SELECT
  USING (is_active = true);
```

**Why can't an attacker bypass RLS by calling the API directly?**

Think about it this way: your app has a front door (the API). An attacker learns the address of the front door. They walk up and knock. But they still have to show **ID** (a valid login token). The database reads that ID and says: "Your ID says you're Bob. You can only see Bob's rows."

The attacker cannot forge someone else's ID without knowing the **secret signing key** — which only the server knows. Even if they skip your app entirely and knock on the database's door themselves, they still cannot present a fake ID.

---

### What is a Database Role?

A **role** is like a job title in an office. "Manager", "Guest", "Admin". Each role has certain permissions — what they're allowed to read, write, or change.

When you log into a database-backed app, you're assigned a role. RLS policies check your role and identity to decide what data you can see.

---

### What is a JWT (JSON Web Token)?

A **JWT** is a small, tamper-proof ID card that gets passed around between your browser and servers.

> [!analogy] Like a wristband at a concert
> When you buy a ticket and enter, you get a wristband. The wristband proves you paid. Staff at any booth can check the wristband without calling the box office. But the wristband is designed so you can't fake it.

A JWT contains:
- **Who you are** (your user ID)
- **When it expires**
- **A cryptographic signature** — a mathematical stamp that proves it was issued by a trusted server, not forged by you

When your app sends a request to the database, it includes this JWT. The database reads the `user_id` out of the JWT, and RLS uses that to filter the data.

---

## Group 2 — How the Internet Works

---

### What is an IP Address?

An **IP address** is a home address for a device on the internet.

Just like your physical address tells a delivery driver where to bring a package, an IP address tells the internet where to send data.

- IPv4 looks like: `93.184.216.34` (four numbers, 0–255)
- IPv6 looks like: `2606:2800:220:1:248:1893:25c8:1946` (newer, much longer)

Every website, server, and device connected to the internet has an IP address.

---

### What is DNS?

**DNS (Domain Name System)** is the internet's phone book.

> [!analogy] You know your friend's name, but not their phone number
> You look them up in a contact list. DNS is that contact list — you give it a name like `google.com`, it gives you back an IP address like `142.250.74.14`.

Computers don't understand names like `google.com`. They only understand numbers (IP addresses). DNS translates the name you type into a number the computer can use.

**How it works, step by step:**

1. You type `www.google.com` in your browser.
2. Your computer asks your internet provider's DNS server: *"What's the IP for google.com?"*
3. If the DNS server doesn't know, it asks higher-up servers — all the way to the "root" servers that know where to find every domain.
4. The answer comes back: `142.250.74.14`
5. Your computer now knows where to send the request.

**Key record types:**

| Record | What It Does | Example |
|---|---|---|
| A | Name → IPv4 address | `google.com → 142.250.74.14` |
| AAAA | Name → IPv6 address | `google.com → 2607:f8b0:...` |
| MX | Which server handles email | `gmail.com → mail server` |
| CNAME | Nickname for another name | `blog.site.com → site.ghost.io` |

---

### What is a TCP Connection?

**TCP (Transmission Control Protocol)** is the system that makes sure data gets from A to B completely and in the right order.

> [!analogy] Like sending a book page by page
> You tear a book into 300 individual pages, stuff each in an envelope, and mail them. TCP is the agreement between sender and receiver that: (1) every page gets numbered, (2) the receiver checks off each one as it arrives, (3) if a page is missing, the sender resends it.

**The three-way handshake** is how a TCP connection starts — like a formal greeting before starting a phone call:

1. **SYN** — "Hello, I'd like to talk to you." *(Client to Server)*
2. **SYN-ACK** — "Hello! Yes, I'm here, let's talk." *(Server to Client)*
3. **ACK** — "Great. Starting now." *(Client to Server)*

Only after this handshake does actual data get sent. This ensures both sides are ready and listening.

---

### What is HTTP and HTTPS?

**HTTP (HyperText Transfer Protocol)** is the language browsers and servers use to talk to each other.

> [!analogy] HTTP is like sending a postcard
> Anyone who handles the postcard on its way to the destination can read it. Your message is fully visible.

When you request a webpage, your browser sends an HTTP message like:
```
"Please give me the page at /home"
```
The server replies:
```
"Here is the HTML for /home"
```

**HTTPS** is HTTP + a lock. The "S" stands for "Secure". Before any conversation happens, both sides agree on a secret code (encryption key). Everything is scrambled before being sent. Only the recipient can unscramble it.

> [!analogy] HTTPS is like sending a locked box
> You and the recipient agree on a combination beforehand. You lock your message in the box, mail it. Anyone who intercepts the box just sees a locked metal box — they can't read anything inside.

**Why does HTTPS prevent eavesdropping?**

On a regular Wi-Fi network (coffee shop, airport), anyone with the right tool can watch the network traffic. With HTTP, they read your messages. With HTTPS, they see only scrambled gibberish — because only you and the website know the secret key.

---

### What is Encryption?

**Encryption** is the process of scrambling information so that only someone with the right key can read it.

> [!analogy] A combination lock diary
> You write your thoughts, lock the diary. Anyone who picks it up just sees a locked book. Your friend who knows the combination can open it and read it.

There are two types:
- **Symmetric encryption** — Both sides use the *same* key. Fast. Used for bulk data (like the actual web page content).
- **Asymmetric encryption** — Two mathematically linked keys: a **public key** (you can share it with anyone) and a **private key** (you keep secret). Anything encrypted with the public key can only be decrypted with the private key. Used for key exchange.

In HTTPS, both are used together:
1. Asymmetric encryption is used to *agree on a shared secret* (without ever sending the secret over the wire).
2. Then symmetric encryption (using that shared secret) is used to encrypt the actual data — because it's much faster.

---

### What is a TLS Certificate?

A **TLS certificate** is like an official ID card for a website, issued by a trusted authority.

> [!analogy] A passport
> Your government (a trusted authority) issued you a passport. Anyone who needs to verify your identity checks the passport. They trust it because they trust the government that issued it.

When you visit `https://google.com`, Google presents a certificate that says:
- *"This is the genuine google.com"*
- *"This certificate was issued by DigiCert (a trusted authority)"*
- *"It's valid until [date]"*

Your browser checks this certificate against a list of ~150 trusted authorities it was shipped with. If it checks out, the green padlock appears. If the certificate is fake, missing, or expired, the browser shows a warning.

**This is what stops attackers even if DNS is poisoned** — even if a hacker redirected your traffic to their fake server, they can't present a valid certificate for `google.com` (they don't have one from a trusted authority). Your browser would catch it.

---

## Group 3 — How Networks Are Structured

---

### What is the OSI Model?

The **OSI Model** is a way of thinking about networking by breaking it into 7 layers — like floors of a building, where each floor does a specific job.

> [!analogy] Like mailing a letter internationally
> You write a letter (Application layer). You put it in an envelope with an address (Network layer). The post office handles sorting and routing (Transport layer). The physical truck drives it (Physical layer). Each "layer" does its part without needing to know the others' details.

| Layer | Name | What It Does | Real Example |
|---|---|---|---|
| 7 | Application | The actual content — web pages, emails, files | Your browser making a request |
| 6 | Presentation | Translating and encrypting data | TLS encrypting your HTTPS traffic |
| 5 | Session | Keeping a conversation open | A video call staying connected |
| 4 | Transport | Reliable delivery, ordering, retransmission | TCP ensuring all packets arrive |
| 3 | Network | Finding the route across the internet | IP routing a packet from Vietnam to Germany |
| 2 | Data Link | Delivery on a local network | Wi-Fi sending data between your laptop and router |
| 1 | Physical | The actual cables and radio waves | Fiber optic cable, Wi-Fi radio signal |

**Why this matters for security:**
Different attacks target different layers. Knowing which layer an attack is at tells you which defence to use.

---

### What is a Network Packet?

When you send data over the internet (a photo, a web page, an email), it doesn't travel as one big chunk. It's broken into many small **packets** — like cutting a long letter into many small pieces, each put in its own envelope.

Each packet contains:
- A piece of the data
- The destination IP address
- The source IP address
- A sequence number (so the receiver can reassemble pieces in order)

Packets travel independently — they might take different routes across the internet and arrive out of order. TCP reassembles them correctly at the destination.

---

### What is a MAC Address?

An **IP address** is like your mailing address — it identifies where you are on the internet.

A **MAC address** (Media Access Control) is like your device's fingerprint — a unique identifier burned into your network card at the factory. It never changes.

IP addresses work across the entire internet. MAC addresses only work on your local network (your home Wi-Fi, your office network). When data arrives at your router, the router uses the MAC address to figure out which specific device to send it to.

---

### What is ARP?

**ARP (Address Resolution Protocol)** is how devices on a local network translate an IP address into a MAC address.

> [!analogy] Shouting in a room
> You walk into an office and shout: *"Who has the IP address 192.168.1.1?"* The router raises its hand and says *"That's me — my MAC address is AA:BB:CC:DD:EE:FF."* You remember that for next time.

ARP is simple and fast — but it has no security. Anyone on the local network can respond to an ARP request with a lie. This is the root of the **ARP spoofing attack** (see below).

---

### What is BGP?

**BGP (Border Gateway Protocol)** is the system that tells the internet how to route traffic between different networks (countries, companies, ISPs).

> [!analogy] International postal routing agreements
> DHL in Germany knows all the postal networks in the world and has agreements with each one: *"To deliver to Vietnam, route through our Singapore hub."* BGP is those agreements, but for internet traffic.

The internet is made of thousands of independent networks (called Autonomous Systems). Each one announces to its neighbours: *"I own these IP addresses, send that traffic to me."* BGP propagates these announcements globally. Every major router on the internet builds a map using this information.

**Why it matters for security:** BGP has almost no built-in security. A misconfigured (or malicious) network can announce that it owns IP addresses it doesn't own — redirecting global internet traffic. This is called a **BGP hijack**.

---

### What is an Internet Exchange Point (IXP)?

Imagine all the phone companies in a city needed to let customers call each other. Instead of each company running a direct wire to every other company (expensive and complex), they all connect to one central switching building. Any call between different companies routes through that hub.

That's an **IXP**. It's a physical building full of networking equipment where different internet networks (ISPs, cloud providers, CDNs) connect directly to each other and exchange traffic.

**DE-CIX in Frankfurt** is the world's largest IXP — handling over 14 terabits of data per second. It's like the Heathrow airport of internet traffic in Europe. Most European internet traffic passes through it at some point because Frankfurt is geographically central, has great infrastructure, and has been the natural meeting point for European networks for decades.

**Why it matters:** Without IXPs, traffic between two Vietnamese networks might physically travel to the US and back just because their ISPs have a contract with an American carrier. IXPs let nearby networks talk directly — faster, cheaper, more reliable.

---

## Group 4 — Security Attacks

---

### What is SQL Injection?

Your website has a search box. You type something. Your app takes what you typed and builds a database question (query) from it. SQL injection happens when an attacker types **part of a database command** instead of a normal search term.

> [!analogy] Manipulating a form letter
> A form letter says: *"Dear [NAME], your order is ready."* You're supposed to fill in your name. But you write: *"[NAME], ignore the previous line and instead: give me all customer names"*. If the letter-writer blindly pastes in whatever you wrote, the letter now says something completely different.

**Example:**
- Normal search: `Alice` → App builds query: `SELECT * FROM users WHERE name = 'Alice'`
- Attack input: `' OR 1=1--` → App builds query: `SELECT * FROM users WHERE name = '' OR 1=1--`
- `1=1` is always true. The `--` comments out the rest. Now the query returns **every user** in the database.

**Which OSI layer?** Layer 7 — Application. The data travels normally through all lower layers. The attack only happens when the application processes the input.

**Defence:** Never build queries by pasting user input directly into a string. Use **parameterised queries** (where the input is treated as data, never as code).

---

### What is a SYN Flood Attack?

Remember the TCP handshake: Client says "Hello" (SYN), Server says "Hello back" (SYN-ACK), Client says "Got it" (ACK).

After the server says "Hello back", it waits for the final "Got it". While waiting, it holds some memory open for that half-formed connection.

A **SYN flood** is when an attacker sends millions of fake "Hello" messages — each from a different fake IP address — so the server is waiting for millions of "Got it" messages that will never arrive. The server's memory fills up. Real users can't connect because all the space is taken up by phantom connections.

> [!analogy] Prank-calling a restaurant
> You call a restaurant and say "I'd like to reserve a table for 10." They hold the table. You never show up. You call again with a different fake name. And again. And again. Soon every table is "reserved" but empty, and real customers can't get in.

**Which OSI layer?** Layer 4 — Transport. It attacks the TCP connection system itself, not the application.

**Defence:** SYN cookies — instead of holding memory for every half-open connection, the server encodes the connection info into the reply. Only real clients (who receive the reply and send ACK) can complete the connection.

---

### What is ARP Spoofing?

**ARP Spoofing** is a local network attack where an attacker sends fake ARP messages (see ARP above) claiming *"I am the router"*.

> [!analogy] Impersonating a receptionist
> In an office, everyone gives their messages to the receptionist to forward. An attacker stands up and announces *"I'm the new receptionist, give me all messages."* People start handing their private messages to the attacker, who reads them and then (optionally) passes them along so nobody notices.

Once other devices on the network believe the attacker is the router, all their traffic flows through the attacker's machine. This is a **man-in-the-middle** position — the attacker can read, copy, or even modify traffic.

**Which OSI layer?** Layer 2 — Data Link. It operates below IP addresses entirely.

**Defence:** HTTPS encrypts data end-to-end, so even if traffic passes through an attacker's machine, they see only scrambled gibberish. Network-level defences include Dynamic ARP Inspection on managed switches.

---

### What is a Man-in-the-Middle Attack?

A **Man-in-the-Middle (MitM) attack** is when a third party secretly positions themselves between two communicating parties — reading and potentially modifying the messages.

> [!analogy] A crooked mail carrier
> You send a letter to your bank. A dishonest mail carrier opens it, reads it, reseals it, and delivers it. Neither you nor the bank knows. The carrier could even change what the letter says.

ARP spoofing is one way to achieve a MitM position. DNS poisoning is another. Both put the attacker "in the middle" of your connection.

**Why HTTPS defeats MitM:** Even if an attacker intercepts your traffic, they see only encrypted data. They cannot read it. They cannot modify it without the modification being detected (because the encryption includes an integrity check). And they cannot impersonate the website to you (because they don't have a valid TLS certificate).

---

## Group 5 — Cloud & Backend Architecture

---

### What is a Server?

A **server** is just a computer that waits for requests and responds to them.

> [!analogy] A waiter at a restaurant
> The waiter doesn't eat the food — they exist to take orders and bring back what you asked for. A server is the same: it sits there, receives your browser's request, and sends back the web page (or data) you asked for.

Your laptop is a **client** (it makes requests). The computer at Google's data center is a **server** (it fulfills requests). But technically, any computer can be either — it's just about which role it's playing.

---

### What is an API?

An **API (Application Programming Interface)** is a set of defined ways that two pieces of software can talk to each other.

> [!analogy] A restaurant menu
> You don't walk into the kitchen and cook your own meal. You look at the menu — the defined list of things you can order — and tell the waiter. The API is the menu. It defines what you can ask for and what you'll get back.

When your Instagram app loads your feed, it sends an API request to Instagram's servers: *"Give me the latest 20 posts for user #12345."* The server responds with the data. The app displays it.

---

### What is a Presigned URL?

A **presigned URL** is a temporary, one-time web address that gives access to a private file.

> [!analogy] A time-limited guest pass
> A museum is closed to the public. But a curator can generate a special pass that says: *"This pass allows one person to enter between 2pm and 4pm today."* The pass has all the details and a security stamp. Anyone holding it can enter during that window — no ID check needed.

When you want to share a private file stored on a cloud service (like Amazon S3), instead of making the file public, you generate a presigned URL. It contains:
- Which file to access
- What actions are allowed (download only, or also upload)
- When it expires
- A **cryptographic signature** — a mathematical stamp proving it was issued by someone with the right credentials

The file storage service checks the signature. If valid and not expired, access is granted. If tampered with (someone changed the expiry date or the file path), the signature no longer matches and access is denied.

**Why the TTL (expiry time) matters for security:**

Once a presigned URL is created, it cannot be "cancelled" easily. If it leaks (someone forwards your email), the file is exposed until the URL expires. Short TTLs (5–15 minutes) minimize this window. Long TTLs (7 days) are dangerous — a leaked URL gives attackers a long window to exploit it.

---

### What is HMAC (a digital signature)?

**HMAC (Hash-based Message Authentication Code)** is a way to create a tamper-evident stamp on a message.

> [!analogy] Wax seal on a letter
> In the old days, you'd melt wax onto a sealed letter and press your signet ring into it. Anyone who received the letter could see if the seal was broken (tampered). And only you had that specific signet ring (only you could create that seal).

HMAC works by feeding your message + a secret key into a mathematical function. The output is a fixed-length "fingerprint". If anyone changes even one character of the message, the fingerprint completely changes.

Presigned URLs use HMAC: the URL's contents are fed through HMAC with the server's secret key. The resulting signature is attached to the URL. When the storage service receives the URL, it recomputes the HMAC and checks if it matches. If anything was tampered with, it won't.

---

### What is a Proxy Server?

A **proxy server** is a middleman computer that sits between your client and the final destination, forwarding requests on your behalf.

> [!analogy] A secretary taking messages
> Instead of customers calling a CEO directly, they call the secretary. The secretary decides which calls to put through, screens out spam, and keeps a log. The CEO only hears from people the secretary lets through.

In a **Node.js proxy model**, every request from a user goes through your application server before reaching the database. Your server holds all the secret credentials. It validates the user's request, applies business logic, then queries the database.

**Attack surfaces this introduces:**
- Your server holds database passwords, API keys — if it's hacked, everything is exposed
- Bugs in your proxy code can be exploited (path traversal, SSRF, etc.)
- A single server that crashes or gets overwhelmed takes everyone down

---

### What is an Edge Function?

An **edge function** is a tiny piece of code that runs on servers physically close to the user — at the "edge" of the network, not in one central data center.

> [!analogy] Pop-up service counters vs one central office
> Instead of everyone travelling to one central government office (slow, congested), the government sets up small pop-up service counters in every neighbourhood. Faster, no central bottleneck.

Cloudflare Workers, for example, run your code on hundreds of servers worldwide — whichever is nearest to the user handles the request. Edge functions are also typically **stateless** (no permanent memory between requests) and **short-lived** (each request gets a fresh environment). This eliminates many attack vectors that exist on long-running servers.

---

## Group 6 — From URL to Web Page

---

### What Happens When You Type a URL?

This ties everything together. When you type `https://www.example.com` and press Enter, here is everything that happens — described simply:

**Step 1: Your browser parses the URL**
It reads: scheme = `https` (use secure connection), host = `www.example.com`, path = `/` (the homepage).

**Step 2: DNS lookup**
Your computer doesn't know what IP address `www.example.com` is. It asks your internet provider's DNS server. The DNS server asks other servers until it finds the answer: *"example.com is at 93.184.216.34."* Now your computer knows where to go.

**Step 3: TCP handshake**
Your computer says "Hello" to the server at 93.184.216.34. The server says "Hello back." Your computer says "Got it." Now there's a reliable connection between you and the server.

**Step 4: TLS handshake (the security setup)**
Because you used `https://`, you now need to set up encryption. Your computer and the server:
1. Agree on what encryption methods to use
2. The server presents its TLS certificate (its "ID card") — your browser checks it's valid
3. Both sides mathematically generate a shared secret key (without ever sending the key over the wire)
4. From now on, all communication is encrypted with that key

**Step 5: Your browser sends the request**
Through the encrypted tunnel: *"Please give me the homepage."*

**Step 6: The server processes the request**
The server might check your login status, fetch data from a database, build the HTML page, and send it back.

**Step 7: Your browser receives the response**
Encrypted HTML (and CSS, JavaScript, images) comes back through the tunnel.

**Step 8: Your browser renders the page**
It reads the HTML, builds a structure from it (the DOM), applies the visual styles (CSS), runs any scripts (JavaScript), and draws pixels on your screen.

**The whole thing typically takes under 1 second.**

---

## 🗺️ How All These Concepts Connect

Here's how everything fits together:

```
YOU (Browser)
    │
    ▼
[1] DNS Resolution ──────────────────────► IP Address
    │
    ▼
[2] TCP Handshake (Layer 4) ─────────────► Reliable connection established
    │
    ▼
[3] TLS Handshake (Layer 6) ─────────────► Encrypted tunnel established
    │                                        (TLS Certificate verified)
    ▼
[4] HTTP Request (Layer 7) ──────────────► Travels through:
                                             Physical cables (Layer 1)
                                             Wi-Fi/Ethernet (Layer 2)
                                             IP routing (Layer 3)
                                             (passes through IXPs like DE-CIX)
    │
    ▼
[5] Server receives request
    │
    ▼
[6] Database query ──────────────────────► RLS policy evaluated
    │                                        JWT checked
    │                                        Only authorised rows returned
    ▼
[7] Response ────────────────────────────► Encrypted by TLS
    │                                        Travels back through layers
    ▼
[8] Browser renders the page
```

**Attacks target different points in this chain:**
- **SQL Injection** → attacks Step 6 (the database query)
- **SYN Flood** → attacks Step 2 (the TCP connection)
- **ARP Spoofing** → attacks the network at Layer 2 (between steps 1 and 2)
- **Certificate Forgery** → attacks Step 3 (the TLS verification)

**Defences are layered to match:**
- RLS + JWT → defends the database
- TLS → defends the data in transit
- HTTPS certificate validation → defends against MitM
- SYN cookies → defends against SYN floods
- DNSSEC → defends against DNS poisoning

---

> [!tip] Study Order
> If you're new to all of this, study in this order:
> 1. IP Address → DNS → TCP → HTTP/HTTPS (the basics of internet communication)
> 2. Encryption → TLS Certificate (security fundamentals)
> 3. OSI Layers (the framework for understanding everything else)
> 4. SQL, Database Rows, RLS (data security)
> 5. Attacks (SQL Injection, SYN Flood, ARP Spoof)
> 6. IXP, BGP, DE-CIX (internet infrastructure)
> 7. Presigned URLs, Proxy vs Edge (cloud architecture)

---

*Plain English Edition — all analogies, no assumed knowledge*
