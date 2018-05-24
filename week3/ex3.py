#! /usr/bin/env/python
from __future__ import print_function, unicode_literals

with open("show_lldp_neighbors_detail.txt") as f:
        lldp_file = f.read()

system_name, port_id = (None, None)

for line in lldp_file.splitlines():
    if 'System Name: ' in line:
        _, system_name = line.split('System Name: ')
    elif 'Port id: ' in line:
        port_id = line.split('Port id: ')
    if system_name and port_id:
        break

print()
print('System Name: {}'.format(system_name))
print('Port ID: {}'.format(port_id))
print()
