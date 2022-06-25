# Config_commands sample
from netmiko import ConnectHandler

R1 = {
    'ip':   '192.168.10.11',
    'username': 'admin',
    'password': 'cisco',
    'secret' : 'cisco',
    'device_type': 'cisco_ios',
}

net_connect = ConnectHandler(**R1)
net_connect.enable()  # device enable mode

#Execute configuration change commands 
#(will automatically enter into config mode)
config_commands = [ 'int lo0',
                    'ip add 1.1.1.1 255.255.255.255',
                    'no shut' ]
output = net_connect.send_config_set(config_commands)
print(output)