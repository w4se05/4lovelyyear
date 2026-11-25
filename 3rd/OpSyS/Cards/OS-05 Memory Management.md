---
course: Operating Systems
source: "[[05_Memory_Management_Paging_Replacement]]"
---
#flashcards/os/05-memory

# OS-05 Memory Management — Cards

> [!info] How to use
> This is the most calculation-heavy deck. Fill every ✍️ answer on paper first, then check in [[05_Memory_Management_Paging_Replacement|OS-05]]. Plan: [[00 OpSys Plan]]

## Partitioning and buddy

Three concepts of memory management in slide set 5?::Static partitioning, dynamic partitioning, buddy memory allocation.

Static partitioning — two drawbacks?::Internal fragmentation always occurs; the number of partitions limits the number of processes.

Dynamic partitioning — main drawback?::External fragmentation (unusable gaps between processes).

First Fit / Next Fit / Best Fit?::First Fit: first fitting block from the start (fast). Next Fit: from the latest allocation (quickly fragments the big free area at the end). Best Fit: the block that fits best (slow, many mini-fragments).

Buddy allocation — how is a request served?::Round the request up to the next power of 2; split a free block into two halves (buddies) repeatedly until a block of that size exists; allocate it.

Buddy allocation — what happens on free?::If the freed block's buddy is also free, both are merged into the bigger block; repeat upwards.

Which fragmentation does buddy allocation cause?::Internal fragmentation (rounding up to powers of 2), but little external fragmentation.

Where does Linux use buddy allocation and how to inspect it?::For page allocation in the kernel; /proc/buddyinfo shows per zone (DMA, DMA32, Normal) how many free chunks of 2^k pages exist (column k counted from 0).

## Real mode and protected mode

Real mode: maximum memory and why?::1 MB, because the 8086 address bus has 20 lines (2^20 bytes).

Real mode address calculation?::Physical address = segment × 16 + offset (segment:offset, 64 KB segments).

Main weakness of real mode?::No memory protection: every process can access the whole memory, including the OS.

Protected mode: since which CPU, and which two methods?::Since the Intel 80286. Methods: segmentation (80286, struck through in the course) and paging (since 80386).

The four memory management demands?::Relocation (no physical addresses in processes), protection (access checked by the CPU), shared use (collaboration via shared memory), increased capacity (use more memory than physically exists via swapping).

Virtual memory — core idea?::Each process gets its own protected address space of virtual addresses, translated to physical addresses; pages can be swapped out, so memory seems larger than RAM.

## Paging

Paging maps what to what?::Fixed-size virtual pages of processes to physical pages (frames) in main memory.

Why does paging avoid external fragmentation?::A process need not be contiguous; any free frame can hold any page.

What does the MMU do?::Translates virtual into physical addresses using the page table (raises exceptions on page faults or access violations).

Page table size: 32-bit, 4 KB pages, 4 B entries?::2^32 / 2^12 = 2^20 entries × 4 B = 4 MB per process.

Short vs. long pages?::Short: less internal fragmentation, but bigger page table. Long: smaller page table, more internal fragmentation.

Present bit / dirty bit / reference bit?::Present: page is in main memory. Dirty: page was modified (write back before eviction). Reference: page was accessed (used e.g. by Clock).

Two-level paging split for 32-bit addresses with 4 KB pages?::10 bits page directory index + 10 bits page table index + 12 bits offset.

Why multi-level paging?::It reduces main-memory usage: only the page tables that are actually needed must exist in memory.

Page fault — what happens?::The requested page is not in main memory (present bit 0): the MMU raises an exception, the OS reads the page from swap into a free frame, updates the page table, the process retries.

Access violation / general protection fault?::A process accesses a virtual address it may not access; the OS usually kills the process. Despite the name "segmentation fault" it is a paging issue.

## Replacement strategies

Hit rate and miss rate?::Hit rate = hits / requests; miss rate = misses / requests = 1 − hit rate.

OPT?::Replace the page that will not be requested for the longest time in the future — impossible to implement, used as benchmark.

LRU vs. LFU?::LRU: replace the page not used for the longest time. LFU: replace the page requested least often (reference counter).

FIFO and Belady's anomaly?::FIFO replaces the page that has been in memory longest. Belady's anomaly: with FIFO, more frames can cause more page faults.

Clock / Second Chance?::A pointer circles the frames: reference bit 1 → set to 0 and move on (second chance); reference bit 0 → replace this page.

Slide example 1 2 3 4 1 2 5 1 2 3 4 5 with 3 frames: misses of OPT, FIFO, LRU?::OPT 7, FIFO 9, LRU 10. FIFO with 4 frames: 10 (Belady's anomaly).

TTL and Random strategies?::TTL: each page gets a time to live; after it expires the page may be replaced. Random: replace random pages — simple, no bookkeeping.

## Understanding — write your own answers ✍️

✍️ Buddy trace on 1024 KB: A 100, B 240, C 60, D 251, free B, free A, E 75, free C, free E, free D. Draw every state and the internal fragmentation.
?
✍️ your answer (paper) — then check [[05_Memory_Management_Paging_Replacement|OS-05]] §5

✍️ Real mode: segment 2000, offset 100 (decimal). Physical address? Which memory area?
?
✍️ your answer — then check [[05_Memory_Management_Paging_Replacement|OS-05]] §6

✍️ Run FIFO, LRU and OPT on 2 3 2 1 5 2 4 5 3 2 5 2 with 3 frames. Count the misses and give the hit rates.
?
✍️ your answer (paper) — then check [[05_Memory_Management_Paging_Replacement|OS-05]] §10

✍️ Put the page-fault steps in order and explain who does each step (process, MMU, OS).
?
✍️ your answer — then check [[05_Memory_Management_Paging_Replacement|OS-05]] §9

✍️ Explain with numbers why two-level paging saves memory compared with one 4 MB page table.
?
✍️ your answer — then check [[05_Memory_Management_Paging_Replacement|OS-05]] §8
