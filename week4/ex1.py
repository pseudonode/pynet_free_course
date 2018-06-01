#! /usr/bin/env/python
from __future__ import print_function, unicode_literals

# Create two dictionaries. One with device keys and the other with bgp keys
net_dict = { 'ip_addr':'192.168.1.1', 'vendor': 'cisco', 'username':'admin', 'password':'cisco'}
bgp_fields = { 'bgp_as':'65000', 'peer_as':'65001', 'peer_ip':'192.168.1.1' }

# Print IP address of device
print('The ipaddress of the device is: {}'.format(net_dict['ip_addr']))

# If Statement to update platform key
if net_dict['vendor'] == 'cisco':
    net_dict['platform'] = 'ios'
elif net_dict['vendor'] == 'juniper':
    net_dict['platform'] = 'ios'

# Print Platform
print()
print('The platform of the device is: {}'.format(net_dict['platform']))

# Using an update method append the bgp dict to the net dict
net_dict.update(bgp_fields)

# Print net_dict
print()
print(net_dict)

# For loop to print all the keys in net_dict
print()
for key in net_dict:
    print(key)
print()

# For loop to pring all the keys and values in net_dict
for k,v in net_dict.items():
    print(k,':',v)
