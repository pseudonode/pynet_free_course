from __future__ import unicode_literals
from netmiko import Netmiko
from getpass import getpass

csr1000v  = { 'device_type':'cisco_ios',
              'username':'admin',
              'password': getpass(),
              'ip':'192.168.8.128' 
}

connection = Netmiko(**csr1000v)

print connection.find_prompt()
