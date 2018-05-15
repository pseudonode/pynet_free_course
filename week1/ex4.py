#!/usr/bin/env python
from __future__ import print_function, unicode_literals

show_version = "*0        CISCO881-SEC-K9       FTX0000038X    "
show_version = show_version.strip()

show_version_list = show_version.split()
model = show_version_list[1]
serial_number = show_version_list[2]


print()
vendor_cisco = 'cisco' in model.lower()
print('Is Cisco contained in the model string: {}'.format(vendor_cisco))

model_881 = '881' in model.lower()
print('Is 881 contained in the model string: {}'.format(model_881))


print ('The Serial Number of the device is: {}'.format(serial_number))
print ('The model of the device is: {}'.format(model))
print()
