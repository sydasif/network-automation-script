# send configuration from config1.txt file
# !/usr/bin/env python
from getpass import getpass

from netmiko import ConnectHandler

S1 = {
    "device_type": "cisco_ios",
    "host": "192.168.10.10",
    "username": "admin",
    "password": getpass(),
}

cfg_file = "config_file.cfg"
with ConnectHandler(**S1) as net_connect:
    output = net_connect.send_config_from_file(cfg_file)
    output += net_connect.save_config()

print()
print(output)
print()
