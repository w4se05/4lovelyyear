## 1. Conceptual Section (Teach Mode)

### A. The TCP 3-Way Handshake
To establish a reliable connection over Transmission Control Protocol (TCP), a specific sequence of flags is used to synchronize sequence numbers $S$ and acknowledgment numbers $A$ between a Client ($C$) and a Server ($S$).

> [!Definition] **TCP Flags**
> - **SYN (Synchronize):** Initiates a connection.
> - **ACK (Acknowledgment):** Confirms receipt of a packet.
> - **Sequence Number ($S$):** A 32-bit number used to keep track of how much data is sent.

**The Process:**
1. **$C \rightarrow S$**: Sends `SYN` with an initial sequence number $S_{c}$.
2. **$S \rightarrow C$**: Sends `SYN-ACK`. The server sets its own sequence $S_{s}$ and sets the acknowledgment $A = S_{c} + 1$.
3. **$C \rightarrow S$**: Sends `ACK`. The client sets $A = S_{s} + 1$.

> [!Property] **Connection State**
> After step 3, the socket transition state moves to `ESTABLISHED`. If a port is closed, the server returns an `RST` (Reset) flag instead of `SYN-ACK`.

### B. IPv4 Addressing & CIDR
An IPv4 address consists of 32 bits, divided into four 8-bit octets. **CIDR (Classless Inter-Domain Routing)** notation uses a suffix $/n$ to denote the network prefix length.

> [!Formula] **Subnet Calculations**
> For a prefix length $n$:
> 1. **Number of bits for hosts ($h$):** $h = 32 - n$
> 2. **Total addresses ($N$):** $N = 2^h$
> 3. **Usable hosts ($H_{u}$):** $H_{u} = 2^h - 2$ (Subtracting Network and Broadcast addresses).
> 4. **Subnet Mask ($M$):** A bitmask where the first $n$ bits are 1 and the rest are 0.

---

## 2. Application Section (Exam Mode)

### 📘 Examples & Applications

#### Example 1: Handshake Analysis
*(Using: TCP State Logic)*
**Question:** A packet capture shows a server sending an acknowledgment number $A = 1001$. What was the original Initial Sequence Number (ISN) sent by the client?
**Solution:**
1. Recall the property: $A = S_{c} + 1$.
2. Set up the equation: $1001 = S_{c} + 1$.
3. Solve: $S_{c} = 1000$.

#### Example 2: Subnet Geometry
*(Using: CIDR Formula)*
**Question:** Calculate the usable host range and subnet mask for the network `192.168.10.0/27`.
**Solution:**
1. Find host bits: $h = 32 - 27 = 5$.
2. Total addresses: $2^5 = 32$.
3. Mask calculation: The last octet has $27 - 24 = 3$ bits set.
   $$M_{octet} = 2^7 + 2^6 + 2^5 = 128 + 64 + 32 = 224$$
   Mask: `255.255.255.224`.
4. Usable range: 
   - Network: `.0`
   - First Host: `.1`
   - Last Host: $32 - 2 = 30$, so `.30`
   - Broadcast: `.31`

---

## 3. Summary Section
- **Handshake:** SYN $\rightarrow$ SYN-ACK $\rightarrow$ ACK.
- **CIDR:** $/24 = 256$ IPs; $/30 = 4$ IPs (used for point-to-point links).
- **Wireshark Filter:** `tcp.flags.syn == 1 && tcp.flags.ack == 0` finds only the initial connection requests.