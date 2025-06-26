# Using for loop to configure device
import time

import paramiko

username = "admin"
password = "cisco"

for sw in range(20, 23):
    ip = "192.168.100." + str(sw)
    print("\n Connecting to the device ------> " + ip)

    connection = paramiko.SSHClient()
    connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    connection.connect(
        ip,
        port=22,
        username=username,
        password=password,
        look_for_keys=False,
        allow_agent=False,
    )
    remote_connection = connection.invoke_shell()

    remote_connection.send(b"config t\n")

    for N in range(2, 5):
        remote_connection.send(b"int lo " + str(N).encode() + b"\n")
        remote_connection.send(
            b"ip address 1.1.1." + str(N).encode() + b" 255.255.255.255\n"
        )

    time.sleep(5)
    remote_connection.send(b"do term length 0\n")
    remote_connection.send(b"do show ip int brief\n")
    time.sleep(3)
    output = remote_connection.recv(65000)
    print(output.decode("ascii"))

    connection.close()
