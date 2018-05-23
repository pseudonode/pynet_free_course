#! /usr/bin/env/python
from __future__ import print_function, unicode_literals
from pprint import pprint

# Initializ a blank list for posterior appending of VLAN_NUMBER and VLAN_NAME
vlan_list = []

# Open file with a context manager to read its content
with open('show_vlan.txt') as f:
    show_vlan = f.read()

# For loop with splitlines so that every line inside show_vlan can be parsed
for line in show_vlan.splitlines():
    # if the keywords below are in a line or if line starts w 3 spaces then continue
    if 'VLAN' in line or '----' in line or line.startswith('  '):
        continue
    # split every line into a list and every string to an item inside list
    fields = line.split()
    # allocate index0 to vlan_id and index1 to vlan_name
    vlan_id = fields[0]
    vlan_name = fields[1]
    # append vlan_id and vlan_name to a tuple inside vlan_list previously initialized
    vlan_list.append((vlan_id, vlan_name))

print()
pprint(vlan_list)
