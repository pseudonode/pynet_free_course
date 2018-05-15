#!/usr/bin/env python
from __future__ import print_function, unicode_literals


try:
    ip_addr = raw_input('Please insert a valid IP address:')
    print ('The IP address you have introduced is:', ip_addr)
except NameError:
    ip_addr = input('Please insert a valid IP address:')
    print ('The IP address you have introduced is:', ip_addr)

ip_addr_split = ip_addr.split('.')

print (ip_addr_split)

print ()
print ('{:^15}{:^15}{:^15}{:^15}'.format('Octet1', 'Octet2', 'Octet3', 'Octet4'))
print ('-' *60)
print (' {:^15}{:^15}{:^15}{:^15}'.format(*ip_addr_split))
print (' {:^15}{:^15}{:^15}{:^15}'.format(bin(int(ip_addr_split[0])), bin(int(ip_addr_split[1])),                                                               bin(int(ip_addr_split[2])),bin(int(ip_addr_split[3]))))
print (' {:^15}{:^15}{:^15}{:^15}'.format(hex(int(ip_addr_split[0])), hex(int(ip_addr_split[1])),                                                               hex(int(ip_addr_split[2])),hex(int(ip_addr_split[3]))))
print ('-' *60)
print ()
