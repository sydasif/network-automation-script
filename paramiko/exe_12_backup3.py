import datetime
import time

import paramiko

username = "admin"
password = "cisco"

tnow = datetime.datetime.now().replace(microsecond=0)
TFORMAT = f"{tnow:%d-%m-%Y_%H:%M:%S}"

list = open("device")
for sw in list:
    sw = sw.strip()
    print("\nConnecting to the device ------> " + sw)

    connection = paramiko.SSHClient()
    connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    connection.connect(
        sw,
        port=22,
        username=username,
        password=password,
        look_for_keys=False,
        allow_agent=False,
    )
    remote_connection = connection.invoke_shell()
    remote_connection.send(b"copy running-config tftp://192.168.100.100" + b"\n\n")
    remote_connection.send((sw + f"_{TFORMAT}" + "\n").encode())
    time.sleep(5)
    output = remote_connection.recv(65000)
    time.sleep(3)
    print()
    print("Device backup is complete =======>> " + sw + "\n")
    print("#" * 50)
    print()
    connection.close()
