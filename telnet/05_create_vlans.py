# Exercise 4: Create multiple VLANs using python for loop
import getpass
import telnetlib

IP = input("Enter IP Address: ")
user = input("Enter your username: ")
password = getpass.getpass()
tn = telnetlib.Telnet(IP)
tn.read_until(b"Username: ")
tn.write(user.encode("ascii") + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode("ascii") + b"\n")
# tn.write(b"enable\n")
# tn.write(b"cisco\n")
tn.write(b"conf t\n")

""" Create a for loop to create multiple VLANs,
also note that we are converting the value on 'n'
to string value using str() command """
for n in range(2, 10):  # with number 2 and keep increment until 10, but 10 is
    # not included
    tn.write(b"vlan " + str(n).encode("ascii") + b"\n")
    tn.write(b"name VLAN_" + str(n).encode("ascii") + b"\n")

tn.write(b"end\n")
tn.write(b"show vlan br\n\n")
tn.write(b"exit\n")
print(tn.read_all().decode("ascii"))
