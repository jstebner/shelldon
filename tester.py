def main():
    with open("runner.TEMPLATE","r") as f:
        template = f.read()
    with open("shellcode.bin", "rb") as f:
        payload = f.read()
    payload = "\\x"+payload.hex(sep=":").upper().replace(":", "\\x")
    with open("runner.c", "w") as f:
        f.write(template.replace("$CODE", payload))
    print("test runner.c written")

if __name__ == "__main__":
    main()
