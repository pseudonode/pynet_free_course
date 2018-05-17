#!/usr/bin/env python

ip_list = ['10.10.10.10','20.20.20.20','30.30.30.30','40.40.40.40','50.50.50.50']
#print (ip_list)

# Using the append method to add items to the end of a list
ip_list.append('60.60.60.60')

# Using the extend method to add items to the end of a list
ip_list.extend(['70.70.70.70','80.80.80.80'])

# Using list concatenation to add two ip addresses to the end of the list
ip_list2 = ['90.90.90.90','100.100.100.100']
ip_list  = ip_list + ip_list2

# Printing the full list, the first item on the list and the last item on the list
print('')
print(ip_list)
print(ip_list[0])
print(ip_list[-1])
print('')

# Using .pop to remove the first ip address in the list and thelast ip address in the list
ip_list.pop(0)
ip_list.pop(-1)

# Using the update method to enter a new ip address in the list
ip_list.insert(0,'2.2.2.2')
print('')
print(ip_list[0])
print('')

print(ip_list)


