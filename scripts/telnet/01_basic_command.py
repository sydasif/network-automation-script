# This is a basic telnet script
from telnetlib import Telnet

cmd = input("Enter the Command: ")  # Command
ip = input("Enter IP Address: ")  # IP Address of device
tn = Telnet(ip)

tn.write(b"admin\n")
tn.write(b"cisco\n")
tn.write(cmd.encode("ascii") + b"\n")
tn.write(b"exit\n")

print(tn.read_all().decode("ascii"))
