# Exercise 8: Backup the configuration of all switches
import getpass
import telnetlib
user = input("Enter your username :")
password = getpass.getpass()
f = open("switches.txt")
for IP in f:
    # IP.strip() is used to remove any white-spaces 
    IP = IP.strip()
    print("Taking backup of Switch " + (IP))
    tn = telnetlib.Telnet(IP)
    tn.read_until(b"Username: ")
    tn.write(user.encode("ascii") + b"\n")
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode("ascii") + b"\n")
    tn.write(b"enable\n")
    tn.write(b"cisco\n")
    # terminal length 0 command show configuration portion in one go
    tn.write(b"terminal length 0\n")
    tn.write(b"show run\n")
    tn.write(b"exit\n")
    #read all the output of the operations to a variable named as output
    output = tn.read_all()
    #opening a file SW+IP address with write permission
    config = open("SW" + IP, "w")
    #write the configurations to the config variable, for each switch
    config.write(output.decode("ascii"))
    config.write("\n")
    #close the files opened
    config.close
    print(tn.read_all().decode("ascii"))