from __future__ import print_function, unicode_literals
import yaml


filename = 'interfaces_list.yml'

with open(filename) as f:
    output = yaml.load(f)

print()
print(output)
print()
