---
course: Computer Networks
source: "[[04-Data-Link-MAC-Error-Control]]"
---
#flashcards/cn/04-mac-error

# CN-04 Data Link Layer: Medium Access and Error Control — Cards (script 05)

> [!info] How to use
> Fill every ✍️ answer from memory first (CRC on paper!), then check in [[04-Data-Link-MAC-Error-Control|CN-04]] or script 05. Plan: [[00 CompNet Plan]]

## Medium access

Why is medium access control needed?::When several NICs share one medium, access must be coordinated, otherwise simultaneous transmissions collide.

Contention-based vs. contention-free MAC?::Contention-based: stations compete, collisions possible, non-deterministic, good for low/medium and bursty load. Contention-free: access allocated in advance, no collisions, deterministic, good for high load and fairness.

ALOHA?::No coordination at all: stations send whenever they want; collisions possible; no fairness; very simple.

Slotted ALOHA?::Fixed-length packets sent only in fixed time slots (needs a common time base): only complete collisions, better throughput, more delay; used in the first GSM networks.

Peak throughput of ALOHA vs. slotted ALOHA?::About 18 % vs. about 37 % of the channel capacity.

p-persistent CSMA?::Medium busy: keep listening until idle. Medium idle: send with probability p; with probability 1−p wait for the next slot and sense again.

Non-persistent CSMA?::Medium busy: wait a random time before sensing again. Medium idle: send immediately.

CSMA: effect of a lower p?::Better throughput (especially under high load), but latency may suffer.

Why collision avoidance (CSMA/CA) in WLANs?::Collisions cannot be detected reliably: sending and listening at the same time is hard, and there is the hidden terminal problem.

DIFS and SIFS?::DIFS (about 50 µs): the medium must be idle this long before a station sends. SIFS (about 10 µs): the receiver waits this long before sending the ACK.

CSMA/CA backoff?::Random value between minimum and maximum contention window × slot time; the counter pauses while the medium is busy and continues after an idle DIFS.

MACA idea?::Sender and receiver first exchange RTS and CTS control frames that announce how long the medium will be occupied, so all stations (also hidden ones) learn about the transmission.

What is the NAV?::Network Allocation Vector: a counter each station keeps with the expected occupation time of the medium; it does not send until the NAV reaches 0.

MACA: where can collisions still happen?::Only during the transmission of RTS and CTS frames.

MACA advantages and drawbacks?::Advantages: fewer collisions (solves hidden terminals), less energy. Drawbacks: reservation delays, RTS/CTS overhead.

Token passing?::A token frame circulates and defines the sending order; only the station holding the token may send (token ring, token bus).

TDMA / FDMA / CDMA?::TDMA: time slots assigned to hosts. FDMA: spectrum split into sub-channels per host or link. CDMA: simultaneous sending on the same frequency with orthogonal codes.

## Errors and detection

Causes of transmission errors?::Signal deformation (attenuation), noise (thermal/electronic), crosstalk, short-time disturbances (cosmic radiation, bad insulation).

Typical BER: radio, Ethernet, fiber?::Radio link 10^-3 to 10^-4; Ethernet 10^-9 to 10^-10; fiber 10^-10 to 10^-12.

Single-bit errors or burst errors — which are more common?::Burst errors (consecutive bit errors).

Codeword structure n, m, r?::n = m + r bits: m payload bits and r > 0 checksum bits.

Hamming distance of a code?::The minimum number of differing bits between two valid codewords.

Hamming distance needed to detect k errors / correct k errors?::Detect k errors: d = k + 1. Correct k errors: d = 2k + 1.

1-D parity on 7-bit characters: Hamming distance and capability?::d = 2: detects 1-bit errors (any odd number of errors), corrects none.

What does 2-D parity detect?::All 1-, 2- and 3-bit errors and most 4-bit errors.

Degree of the generator polynomial 100101 and its use?::Degree 5 (number of bits minus 1); the sender appends 5 zero bits before dividing.

CRC at the sender?::Append degree-many zero bits, divide by the generator from the left using XOR only, the remainder (padded to degree bits) is the checksum, append it to the payload.

CRC at the receiver?::Divide the received frame by the generator using XOR; remainder 0 → no error detected.

Which CRC does Ethernet use?::CRC-32.

Error detection + retransmission vs. forward error correction?::Detection is cheaper on fairly reliable links; FEC (e.g. Hamming code) is cheaper on error-prone links like wireless because it saves retransmissions.

Code with only 0000000000, 0000011111, 1111100000, 1111111111: distance, detect, correct?::d = 5: detects up to 4, corrects up to 2 bit errors.

## Understanding — write your own answers ✍️

✍️ Compute the CRC checksum for payload 10101 with generator x^5 + x^2 + 1. What is the transmitted frame?
?
✍️ your answer (paper, XOR division) — then check [[04-Data-Link-MAC-Error-Control|CN-04]] gold example 1

✍️ Explain the hidden terminal problem and how RTS/CTS solves it.
?
✍️ your answer — then check [[04-Data-Link-MAC-Error-Control|CN-04]]

✍️ Which requirements must a code fulfil to detect and to correct errors? (self-check question)
?
✍️ your answer — then check [[04-Data-Link-MAC-Error-Control|CN-04]]

✍️ Which performance can ALOHA, CSMA variants and contention-free MAC achieve, and when is which preferable? (self-check question)
?
✍️ your answer — then check [[04-Data-Link-MAC-Error-Control|CN-04]]
