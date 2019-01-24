#!/usr/bin/env python

import sys

args = sys.argv[1:]
flag = False #while this is true, we'll print the bytecode
bytestring = ''

for line in sys.stdin:
    if flag: # wanted label found, now get all its bytecode
        if line == '\n':
            flag = False
            continue
        bytestring += (line.split('\t')[1].strip() + ' ')
    if not flag: # we're looking for a wanted label
        for arg in args:
            label = '<' + arg + '>:'
            if label in line:
                flag = True
                break

# strip excess spaces, split, split on spaces, and join with the escape
bytestring = '\\x'.join(bytestring.strip().split(' '))
print('\\x' + bytestring) # join didn't escape the first, so there we go
