#! /usr/bin/env/python
from __future__ import print_function, unicode_literals

import re

with open('show_ipv6_intf.txt') as f:
    output = f.read()

#print(output)

ipv6_list = []

addr_1 = re.search(r'^\s+(\d+\S+)\s\S+$', output, flags=re.M).groups(1)
addr_2 = re.search(r'^\s+(\d+\S+)$', output, flags=re.M).groups(1)

ipv6_list.append((str(addr_1[0])))
ipv6_list.append((str(addr_2[0])))

print(ipv6_list)



