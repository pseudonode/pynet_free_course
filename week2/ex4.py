#!/usr/bin/env python
from __future__ import print_function, unicode_literals
from pprint import pprint

with open("show_ip_int_brief.txt") as f:
    file = f.readlines()

# pprint(file)

for item in file:
    if 'FastEthernet4' in item:
        my_string = item
        my_string = my_string.split()
        my_tuple = (my_string[0], my_string[1])

pprint(my_string)
pprint(my_tuple)
