#!/bin/bash

python3 ./builder.py "$@"
./make_payload.sh

python3 ./tester.py
./test_shellcode.sh
