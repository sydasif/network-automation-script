#!/usr/bin/env python
from datetime import datetime

from netmiko import Netmiko

now = datetime.now()

dt_string = now.strftime("%d%m%Y_%H-%M-%S")

username = "networkchuck"
password = "Password123!"

Switch1 = {
    "host": "192.168.243.146",
    "username": username,
    "password": password,
    "device_type": "cisco_ios",
}

Switch2 = {
    "host": "192.168.243.149",
    "username": username,
    "password": password,
    "device_type": "cisco_ios",
}

Switch3 = {
    "host": "192.168.243.150",
    "username": username,
    "password": password,
    "device_type": "cisco_ios",
}

Switch4 = {
    "host": "192.168.243.148",
    "username": username,
    "password": password,
    "device_type": "cisco_ios",
}

Switch5 = {
    "host": "192.168.243.147",
    "username": username,
    "password": password,
    "device_type": "cisco_ios",
}

switches = [Switch1, Switch2, Switch3, Switch4, Switch5]

for sw in switches:
    net_connect = Netmiko(**sw)
    show_version = net_connect.send_command("show version", use_textfsm=True)
    show_run = net_connect.send_command("show run")
    hostname = show_version[0]['hostname']
    backup_file = hostname + "_" + dt_string + ".txt"
    file = open(backup_file, "w")
    file.write(show_run)
    file.close()
    print(hostname + " has been backed up" + "\n")
    net_connect.disconnect()
