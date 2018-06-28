from __future__ import print_function, unicode_literals
import yaml
from pprint import pprint

filename = 'interfaces_dict.yml'

with open(filename) as f:
    output = yaml.load(f)

print()
print(output)
print()
