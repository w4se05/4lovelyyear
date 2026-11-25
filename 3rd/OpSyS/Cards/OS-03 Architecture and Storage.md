---
course: Operating Systems
source: "[[03_Computer_Architecture_IO_Storage]]"
---
#flashcards/os/03-architecture

# OS-03 Computer Architecture, I/O, Data Storage — Cards

> [!info] How to use
> Fill every ✍️ answer from memory first, then check in [[03_Computer_Architecture_IO_Storage|OS-03]]. Plan: [[00 OpSys Plan]]

## CPU and buses

Main components of the Von Neumann architecture?::CPU (control unit + ALU), main memory shared by program and data, input/output devices, connected by buses (data, address, control).

Three components of the CPU (official solution)?::Control unit, arithmetic logic unit (ALU), memory (registers; caches).

Task of the data bus?::Transmits data between CPU, main memory and I/O devices; the number of lines = how much data per clock cycle.

Task of the address bus?::Transmits memory addresses; its width n limits the addressable memory to 2^n addresses.

Task of the control bus?::Transmits commands (e.g. read/write requests) from the CPU and status signals from the I/O devices (also interrupt lines).

Address bus vs. control bus in one sentence?::Components are addressed via the address bus and told what to do via the control bus.

How many address lines are needed to address 8 GB (byte-addressed)?::33, because 8 GB = 2^3 · 2^30 = 2^33 bytes.

What is the Front Side Bus?::The bus between CPU and chipset (northbridge) containing address, data and control bus — used until about 2008/9.

Northbridge vs. southbridge?::Northbridge: close to the CPU, fast components (memory controller, graphics/PCIe). Southbridge: slower I/O (USB, SATA, audio, network).

What moved into the CPU around 2008, and what next?::First the memory controller, then the remaining northbridge functions (e.g. PCIe, graphics); today chiplets and SoCs.

## I/O

Character device vs. block device (criterion + examples)?::Criterion: minimum transfer unit. Character device: each single character (keyboard, mouse, serial port, printer). Block device: only whole blocks (HDD, SSD, CD/DVD, USB stick).

Busy waiting (programmed I/O)?::The driver sends the request and waits in an infinite loop, polling the controller until the data is ready — causes CPU load.

Interrupt-driven I/O?::The driver starts the I/O; the controller raises an interrupt when the data is ready; the CPU can do other work meanwhile. Needs an interrupt controller and an interrupt line on the control bus.

Direct Memory Access (DMA)?::A DMA controller transfers data directly between device and main memory; the CPU is only informed by an interrupt at the end — no CPU load during the transfer.

Which concept: the CPU periodically polls? Reading causes no CPU load?::Polling = busy waiting. No CPU load = DMA.

## Storage

Random access vs. sequential access?::Random: any location can be accessed directly (RAM, HDD, SSD). Sequential: the medium must be searched from the beginning (magnetic tape).

Primary / secondary / tertiary storage?::Primary: CPU accesses directly (registers, cache, main memory). Secondary: only via a controller, permanently connected (HDD, SSD). Tertiary: via a controller, removable/robotic (tape libraries, optical media).

Near-line vs. off-line storage?::Near-line: connected automatically without humans (tape library). Off-line: media stored in a shelf, a human must insert them.

SRAM vs. DRAM?::SRAM: flip-flops, fast, expensive, no refresh (caches). DRAM: charge in capacitors, slower, cheaper, needs periodic refresh (main memory).

Memory hierarchy: what changes moving up towards the registers?::Faster access, higher cost per bit, smaller capacity.

How does the memory hierarchy work on the first access of a record?::A copy of the record travels up the hierarchy to the top; later accesses are served from the faster levels; modified data must travel back down.

Write-through?::Modifications are immediately propagated to the lower layers. Consistency guaranteed, worse performance.

Write-back?::Modifications are propagated only when the page is removed from the cache. Better performance, risk of inconsistency/data loss; uses the dirty bit.

Why is a dirty bit used?::It marks modified cache pages, so only modified pages are written back when they are evicted (write-back).

Registers / cache / main memory — access speed?::Registers: immediately, at CPU clock speed. Cache (L1, L2, L3): copies of main memory parts, fast. Main memory (RAM): every request the cache cannot serve.

## Understanding — write your own answers ✍️

✍️ Explain the Von Neumann (fetch–decode–execute) cycle phase by phase.
?
✍️ your answer — then check [[03_Computer_Architecture_IO_Storage|OS-03]] §2

✍️ Keyboard, SSD, sound card: which I/O method would you choose for each, and why?
?
✍️ your answer — then check [[03_Computer_Architecture_IO_Storage|OS-03]] §5

✍️ Trace write-through vs. write-back for: modify A, modify A, modify B, evict A, evict B. How many writes reach the lower layer in each case?
?
✍️ your answer — then check [[03_Computer_Architecture_IO_Storage|OS-03]] §8

✍️ 36-line address bus, 64-line data bus: maximum addressable memory? Bytes per transfer?
?
✍️ your answer — then check [[03_Computer_Architecture_IO_Storage|OS-03]] §12
