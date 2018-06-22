#! /usr/bin/env python
from __future__ import print_function, unicode_literals

from random import randint

def netgen(network='10.10.10.', mask='/24'):
    #print(' The assigned IP address is: {}{}{}'.format(network, octet, mask))
    ip = network + str(randint(1,254)) + mask
    print('The assigned IP address is: {}'.format(ip))

print('-') * 50
netgen()
print('-') * 50
netgen('25.25.25.')
print('-') * 50
netgen(network='20.20.20.')
