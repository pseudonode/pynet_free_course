#! /usr/bin/env/python
from __future__ import print_function, unicode_literals
import re

show_version = '''
Cisco 881 (MPC8300) processor (revision 1.0) with 236544K/25600K bytes of memory.
Processor board ID FTX0000038X

5 FastEthernet interfaces
1 Virtual Private Network (VPN) Module
256K bytes of non-volatile configuration memory.
126000K bytes of ATA CompactFlash (Read/Write)
'''

model = re.search('Cisco (?P<model>\S+)', show_version)
model = model.groupdict()['model']
memory = re.search('(?P<memory>\d+\S\/\d+\S)', show_version)
memory = memory.groupdict()['memory']

print()
print('-' * 80)
print("Model: {}".format(model))
print("Memory: {}".format(memory))
print('-' * 80)
print()
