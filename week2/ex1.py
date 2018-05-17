#!/usr/bin/env python
from __future__ import print_function

file = open("show_version.txt")
output = file.read()
file.close()

print(output)
print(type(output))

with open("show_version.txt") as f:
    output = f.readlines()
print(output)
print(type(output))
