#! /usr/bin/env/python
from __future__ import print_function, unicode_literals

houston_ips = [
    '10.10.10.1',
    '10.10.20.1',
    '10.10.30.1',
    '10.10.40.1',
    '10.10.50.1',
    '10.10.60.1',
    '10.10.70.1',
    '10.10.80.1',
    '10.10.10.1',
    '10.10.20.1',
    '10.10.70.1',
]

atlanta_ips = [
    '10.10.10.1',
    '10.10.20.1',
    '10.10.30.1',
    '10.10.140.1',
    '10.10.150.1',
    '10.10.160.1',
    '10.10.170.1',
    '10.10.180.1',
]

chicago_ips = [
    '10.10.10.1',
    '10.10.20.1',
    '10.10.140.1',
    '10.10.150.1',
    '10.10.210.1',
    '10.10.220.1',
    '10.10.230.1',
    '10.10.240.1',
]

houston_ips = set(houston_ips)
atlanta_ips = set(atlanta_ips)
chicago_ips = set(chicago_ips)

print()
print("-" * 80)
print('The unique IP addresses in the Houston DC are: {}'.format(houston_ips))
print()
print("-" * 80)
print('The unique IP addresses in the Atlanta DC are: {}'.format(atlanta_ips))
print()
print("-" * 80)
print('The unique IP addresses in the Chicago DC are: {}'.format(chicago_ips))

print()
print("-" * 80)
print('Duplicate IPs between Houston and Atlanta are: {}'.format(houston_ips & atlanta_ips))

print()
print("-" * 80)
print('Duplicate IPs between all three DCs are: {}'.format(houston_ips & atlanta_ips & chicago_ips))

print()
print("-" * 80)
print('Unique IPs in Chicago are: {}'.format(chicago_ips.difference(houston_ips).difference(atlanta_ips)))
