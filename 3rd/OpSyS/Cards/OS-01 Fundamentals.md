---
course: Operating Systems
source: "[[01_OS_Fundamentals_and_Generations]]"
---
#flashcards/os/01-fundamentals

# OS-01 Fundamentals and Generations — Cards

> [!info] How to use
> Before your first review: replace every ✍️ answer with your own answer from memory, then check it in [[01_OS_Fundamentals_and_Generations|OS-01]]. After that, review daily. Plan: [[00 OpSys Plan]]

## Place and structure

To which two branches of computer science do operating systems belong?::Practical computer science and technical computer science.

User process vs. system process?::A user process processes the users' jobs; a system process provides services of the operating system.

What is the kernel (definition of slide set 1)?::All components of the OS that are not implemented as system processes.

Layers of a computer system from top to bottom, and which of them form the OS?::User processes, system processes, kernel, hardware. The OS = system processes + kernel.

Name the four areas an OS manages (core functionalities).::Processes (management, scheduling, synchronization, communication), users (user management), data (file systems, storage, memory management), hardware (hardware management).

## Generations

Three requirements of a universal computer?::Stored program, conditional jump (GOTO), separation of memory and processing unit.

Generation 1: years, technology, OS?::1940–1955; electron tubes, relays, jack panels (plugboards); programs are circuits; no operating system.

Generation 2: years, technology, key OS concept?::1955–1965; transistors and punch cards; batch processing.

Objective of batch processing?::Maximize CPU utilization (automatic, sequential execution of jobs without user interaction).

What is spooling?::Removing I/O workload from the CPU with additional hardware, so I/O runs concurrently with processing (e.g. frontend/backend computers, tapes).

How much does one punch card hold?::One line of text with 80 characters (or the equivalent binary data).

Generation 3: years, technology, key concepts?::1965–1980; integrated circuits; multitasking, time-sharing, memory protection, file systems, swapping, scheduling.

Objective of time-sharing?::Fair distribution of computing time among the users (short response times) via time slices.

What is memory protection?::Memory is split and running programs are separated, so a bug or crash in one program does not affect the others.

What is swapping?::Moving data between main memory and background memory (HDD/SSD).

What is scheduling?::Automatic creation of an execution plan (schedule) that allocates time-limited resources to users or processes.

Generation 4 (1980–2000): keywords?::Highly integrated circuits, personal computers, graphical user interfaces, networking (e.g. MS-DOS, Windows, MINIX, Ethernet).

Generation 5 (2000–2022): keywords?::"The network is the computer": distributed systems (cluster, cloud, grid, P2P), multicore processors and parallelization, mobile devices.

Generation 6 (2022–): keyword?::Generative AI available to everyone (public release of ChatGPT in 2022).

## Understanding — write your own answers ✍️

✍️ Why does batch processing speed up the execution of several jobs compared to manual operation?
?
✍️ your answer — then check [[01_OS_Fundamentals_and_Generations|OS-01]] §7

✍️ Compare batch processing and time-sharing: interaction, objective, generation.
?
✍️ your answer — then check [[01_OS_Fundamentals_and_Generations|OS-01]] §8

✍️ In 1975 one user's program crashes, but all other users keep working. Which concept makes this possible, and how does it work?
?
✍️ your answer — then check [[01_OS_Fundamentals_and_Generations|OS-01]] §8

✍️ Trace how the main objective of operating systems changed from generation 2 → 3 → 5.
?
✍️ your answer — then check [[01_OS_Fundamentals_and_Generations|OS-01]] §9
