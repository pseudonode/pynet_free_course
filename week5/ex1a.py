#! /usr/bin/env python
from __future__ import print_function, unicode_literals

def ssh_conn(ip_addr, username, password):
    print('The IP address argument of the function is: {}'.format(ip_addr))
    print('The username argument of the function is: {}'.format(username))
    print('The password argiment of the function is: {}'.format(password))

ssh_conn('1.1.1.1', 'admin', 'password')
print('-') * 80
ssh_conn(ip_addr='2.2.2.2', password='password123', username='admin')
print('-') * 80
ssh_conn('2.2.2.2', password='password123', username='admin')
