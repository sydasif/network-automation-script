# Exercise Additional task

''' 1. Create a loopback interface and assign an IP, then get the running config.
    2. Create a new user.
    3. Delete the previously created VLAN 20.'''

import getpass
import telnetlib

IP = "192.168.100.20"
user = input("Enter your username :")
password = getpass.getpass()
tn = telnetlib.Telnet(IP)
tn.read_until(b"Username: ")
tn.write(user.encode("ascii") + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode("ascii") + b"\n")
    tn.write(b"enable\n")
    tn.write(b"cisco\n")
    tn.write(b"conf t\n")
    tn.write(b"int loopback 0\n")
    tn.write(b"ip add 172.16.10.1 255.255.255.255\n\n")
    tn.write(b"no vlan 20\n")
    tn.write(b"username admin1 password cisco1\n")
    tn.write(b"end\n")
    tn.write(b"exit\n")
    print(tn.read_all().decode("ascii"))
