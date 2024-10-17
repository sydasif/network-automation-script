#!/usr/bin/env python
from netmiko import Netmiko

username = "admin"
password = "cisco"

SW1 = {
    "host": "172.16.141.11",
    "username": username,
    "password": password,
    "device_type": "cisco_ios",
}

R1 = {
    "host": "172.16.141.12",
    "username": username,
    "password": password,
    "device_type": "cisco_ios",
}

devices = [SW1, R1]

# Get the target IP address from the user
client = input("What is the IP address that your client can't reach? ")

for x in devices:
    net_connect = Netmiko(**x)
    show_ver = net_connect.send_command("show version", use_textfsm=True)
    hostname = show_ver[0]["hostname"]
    # Ping the client IP and check the result
    ping = net_connect.send_command("ping " + client, read_timeout=30)
    if "....." in ping:
        print(hostname + " can't connect.")
    else:
        print(hostname + " -------> is good")
    net_connect.disconnect()
