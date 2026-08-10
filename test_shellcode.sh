#!/bin/bash
python3 ./tester.py
gcc -o runner -z execstack -fno-stack-protector ./runner.c
echo 'runner compiled, run it'
