#! /usr/bin/env/python
from __future__ import print_function, unicode_literals
from pprint import pprint

with open("show_ip_bgp_summ.txt") as f:
    bgp_output = f.readlines()
    bgp_output_first = bgp_output[0]
    bgp_output_last = bgp_output[-1]


# pprint(bgp_output)
# pprint(bgp_output_first)
# pprint(bgp_output_last)

bgp_asn = (bgp_output_first.split()[-1])
bgp_neighbor = (bgp_output_last.split()[0])

print('The Local AS Number is: {}'.format(bgp_asn))
print('The Remote BGP Neighbor is: {}'.format(bgp_neighbor))

