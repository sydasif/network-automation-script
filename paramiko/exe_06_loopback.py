import time

import paramiko

ip = "192.168.100.20"
username = "admin"
password = "cisco"

a = int(input("Enter first loopback in range : "))
b = int(input("Enter last loopback in range : ")) + 1

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

for N in range(a, b):
    remote_connection.send(b"int lo " + str(N).encode() + b"\n")
    remote_connection.send(
        b"ip address 1.1.1." + str(N).encode() + b" 255.255.255.255" + b"\n"
    )

time.sleep(3)
remote_connection.send(b"do term length 0\n")
remote_connection.send(b"do show ip int brief\n")
time.sleep(3)
output = remote_connection.recv(65000)
print(output.decode("ascii"))

connection.close()
