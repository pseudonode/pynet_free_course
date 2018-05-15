#!/usr/bin/env python
from __future__ import print_function, unicode_literals

mac1 = "Internet  10.220.88.29           94   5254.abbe.5b7b  ARPA   FastEthernet4"
mac2 = "Internet  10.220.88.30            3   5254.ab71.e119  ARPA   FastEthernet4"
mac3 = "Internet  10.220.88.32          231   5254.abc7.26aa  ARPA   FastEthernet4"

mac1_list = mac1.split()
print (mac1_list)
mac2_list = mac2.split()
print (mac2_list)
mac3_list = mac3.split()
print (mac3_list)

print ('{:>20} {:>20}'.format('IP ADDR','MAC ADDRESS'))


