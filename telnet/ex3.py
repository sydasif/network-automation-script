# Exercise 3: Create and assign IP to a VLAN interface
import getpass
import telnetlib
IP = input("Enter the IP Address :")
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
tn.write(b"vlan 20\n")
tn.write(b"name VLAN_20\n")
tn.write(b"int vlan 20\n")
tn.write(b"ip add 10.20.30.40 255.255.255.0\n")
tn.write(b"no sh\n")
tn.write(b"end\n")
tn.write(b"show ip int br\n")
tn.write(b"exit\n")
print(tn.read_all().decode('ascii'))