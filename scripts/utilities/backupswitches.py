#!/usr/bin/env python
from datetime import datetime
from netmiko import Netmiko

# Get current date and time for timestamping the backup
now = datetime.now()
dt_string = now.strftime("%d%m%Y_%H-%M-%S")

username = "admin"
password = "cisco"

SW_RTR = {
    "host": "192.168.99.1",
    "username": username,
    "password": password,
    "device_type": "cisco_ios",
}

SW2 = {
    "host": "192.168.99.2",
    "username": username,
    "password": password,
    "device_type": "cisco_ios",
}

SW3 = {
    "host": "192.168.99.3",
    "username": username,
    "password": password,
    "device_type": "cisco_ios",
}

R1 = {
    "host": "192.168.100.2",
    "username": username,
    "password": password,
    "device_type": "cisco_ios",
}

# List of devices to back up
devices = [SW2, R1, SW3, SW_RTR]

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
