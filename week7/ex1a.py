#!/usr/bin/env python
from __future__ import unicode_literals
import jinja2

vlan_vars = {
            'vlan_number':'400',
            'vlan_name':'red400'
}

vlan_template = '''
vlan {{ vlan_id }}
   name {{ vlan_name }}
'''


template = jinja2.Template(vlan_template)
print(template.render(vlan_vars))
