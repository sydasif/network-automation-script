# Exercise 4: Apply different configuration to different switches
from netmiko import ConnectHandler
CoreSW = {
 'device_type': 'cisco_ios',
 'ip': '192.168.100.20',
 'username': 'admin',
 'password': 'cisco',
 'secret' : 'cisco'
}
SW1 = {
 'device_type': 'cisco_ios',
 'ip': '192.168.100.21',
 'username': 'admin',
 'password': 'cisco',
 'secret' : 'cisco'
}
SW2 = {
 'device_type': 'cisco_ios',
 'ip': '192.168.100.22',
 'username': 'admin',
 'password': 'cisco',
 'secret' : 'cisco'
}
switches = [CoreSW, SW1, SW2]
with open('network.txt') as f:
    lines = f.read().splitlines()
print(lines)
for devices in switches:
    net_connect = ConnectHandler(**devices)
    net_connect.enable()
    output = net_connect.send_config_set(lines)
    print(output)

with open('SW2.txt') as f:
    lines = f.read().splitlines()
print(lines)
net_connect = ConnectHandler(**SW2)
net_connect.enable()
output = net_connect.send_config_set(lines)
print(output)