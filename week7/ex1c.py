#!/usr/bin/env python
from __future__ import unicode_literals
import jinja2

vlan_vars = { 
            'vlans': {
            '501':'red501',
            '502':'red502',
            '503':'red503',
            '504':'red504',
            '505':'red505',
            '506':'red506',
            '507':'red507',
            '508':'red508',
            },
}

template_file = 'vlan_list.j2'

with open(template_file) as f:
    vlan_template = f.read()
 
template = jinja2.Template(vlan_template)
print(template.render(vlan_vars))
