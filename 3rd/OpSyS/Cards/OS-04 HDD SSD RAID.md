---
course: Operating Systems
source: "[[04_HDD_SSD_RAID]]"
---
#flashcards/os/04-storage

# OS-04 HDD, SSD, RAID — Cards

> [!info] How to use
> Fill every ✍️ answer from memory first (calculator allowed, as in the exam), then check in [[04_HDD_SSD_RAID|OS-04]]. Plan: [[00 OpSys Plan]]

## HDD

Track / cylinder / sector?::Track: circular ring on a platter surface. Cylinder: all tracks at the same arm position on all platters. Sector (block): smallest addressable unit (512 B, today often 4 KB).

What is a cluster?::A group of sectors of fixed size (e.g. 4 or 8 KB) — the unit the file system allocates.

How many heads does an HDD with 3 platters have?::6 — one per platter side.

CHS maximum capacity and its formula?::1024 cylinders × 255 heads × 63 sectors × 512 B = 8,422,686,720 B ≈ 7.844 GB.

Why 63 sectors per track, not 64?::6 bits are available, but sector numbering starts at 1 (there is no sector 0).

Why 255 heads although no HDD has more than 16?::Logical heads: the BIOS interface offers 8 bits for heads; the drive translates logical CHS to its real geometry.

What is LBA and when is it used?::Logical Block Addressing: all sectors are numbered consecutively from 0; used for HDDs larger than 7.844 GB.

Average rotational latency formula?::Half a rotation: 0.5 × 60,000 ms / RPM = 30,000 / RPM ms (7200 RPM ≈ 4.17 ms).

Average access time of an HDD?::Average seek time + average rotational latency.

Typical average seek time?::5–15 ms for modern HDDs.

## SSD and flash

Why is "Solid State Disk" a wrong name?::An SSD contains no disk (no rotating platters); it is flash memory — Solid State Drive.

Two advantages of SSDs over HDDs?::Any two of: fast access time, low power consumption, no noise, mechanical robustness, low weight.

Reading a flash cell: how is 0 vs. 1 decided?::About 5 V at the control gate: if current flows between source and drain the floating gate is uncharged (1); if not, it holds electrons (0).

Writing (programming) a flash cell?::High positive voltage (about 12 V) at the control gate: electrons tunnel into the floating gate (Fowler-Nordheim tunneling).

Why is erasing flash more complex than reading?::Erasing works only on whole blocks: the block is copied to a buffer, erased (negative voltage), and rewritten with the modified data.

NOR vs. NAND flash?::NOR: every cell has its own data line, random access, good latency (firmware). NAND: cells grouped into pages/blocks, higher density, cheaper, page-wise access (SSDs, USB sticks).

SLC / MLC / TLC / QLC?::1 / 2 / 3 / 4 bits per cell. More bits: cheaper per bit, slower writes, fewer program/erase cycles. SLC is the most expensive and most durable.

What is wear leveling?::Algorithms that distribute write/erase operations evenly over all blocks so that hot blocks do not wear out early.

## RAID

RAID 0?::Striping without redundancy; higher data rate; net capacity n × drive; one drive failure loses data.

RAID 1?::Mirroring: at least 2 drives store identical data; net capacity = smallest drive; survives the failure of all but one drive.

RAID 2?::Bit-level striping with Hamming code error correction (obsolete).

RAID 3 vs. RAID 4?::Both use a dedicated parity drive (write bottleneck). RAID 3: byte-level striping. RAID 4: block-level striping.

RAID 5?::Block-level striping with distributed parity; at least 3 drives; net capacity (n−1) × drive; tolerates 1 drive failure.

RAID 6?::Block-level striping with double distributed parity; at least 4 drives; net capacity (n−2) × drive; tolerates 2 drive failures.

How is parity computed and a lost block restored?::Parity = XOR of all data blocks of a stripe; a lost block = XOR of the remaining blocks and the parity.

What does RAID 10 mean?::RAID 1+0: mirrored pairs (RAID 1) combined by striping (RAID 0). In "RAID xy", x is the inner, y the outer level.

Hardware vs. host vs. software RAID?::Hardware: controller with its own processor (no CPU load, OS-independent, expensive). Host/FakeRAID: cheap controller or firmware, the CPU does the work, driver-dependent. Software: the OS does it (no extra cost, CPU load, OS-dependent).

## Understanding — write your own answers ✍️

✍️ Compute the CHS capacity with only 16 heads. Which addressing does a 500 GB drive need, and why?
?
✍️ your answer — then check [[04_HDD_SSD_RAID|OS-04]] §4

✍️ 7200 RPM, average seek time 9 ms: average access time?
?
✍️ your answer — then check [[04_HDD_SSD_RAID|OS-04]] §5

✍️ 6 drives of 2 TB: net capacity and tolerated failures for RAID 0, 1, 5 and 6.
?
✍️ your answer — then check [[04_HDD_SSD_RAID|OS-04]] §13

✍️ B1 = 1010, B2 = 0110, B3 = 1100: compute the parity, then restore B2 after its drive fails.
?
✍️ your answer — then check [[04_HDD_SSD_RAID|OS-04]] §12

✍️ Draw an HDD schematic and explain sector, track, cylinder and cluster (exam WS24/25, 4 points).
?
✍️ your answer (draw on paper) — then check [[04_HDD_SSD_RAID|OS-04]] §2–3
