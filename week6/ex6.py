from __future__ import unicode_literals
from netmiko import Netmiko
from getpass import getpass

password = getpass()

csr1v  = { 'device_type':'cisco_ios',
              'username':'admin',
              'password': password,
              'secret': password,
              'ip':'192.168.8.141' 
}
csr2v  = { 'device_type':'cisco_ios',
              'username':'admin',
              'password': password,
              'secret': password,
              'ip':'192.168.8.142' 
}
csr3v  = { 'device_type':'cisco_ios',
              'username':'admin',
              'password': password,
              'secret': password,
              'ip':'192.168.8.143' 
}

device_list = [csr1v,csr2v,csr3v]
cmd = 'show ip arp'

for device in device_list:
    connection = Netmiko(**device)
    print()
    print('Printing device hostname')
    print('-' * 80)
    print connection.find_prompt()
    print('-' * 80)
    print('Printing {}'.format(str(cmd)))
    print('-' * len(cmd) * 2)
    output = connection.send_command(cmd, use_textfsm=True)
    print(output)
    print('-' * 80)
    connection.disconnect()
