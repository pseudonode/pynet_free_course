#!/usr/bin/env python
from __future__ import unicode_literals
import jinja2
import yaml


template_file = 'interfaces.j2'
filename = 'interfaces_dict.yml'

with open(filename) as f:
    output = yaml.load(f)

with open(template_file) as f:
    interface_template= f.read()

template = jinja2.Template(interface_template)
print(template.render(output))
