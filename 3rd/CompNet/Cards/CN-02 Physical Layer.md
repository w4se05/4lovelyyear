---
course: Computer Networks
source: "[[02-Physical-Layer]]"
---
#flashcards/cn/02-physical

# CN-02 Physical Layer — Cards (script 03)

> [!info] How to use
> Fill every ✍️ answer from memory first (calculator allowed), then check in [[02-Physical-Layer|CN-02]]. Plan: [[00 CompNet Plan]]

## Signals

What is a signal?::The physical representation of data: a chronological sequence of physical values (voltage, light, electromagnetic waves).

Analog vs. digital signal?::Analog: time- and value-continuous. Digital: time- and value-discrete.

Parameters of a periodic signal?::Period T, frequency f = 1/T, amplitude A, phase φ: s(t) = A · sin(2πft + φ).

Quantization, sampling, coding?::Quantization: map continuous values to discrete intervals. Sampling: measure at discrete points in time. Coding: represent each sample as a bit word.

Bits per sample with N quantization intervals?::⌈log2 N⌉ bits.

Bit rate vs. symbol rate (units, relation)?::Bit rate: bit/s. Symbol rate: baud (symbols per second). r_b = r_s · log2 V, with V = number of symbol values.

When are bit rate and symbol rate equal?::When every symbol carries exactly one bit (V = 2, binary signal).

Can the bit rate be smaller than the symbol rate?::Yes — if a code needs more than one symbol per bit, e.g. Manchester code (2 symbols per bit).

## Channel capacity

Hartley's law (noiseless channel)?::R_max = 2 · H · log2 V bit/s, H = bandwidth in Hz, V = number of symbol values.

Why can a symbol not carry an arbitrary number of bits? (sheet 2)::Because of noise — the Shannon-Hartley theorem gives the upper bound.

Shannon–Hartley theorem (noisy channel)?::R_max = H · log2(1 + S/N) bit/s, with S/N as a linear ratio.

Convert SNR in dB to the linear ratio?::S/N = 10^(SNR_dB / 10).

What is attenuation?::Weakening of the signal amplitude; it grows with distance on all media and depends on the frequency.

AWGN?::Additive White Gaussian Noise — the typical noise model (Gaussian channel).

Bit error rate?::BER = number of erroneous bits / number of transmitted bits.

What does Fourier analysis say about square waves?::A square wave is a sum of sine waves: the fundamental frequency plus odd harmonics; at least the fundamental, 3rd and 5th harmonic are needed to transmit it clearly — this defines the bandwidth needed.

## Encoding and modulation

Baseband vs. broadband?::Baseband: the digital signal is sent directly using a line code. Broadband: the data is modulated onto an analog carrier signal.

Why do computer networks need line codes? (sheet 2)::Computers are digital, transmission media work analog — a line code specifies how binary data is converted into signals.

NRZ: how does it work, and its two problems?::Logical 0 = low level, logical 1 = high level. Problems with long runs of equal bits: baseline wander and clock recovery (no level changes).

Manchester code (as on the slides)?::2 levels; level change in every bit cell: logical 1 = rising edge, logical 0 = falling edge. Self-clocking, but double symbol rate.

ASK / FSK / PSK / QAM?::Data carried by the amplitude / frequency / phase / amplitude and phase of a carrier wave.

## Media and technologies

Structure of a coaxial cable (inside out)?::Inner conductor, insulation (dielectric), outer conductor (shield), outer jacket.

Why are twisted-pair wires twisted?::Twisting protects against electromagnetic interference and crosstalk.

Which component determines the performance of a twisted-pair link?::The component with the lowest category.

What distinguishes twisted-pair categories?::Number of twists per cm (more twists = less noise), wire thickness, shielding → higher frequencies/data rates.

Advantages of fiber over copper?::High data rates over long distances, no electromagnetic emission, immune to electromagnetic interference.

DSL vs. DOCSIS?::DSL: uses the whole spectrum of the copper telephone line (DMT modulation, DSLAM at the provider). DOCSIS: data over the cable-TV coax network (cable modem at home, CMTS at the provider).

Ethernet and WLAN standards?::Ethernet: IEEE 802.3 (physical layer + parts of data link layer). WLAN: IEEE 802.11 (Wi-Fi is a marketing brand).

WEP vs. WPA2?::WEP: static 40- or 104-bit keys, cracked within minutes. WPA2: AES-based, the current standard (WPA3 is its successor).

## Understanding — write your own answers ✍️

✍️ 33.6 kbit/s modem at 3429 baud (sheet 2): bits per symbol? Required SNR on a 3.1 kHz line? Signal strength if the noise is 0.1 kW?
?
✍️ your answer (show the steps) — then check the official solution: [exercise session 4](file:///C:/Users/hongp/OneDrive/Desktop/WS2627/CompNet/compnet-ws26-exercise-04.pdf), PDF p. 31–38

✍️ Why does a telephone modem use modulation instead of a line code?
?
✍️ your answer — then check [[02-Physical-Layer|CN-02]] §4–5 and §8 · official answer: session 4, p. 33–34

✍️ Which line codes guarantee a level change for every bit, and why does that matter? (sheet 2)
?
✍️ your answer — then check [[02-Physical-Layer|CN-02]] §4 · official answer: session 4, p. 29–30

✍️ The three requirements an encoding must fulfil?
?
✍️ your answer — then check [[02-Physical-Layer|CN-02]] §4

✍️ Which challenges arise particularly in wireless networks? (self-check question)
?
✍️ your answer — then check [[02-Physical-Layer|CN-02]] §7

✍️ How can existing infrastructure be used to bridge the last mile? (self-check question)
?
✍️ your answer — then check [[02-Physical-Layer|CN-02]] §8
