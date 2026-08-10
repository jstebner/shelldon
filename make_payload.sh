#!/bin/bash
gcc -m64 -c -o shellcode.o shellcode.S
objcopy -S -O binary -j .text shellcode.o shellcode.bin
rm -rf shellcode.o
echo 'shellcode.bin written'
