#!/usr/bin/env python3

import sys
import progressbar
import re

buf = ""
re_pattern = "admin"  # feel free to use regex

def decode(input, key=0x22):  # 0x22 = 0xDE ^ 0xAD ^ 0xBE ^ 0xEF
    output = ""
    for n in input:
        output += chr(n^key)
    return output

def pattern_not_found(input, key):
    return pattern not in decode(input, key)

def guess_key(input):
    print("Guessing the key.")
    keys = progressbar.ProgressBar()
    for key in keys(range(1, 0xff)):
        if re.search(re_pattern, decode(input, key)):
            return key
    raise Exception("Key not found")

with open(sys.argv[1], 'rb') as f:
    buf = f.read()
    key = guess_key(buf)
    print("Key found: {}".format(hex(key)))
    buf = decode(buf, key)

with open(sys.argv[1] + '-dexored', 'wb') as f:
    f.write(buf.encode())
    print("dexored file written.")
