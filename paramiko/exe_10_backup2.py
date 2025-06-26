import datetime
import time

import paramiko

username = "admin"
password = "cisco"

tnow = datetime.datetime.now().replace(microsecond=0)
TFORMAT = f"{tnow:%d-%m-%Y_%H-%M-%S}"  # Added format for datetime object

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

    remote_connection.send(b"terminal len 0\n")
    remote_connection.send(b"sh run\n")
    time.sleep(10)

    output = remote_connection.recv(65000)
    print(output.decode("ascii"))
    save_output = open("sw_" + sw + TFORMAT, "w")  # Changed tnow to TFORMAT
    save_output.write(output.decode("ascii"))
    save_output.close()
    print("Device backup successfull ========>>>" + sw)
    connection.close()
