# Linux Kernel

## [1] User Space and Kernel Space

The term "operating system" refers to a system that provides the functionality to execute various programs.

-   The 8051 processor executes programs by reading machine code sequentially from ROM address 0.

    If you want to run a different program, you need to write it to the ROM.

-   An operating system provides a management system that allows the execution of multiple programs.

    At least two programs exist in memory simultaneously.

### Memory Space Segmentation for Security

To ensure security in the Linux kernel, a careful division of memory space into user space and kernel space is implemented.

-   In the Linux i386 32-bit environment, user space is allocated 3G, and kernel space is allocated 1G.

The size of user space and kernel space varies depending on the CPU architecture and whether it's 32-bit or 64-bit.

This implementation is hardware-dependent, and each CPU may have a different configuration.

-   In `include/asm-i386/page.h`, you can find the boundary value (0xC000 000) between kernel space and user space in `__PAGE_OFFSET` or `PAGE_OFFSET`.
-   In the Windows NT environment, the size of this area may vary according to the design chosen by the kernel designer, such as using 2G for user space and 2G for kernel space.

---

## [2] Memory Access Permissions for Enhanced Security

In Linux, similar to restricting access to files created by other users, permissions are crucial in kernel space and user space, allowing memory access only when the appropriate permissions exist.

Checking for permissions on every memory access may take more time than program execution itself, so this is handled by the CPU itself.

The permissions provided by the CPU are referred to as Privilege Rings or Privilege Levels.

![Privilege Levels](README.assets/image-20201012135512770.png)

-   Privilege Levels range from 0 to 3, offering four levels.
    -   Level 0: Kernel space (Core)
    -   Levels 1, 2: Kernel space (Subsystem)
    -   Level 3: User space
-   Typically, operating systems use only levels 0 and 3 for enhanced security.
