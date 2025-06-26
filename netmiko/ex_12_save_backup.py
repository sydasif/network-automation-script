# How to take Cisco IOS device configuration backup from the terminal
# using netmiko and save the file with timestamp

import datetime

from netmiko import ConnectHandler

now = datetime.datetime.now().replace(microsecond=0)
cr_date = f"{now:%d-%m-%Y}"
IP_LIST = open("devices_list")
for IP in IP_LIST:
    print("\n==========> Connecting Device " + IP.strip() + "\n")
    device = {
        "ip": IP,
        "username": "admin",
        "password": "cisco",
        "device_type": "cisco_ios",
    }

    net_connect = ConnectHandler(**device)

    print("Initiating Running Backup\n")
    showver = net_connect.send_command("show version", use_textfsm=True)
    showrun = net_connect.send_command("show run", delay_factor=False)
    hostname = showver[0]["hostname"]
    backupfilename = hostname + "_" + cr_date
    file = open(backupfilename, "w")
    file.write(showrun)
    file.close()
    print("Backup Finished\n")
