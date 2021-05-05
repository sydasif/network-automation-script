# Exercise 2: Create Multiple VLANs on all switches using SSH
from netmiko import ConnectHandler
switch1 = {
 'device_type': 'cisco_ios',
 'ip': '192.168.100.20',
 'username': 'admin',
 'password': 'cisco',
 'secret' : 'cisco',
}
switch2 = {
 'device_type': 'cisco_ios',
 'ip': '192.168.100.21',
 'username': 'admin',
 'password': 'cisco',
 'secret' : 'cisco',
}
switch3 = {
 'device_type': 'cisco_ios',
 'ip': '192.168.100.22',
 'username': 'admin',
 'password': 'cisco',
 'secret' : 'cisco',
}
switches = [switch1, switch2, switch3]
for devices in switches:
 net_connect = ConnectHandler(**devices)
 net_connect.enable()
 for n in range (10, 15):
    print("Creating VLAN " + str(n))
    config_commands = ['vlan ' + str(n), 'name DevOps_VLAN ' + str(n)]
    output = net_connect.send_config_set(config_commands)
    print(output)