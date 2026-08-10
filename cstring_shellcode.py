with open("shellcode.bin", "rb") as f:
    print("\\x"+f.read().hex(sep=":").upper().replace(":", "\\x"))
