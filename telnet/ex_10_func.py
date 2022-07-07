# Python telnetlib  
import getpass
import telnetlib

commands = ["terminal length 0",
            "sh ip int bri",
            "exit"
            ]

IP = '192.168.10.10'
user = input("Enter your username :")
password = getpass.getpass()


def send_cmd(command):
    '''send commands from list'''
    for cmd in command:
        tn.write(cmd.encode('ascii') + b"\n")
    result = tn.read_all().decode('ascii')
    return result
    
tn = telnetlib.Telnet(IP)
tn.read_until(b"Username: ")
tn.write(user.encode("ascii") + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode("ascii") + b"\n")

output = send_cmd(commands)
print(output)
