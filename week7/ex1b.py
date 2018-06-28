#!/usr/bin/env python
from __future__ import unicode_literals
import jinja2

ipsec_vars = {'encryption':'aes', 'dh_group':'5', 'isakmp_enable':True}

cfg_template = '''

{%- if isakmp_enable %}}
crypto isakmp policy 10
 encr {{ encryption }}
 authentication pre-share
 group {{ dh_group }}
crypto isakmp key my_key address 1.1.1.1 no-xauth
crypto isakmp keepalive 10 periodic
{%- endif %}

'''

template = jinja2.Template(cfg_template)
print(template.render(ipsec_vars))
