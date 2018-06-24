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

cmd = ['logging on','logging buffered']
print()
print('Sending logging config to device')
print('-' * 80)
output = connection.send_config_set(cmd)
#print(output)
print('Saving Configuration to NVRAM')
print('-' * 80)
connection.save_config()
output = connection.send_config_from_file('logging_config.txt')
print(output)
show_run = connection.send_command('show run | include logging')
print(show_run)
connection.disconnect()
