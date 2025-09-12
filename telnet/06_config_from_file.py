# Exercise 5: Create multiple VLANs on multiple switches

"""For this exercise, first we need to create a file containing the
IP addresses of all the switches.Later in the program, we will call this file
and the code will check IP one by one and perform the operation.
Create a file named as switches.txt. Write all the three IP address of the
switches in the test file, one by one. Then save and exit."""

import getpass
import telnetlib

# If the credentials are different for each switches, put the code inside
# the for loop
user = input("Enter your username :")
password = getpass.getpass()

#  Open the file
f = open("telnet/switch.cfg")

# For loop will get the IP from the file one by one and execute the code
for IP in f:
    IP = IP.strip()
    print("Configuring Switch " + IP)
    tn = telnetlib.Telnet(IP)
    tn.read_until(b"Username: ")
    tn.write(user.encode("ascii") + b"\n")
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode("ascii") + b"\n")
    tn.write(b"enable\n")
    tn.write(b"cisco\n")
    tn.write(b"conf t\n")

    for n in range(2, 10):
        tn.write(b"vlan " + str(n).encode("ascii") + b"\n")
        tn.write(b"name VLAN_" + str(n).encode("ascii") + b"\n")
    tn.write(b"end\n")
    tn.write(b"show vlan br\n\n")
    tn.write(b"exit\n")
    print(tn.read_all().decode("ascii"))
