---
course: Computer Networks
source: "[[03-Data-Link-Framing-Switching]]"
---
#flashcards/cn/03-framing-switching

# CN-03 Data Link Layer: Framing and Switching — Cards (script 04)

> [!info] How to use
> Fill every ✍️ answer from memory first, then check in [[03-Data-Link-Framing-Switching|CN-03]] or [script 04](file:///C:/Users/hongp/OneDrive/Desktop/WS2627/CompNet/Lect/compnet-ws26-04.pdf). Plan: [[00 CompNet Plan]]

## Tasks and framing

Tasks of the data link layer?::Framing, addressing (MAC addresses), media access, error control, flow control.

Two sublayers of the data link layer?::Media Access Control (MAC) and Logical Link Control (LLC).

Four ways to mark frame borders?::Character count in the header, byte/character stuffing, bit stuffing, line code violations.

Character count in the header: example protocol and drawback?::DDCMP (DEC, 1974) has a Count field with the payload length. Drawback: if the count is corrupted in transit, the receiver can no longer find the end of the frame.

BISYNC (IBM, 1960s, byte-oriented): control characters and their meaning?::SYN (synchronization/frame start), SOH (start of header), STX (start of payload), ETX (end of payload), DLE (escape).

Byte stuffing rule of BISYNC?::An ETX in the payload is sent as DLE ETX; a DLE in the payload is sent as DLE DLE.

Drawback of byte stuffing?::It is tied to a character encoding (e.g. ASCII); newer protocols are bit-oriented.

HDLC flag and bit stuffing rule?::Frames start and end with 01111110. The sender inserts a 0 after five consecutive 1s; the receiver removes a 0 that follows five consecutive 1s.

Which common protocol implements HDLC framing?::PPP.

Line code violations — example?::Token Ring uses Differential Manchester (a level change inside every bit cell); its starting delimiter (first byte) and ending delimiter (second-to-last byte) each contain 4 line code violations — bit cells without that change.

## Ethernet frames

Ethernet preamble and SFD?::Preamble: 7 bytes 10101010 (0x55, sent LSb first) to synchronize the receiver clock and mark the frame start. SFD (start frame delimiter): 1 byte 10101011 (0xD5).

Ethernet type field values for IPv4, IPv6, ARP?::0x0800 IPv4, 0x86DD IPv6, 0x0806 ARP.

Ethernet MTU and why a minimum frame size exists?::Payload at most 1500 bytes (MTU). The minimum frame size is needed for collision detection; short frames are filled with a pad field.

Ethernet frame size limits (incl. preamble and SFD)?::Minimum 72 bytes, maximum 1526 bytes (1530 with VLAN tag).

Ethernet checksum?::32 bits over all fields except preamble and SFD.

Interframe gap?::At least 96 bit times (12 bytes): 9.6 µs at 10 Mbit/s, 0.96 µs at 100 Mbit/s, 96 ns at 1 Gbit/s.

Reduced interframe spacing: benefit and drawback?::Benefit: higher data rate. Drawback: the receiver may no longer detect the frame borders → more errors.

VLAN tag?::Optional 4 bytes (IEEE 802.1Q) with a 12-bit VLAN ID and a 3-bit priority.

## MAC addresses

Format of a MAC address?::48 bits (6 bytes), written in hex with dashes or colons, e.g. 00-16-41-52-DF-D7.

What is the OUI?::The first 24 bits of a MAC address, identifying the manufacturer; the other 24 bits give 2^24 device addresses per OUI.

What does the I/G bit mean?::Least significant bit of the first byte: 1 = group address (multicast/broadcast), 0 = unicast. A switch forwards such frames to several (possibly all) ports.

Broadcast MAC address?::FF-FF-FF-FF-FF-FF (all 48 bits set).

Why are MAC filters weak protection?::MAC addresses can be changed in software (MAC spoofing).

EUI-48 vs. EUI-64 — where used?::EUI-48: Ethernet, WLAN, Bluetooth. EUI-64: FireWire, 6LoWPAN, Zigbee.

Linux: show your MAC, show your neighbours' MACs, set a MAC?::`ip link` (or ifconfig) · `ip neigh` · `ip link set dev <interface> address <MAC>`.

## Switching

Repeater vs. bridge vs. switch?::Repeater (L1): extends a physical network. Bridge (L2): connects physical networks, at least 2 ports. Switch: a bridge with more than 2 ports.

Two properties of every bridge/switch besides forwarding?::They check each frame via its checksum, and they operate transparently (the hosts don't notice them).

How does a learning bridge fill its forwarding table?::It records the source address of every received frame with the port it arrived on; entries expire (TTL); unknown destination → frame is sent on all other ports.

Store-and-forward vs. cut-through vs. fragment-free?::Store-and-forward: receive the whole frame, check it, forward. Cut-through: forward as soon as the destination address is read. Fragment-free: forward after the first 64 bytes arrived without error. Adaptive cut-through: switches to store-and-forward above an error threshold.

Why are loops at the data link layer dangerous?::Frames get duplicated and keep circulating (Ethernet has no TTL/hop limit) until the switches learn the destination; tables flip, and every new frame adds copies → the network floods and collapses.

Spanning Tree Protocol: inventor and standard?::Radia Perlman at DEC (1980s), IEEE 802.1D.

What is a spanning tree?::A cycle-free subgraph that covers all nodes, created by removing (blocking) edges.

Bridge ID (IEEE)?::8 bytes: bridge priority (2 bytes, 0–65,535, default 32,768) + MAC address (6 bytes) of the bridge port with the lowest port ID.

Cisco's extended system ID?::The 2-byte priority field is split: 4 bits priority (0 or a multiple of 4,096, up to 61,440) + 12 bits VLAN ID → one spanning tree per VLAN (4,096 VLANs).

How is the root bridge chosen?::The bridge with the lowest priority value; on a tie the lowest MAC address.

What is the designated bridge of a physical network?::The directly connected bridge with the lowest path cost to the root bridge. Path cost = sum of the costs of the physical networks on the path to the root.

What are BPDUs?::Bridge Protocol Data Units — STP messages with bridge IDs and path costs, sent as Ethernet payload by broadcast to the neighbouring bridges.

## Understanding — write your own answers ✍️

✍️ Mark the payload (and unstuff it): 16 16 01 99 98 97 96 95 02 10 03 10 10 10 03 03 92 55 (sheet 3)
?
✍️ your answer — then check [[03-Data-Link-Framing-Switching|CN-03]] gold example 1

✍️ Bit-stuff 01111110 10100111 11111000 11110010 10011111 10111111 11100101 (sheet 3)
?
✍️ your answer — then check with the rule: 0 after every five 1s

✍️ Three switches in a loop, empty tables, A sends to B: explain step by step how the copies multiply and why it never stops.
?
✍️ your answer — then check [[03-Data-Link-Framing-Switching|CN-03]] gold example 3

✍️ How do switching and forwarding work, and what causes loops at the data link layer? (self-check questions)
?
✍️ your answer — then check the summary on the last page of [script 04](file:///C:/Users/hongp/OneDrive/Desktop/WS2627/CompNet/Lect/compnet-ws26-04.pdf)
