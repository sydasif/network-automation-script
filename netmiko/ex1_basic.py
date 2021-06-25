#Basic netmiko sample
from netmiko import ConnectHandler

#Create a dictionary representing the device
CoreSW = {
    'ip':   '192.168.100.20',
    'username': 'admin',
    'password': 'cisco',
    'device_type': 'cisco_ios',
}

#Establish an SSH connection to the device by passing in the device dictionary
net_connect = ConnectHandler(**CoreSW)

#Execute show commands
output = net_connect.send_command('show ip int brief')
print(output)