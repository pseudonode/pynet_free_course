#! /usr/bin/env/python
from __future__ import print_function, unicode_literals
import re

with open('show_version.txt') as f:
    show_version = f.read()

#print(show_version)

os_version = re.search(r'Version (.+),', show_version).group(1)
serial_number = re.search(r'Processor board ID (.+)', show_version).group(1)
config_register = re.search(r'Configuration register is (.+)', show_version).group(1)
print('OS Version', os_version)
print('Serial Number:', serial_number)
print('Config Register:', config_register)
