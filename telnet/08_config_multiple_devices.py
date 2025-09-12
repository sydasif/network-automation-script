# Exercise 7: Loop for configuration of multiple devices.

import getpass
import telnetlib

user = input("Welcome, if authorized \nPlease enter your telnet Username: ")
password = getpass.getpass()

""" Create a for loop to configure multiple devices,
also note that we are converting the value on 'IP'
to string value using str() command.
1st digit is included & last digit will exclude """

for IP in range(101, 102):
    HOST = "192.168.121." + str(IP)
    print("configuration of 192.168.121." + str(IP))
    tn = telnetlib.Telnet(HOST)
    tn.read_until(b"Username: ")
    tn.write(user.encode("ascii") + b"\n")
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode("ascii") + b"\n")
    tn.write(b"enable\n")
    tn.write(b"cisco\n")
    tn.write(b"conf t\n")

    for v in range(2, 10):
        tn.write(b"vlan " + str(v).encode("ascii") + b"\n")
        tn.write(b"name VLAN_" + str(v).encode("ascii") + b"\n")
    tn.write(b"end\n")
    tn.write(b"show vlan br\n\n")
    tn.write(b"exit\n")
    print(tn.read_all().decode("ascii"))
