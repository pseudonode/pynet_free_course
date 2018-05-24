#! /usr/bin/env/python
from __future__ import print_function, unicode_literals

with open("show_arp.txt") as f:
    arp_file = f.read()


found1, found2 = (False, False)

for line in arp_file.splitlines():
    if 'protocol' in line.lower():
        continue
    fields = line.split()
    ip_addr = fields[1]
    mac_addr = fields[3]
    if ip_addr == '10.220.88.1':
        print('Default gateway IP/MAC is {}/{}'.format(ip_addr, mac_addr))
        found1 = True
    elif ip_addr == '10.220.88.30':
        print('Arista3 IP/MAC is: {}/{}'.format(ip_addr, mac_addr))
        found2 = True
    
    if found1 and found2:
        print('found gateway and arista3 MAC/IP')
        break





