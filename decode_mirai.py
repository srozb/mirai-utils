#!/usr/bin/env python

import sys

def decode(input):
    key = 0xdeadbeef
    k1 = key & 0xFF
    k2 = (key>>8) & 0xFF
    k3 = (key>>16) & 0xFF
    k4 = (key>>24) & 0xFF
    output = ""
    for n in input:
        output += chr(ord(n)^k4^k3^k2^k1)
    return output

buf = ""

with open(sys.argv[1], 'rb') as f:
    buf = f.read()
    buf = decode(buf)

with open(sys.argv[1] + '-dexored', 'wb') as f:
    f.write(buf)
