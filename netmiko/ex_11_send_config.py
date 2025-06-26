# Exercise 1: Create VLANs and Assign IP using SSH
from getpass import getpass

from netmiko import ConnectHandler

# user input
password = getpass()
secret = getpass("Enter secret: ")

# Create a dictionary for a particular device
CoreSW = {
    "device_type": "cisco_ios",
    "ip": "192.168.100.20",
    "username": "admin",
    "password": password,
    "secret": secret,
}

"""calling the ConnectHandler Library [**iosv_l2] means telling
python to consider the contents of the dictionary as key value pairs
instead of single elements."""

net_connect = ConnectHandler(**CoreSW)
net_connect.enable()

# Sending a command in to the switch --->
output = net_connect.send_command("show ip int br")
print(output)

# Create a list that includes all the commands that we need to execute
config_commands = ["int vlan 5", "ip add 5.5.5.1 255.255.255.0"]
output = net_connect.send_config_set(config_commands)
print(output)
