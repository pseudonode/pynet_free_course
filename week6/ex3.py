from __future__ import unicode_literals
from netmiko import Netmiko
from getpass import getpass

password = getpass()

csr1000v  = { 'device_type':'cisco_ios',
              'username':'admin',
              'password': password,
              'secret': password,
              'ip':'192.168.8.128' 
}

connection = Netmiko(**csr1000v)

print connection.find_prompt()

cmd = 'reload in 10'
output = connection.send_command_timing(cmd)
if 'confirm' in output:
    output += connection.send_command_timing('\n')
connection.disconnect()
print(output) 
