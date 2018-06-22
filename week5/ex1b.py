#! /usr/bin/env python
from __future__ import print_function, unicode_literals

def ssh_conn2(ip_addr, username, password, device_type='cisco_ios'):
    print('The IP address argument of the function is: {}'.format(ip_addr))
    print('The username argument of the function is: {}'.format(username))
    print('The password argiment of the function is: {}'.format(password))
    print('The device_type argiment of the function is: {}'.format(device_type))

ssh_dict = { 
        'ip_addr':'3.3.3.3',
        'username':'administrator',
        'password':'admin123',
        'device_type':'arista'
}

ssh_conn2('1.1.1.1', 'admin', 'password', 'junos')
print('-') * 80
ssh_conn2(ip_addr='2.2.2.2', password='password123', username='admin',)
print('-') * 80
ssh_conn2('2.2.2.2', password='password123', username='admin', device_type='junos')
print('-') * 80
ssh_conn2(**ssh_dict)


