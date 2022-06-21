# Python telnetlib  
import getpass
import telnetlib

# my function to add commands in one list
def send_cmd(cmds):
    for cmd in cmds:
        tn.write(cmd.encode('ascii') + b"\n")
    output = tn.read_all().decode('ascii')
    print(output)
    
my_cmds = ["terminal length 0",
        "sh version",
        "sh ip int bri",
        "exit"]

IP = '192.168.10.10'

user = input("Enter your username :")
password = getpass.getpass()

tn = telnetlib.Telnet(IP)
tn.read_until(b"Username: ")
tn.write(user.encode("ascii") + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode("ascii") + b"\n")

send_cmd(my_cmds)
