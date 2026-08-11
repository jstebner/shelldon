echo -e "shellcode:\n"
python3 -c 'with open("shellcode.bin", "rb") as f: print("\\x"+f.read().hex(sep=":").upper().replace(":", "\\x"))'

echo -e "\nhexdump:\n"
xxd shellcode.bin
