# Python telnet 
import getpass
import telnetlib

commands = ["show ip int bri", "exit"]

IP = '192.168.138.9'
user = input("Enter your username :")
password = getpass.getpass()
tn = telnetlib.Telnet(IP)
tn.read_until(b"Username: ")
tn.write(user.encode("ascii") + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode("ascii") + b"\n")

def send_cmd(commands):
    for command in commands:
        tn.write(command.encode('ascii') + b"\n")
    output = tn.read_all().decode('ascii')
    print(output)


send_cmd(commands)
