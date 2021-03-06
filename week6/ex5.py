from __future__ import unicode_literals
from netmiko import Netmiko
from getpass import getpass

password = getpass()

csr1000v  = { 'device_type':'cisco_ios',
              'username':'admin',
              'password': password,
              'secret': password,
              'ip':'192.168.8.136' 
}

connection = Netmiko(**csr1000v)

print connection.find_prompt()

cmd = 'show ip arp'
print()
print('Sending command to device')
print('-' * 80)
output = connection.send_command(cmd, use_textfsm=True)
print(output)
connection.disconnect()
