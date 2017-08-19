#!/usr/bin/env python3
# supply document file as argument for its content to be transformed
import random
import os
import sys

VOWELS = ("a", "e", "i", "o", "u")

if len(sys.argv) is 1:
    print("please supply a filename")
    sys.exit(-1)

fn = sys.argv[1]
f = open(fn, 'r')

message = f.read()

new_message = ""
for letter in message:
    if letter not in VOWELS:
        new_message += letter
    else:
        new_message += random.choice(VOWELS)

new_f = open(fn+'.out', 'w')
new_f.write(new_message)

print("transformed text of file {} and wrote" 
        "contents to {}.out".format(fn, fn))

