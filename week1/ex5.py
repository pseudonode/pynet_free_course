#!/usr/bin/env python
from __future__ import print_function, unicode_literals

mac1 = "Internet  10.220.88.29           94   5254.abbe.5b7b  ARPA   FastEthernet4"
mac2 = "Internet  10.220.88.30            3   5254.ab71.e119  ARPA   FastEthernet4"
mac3 = "Internet  10.220.88.32          231   5254.abc7.26aa  ARPA   FastEthernet4"

fields = mac1.split()
mac1_ip = fields[1] 
mac1_arp = fields [3]

fields = mac2.split()
mac2_ip = fields[1] 
mac2_arp = fields [3]

fields = mac3.split()
mac3_ip = fields[1] 
mac3_arp = fields [3]

print()
print ('{:>20} {:>20}'.format('IP ADDR','MAC ADDRESS'))
print ('{:>20} {:>20}'.format('-' *20, '-'*20))
print ('{:>20} {:>20}'.format(mac1_ip, mac1_arp))
print ('{:>20} {:>20}'.format(mac2_ip, mac2_arp))
print ('{:>20} {:>20}'.format(mac3_ip, mac3_arp))
print()
