# Basic config_commands sample
from netmiko import ConnectHandler
from getpass import getpass

password = getpass()

CoreSW = {
    'ip':   '192.168.100.20',
    'username': 'admin',
    'password': 'cisco',
    'device_type': 'cisco_ios',
}

net_connect = ConnectHandler(**CoreSW)

#Execute configuration change commands 
#(will automatically enter into config mode)
config_commands = [ 'int lo0',
                    'ip add 1.1.1.1 255.255.255.255',
                    'no shut' ]
output = net_connect.send_config_set(config_commands)
print(output)