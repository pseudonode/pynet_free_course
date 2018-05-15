#!/usr/bin/env python
from __future__ import print_function, unicode_literals

address =  '2001:1000:2000::1/64'
ADDRESS =  '2001:1000:2000::1/64'
IPV6_ADDRESS = '2001:1000:2000::2/64'

print("")
print('Is variable 1 equal to variable2: {}'.format(address == ADDRESS))
print('Is variable 1 not equal to variable3:i {}'.format(address == IPV6_ADDRESS))
print("")
