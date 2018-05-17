#!/usr/bin/env python
from __future__ import print_function, unicode_literals
from pprint import pprint

# Open file with a python context manager
with open("show_arp.txt") as f:
    arp_file = f.readlines()

# Removing header line
arp_file = arp_file[1:]
pprint(arp_file)

# Grab the first three entries
arp_entries = arp_file[:3]

# Joining the 3 string inside the list
arp_entries = '\n'.join(arp_entries)

# Writing the content of arp_entries to a file
with open("arp_entries.txt", 'w') as f:
    f.write(arp_entries)
