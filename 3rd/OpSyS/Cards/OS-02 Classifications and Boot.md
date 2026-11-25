---
course: Operating Systems
source: "[[02_OS_Classifications_Kernels_Layers_Booting]]"
---
#flashcards/os/02-classifications

# OS-02 Classifications, Kernels, Layers, Booting — Cards

> [!info] How to use
> Fill every ✍️ answer from memory first, then check in [[02_OS_Classifications_Kernels_Layers_Booting|OS-02]]. Plan: [[00 OpSys Plan]]

## Classifications

Singletasking vs. multitasking?::Singletasking: only one program runs at a time, others run one after another. Multitasking: several programs run at the same time, truly parallel (several cores) or quasi-parallel (one core, time slices).

Main reason for multitasking?::Processes often wait for external events (input, I/O, messages, network); meanwhile the CPU can run other processes, so it is better utilized.

Single-user vs. multi-user OS?::Single-user: only one user at any point in time. Multi-user: several users work simultaneously and share the resources; their data must be protected from each other.

What is a half multi-user OS? Example?::Different users can work with the system only one after the other, but their data and processes are protected from each other — desktop Windows NT/XP/Vista/7/8/10/11.

Why is a multi-user, singletasking OS impossible?::Simultaneous users need several programs running at the same time, so multi-user requires multitasking.

Classify MS-DOS, Windows 95 and Linux (tasking/users).::MS-DOS: singletasking, single-user. Windows 95: multitasking, single-user. Linux/UNIX: multitasking, multi-user.

What does the bit number of an OS mean?::The memory address length the OS works with internally; an n-bit OS can address 2^n memory units.

What is a real-time OS? Two essential criteria?::A multitasking OS with additional real-time functions to comply with time conditions. Criteria: response time (short latency) and meeting deadlines.

Hard vs. soft real-time? One example each.::Hard: deadlines must be met strictly, delays have disastrous consequences (airbag, flight control). Soft: tolerances allowed, delays cause acceptable costs (telephone system, video streaming, ticket machine).

Distributed OS / Single System Image?::An OS that controls processes on several computers of a cluster; the individual computers are hidden, users see one large virtual computer. The concept never left research.

## Kernel architectures

Kernel mode vs. user mode?::Kernel mode: full access to hardware and all instructions (kernel runs here). User mode: restricted, processes must ask the kernel via system calls.

Monolithic kernel: contents, advantage, drawback?::Memory and process management, IPC, drivers, file systems all in the kernel. Advantage: fewer context switches, better performance, grown stability. Drawback: a crashed component can crash the whole system.

Microkernel: contents, advantage, drawback?::Only essential memory/process management, synchronization and IPC; drivers and file systems run as user-mode processes. Advantage: components easy to exchange, best stability and security in theory. Drawback: slower (more context switches).

Hybrid kernel (macrokernel)?::Trade-off between monolithic and microkernel: some components (e.g. drivers, file systems) moved into the kernel for performance reasons.

Classify GNU HURD, Linux, macOS X, Windows NT.::GNU HURD: microkernel. Linux: monolithic. macOS X: hybrid. Windows NT: hybrid.

What was kHTTPd and what does it teach?::A web server inside the Linux kernel: faster (no user/kernel mode switches), but a bug can crash or compromise the whole kernel — moving functions into the kernel trades safety for speed.

Minimum of 3 layers of an OS?::Innermost: hardware-dependent parts (easy porting). Central: basic I/O services (libraries, interfaces). Outermost: applications and user interface.

## Booting

The 7 boot steps (Linux/UNIX) in order?::1 switch on, 2 firmware + self-test (POST), 3 boot loader, 4 kernel + temporary root file system (initrd/initramfs), 5 mount real root file system, 6 init/systemd (PID 1) + system processes, 7 pass control to the users.

Firmware of classic vs. modern computers?::Classic: BIOS. Modern: UEFI.

What is the task of the firmware at start?::Initialize the hardware, run the Power-On Self-Test (POST), find the boot device and start the boot loader.

What is a boot loader? Examples?::A program that loads the operating system (kernel); e.g. GRUB, Windows Boot Manager, Clover.

Where is the boot loader stored?::Classic partition table: in the 512-byte Master Boot Record (MBR). GPT: in the EFI System Partition (ESP).

Why initrd / initramfs?::A temporary root file system in RAM with the drivers/modules the kernel needs to access the real root file system before it is mounted.

First user-mode process and its PID?::init (or systemd) with PID 1; all other user-mode processes descend from it.

## Understanding — write your own answers ✍️

✍️ One advantage and one drawback of autonomous subsystems such as Intel ME / AMD PSP. (exam WS24/25, 4 points)
?
✍️ your answer — then check [[02_OS_Classifications_Kernels_Layers_Booting|OS-02]] §9

✍️ A colleague wants to move the web, mail and SSH servers into kernel mode. Give one argument for and one against.
?
✍️ your answer — then check [[02_OS_Classifications_Kernels_Layers_Booting|OS-02]] §7

✍️ What does a getty process do, and how many does the OS start? (exam WS24/25)
?
✍️ your answer — then check slide set 2, boot step 7 / [[02_OS_Classifications_Kernels_Layers_Booting|OS-02]] §9

✍️ Convert chmod 640 to symbolic form and say what each class may do. Then convert rwxr-x--x to octal.
?
✍️ your answer — then check [[02_OS_Classifications_Kernels_Layers_Booting|OS-02]] §11
