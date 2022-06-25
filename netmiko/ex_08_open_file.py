# Exercise 3: Upload the configurations on all switches using SSH from file
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
devices = [CoreSW, SW1, SW2]

#Open the config_change.txt file that has all the commands that we need to execute and read lines
with open('config_file.txt') as f:
    lines = f.read().splitlines()
print(lines)

for device in devices:
    net_connect = ConnectHandler(**device)
    net_connect.enable()
    #Call each command line by line and send to the switch ---> 
    output = net_connect.send_config_set(lines)
    print(output)