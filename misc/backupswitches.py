#!/usr/bin/env python
from datetime import datetime
from netmiko import Netmiko

# Get current date and time for timestamping the backup
now = datetime.now()
dt_string = now.strftime("%d%m%Y_%H-%M-%S")

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

# List of devices to back up
devices = [SW1, R1]

for device in devices:
    net_connect = Netmiko(**device)
    show_version = net_connect.send_command("show version", use_textfsm=True)
    hostname = show_version[0]["hostname"]
    print(hostname + " ........ Connected.")
    show_run = net_connect.send_command("show run")
    # Create a backup file with the hostname and timestamp
    backup_file = hostname + "_" + dt_string + ".ios"
    file = open(backup_file, "w")
    file.write(show_run)
    file.close()
    print(hostname + " has been backed up." + "\n")

    # Disconnect from the device
    net_connect.disconnect()
