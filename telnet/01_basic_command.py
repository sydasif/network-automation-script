# This is a basic telnet script
from telnetlib import Telnet

ip = "192.168.121.101"
cmd = input("Enter the Command: ")  # Command
tn = Telnet(ip)

tn.write(b"admin\n")
tn.write(b"admin\n")
tn.write(cmd.encode("ascii") + b"\n")
tn.write(b"exit\n")

print(tn.read_all().decode("ascii"))
