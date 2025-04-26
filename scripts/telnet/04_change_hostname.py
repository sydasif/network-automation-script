# Exercise 1: Python code to Change the Hostname using telnet.
import getpass
import telnetlib

# Declare a variable for storing the IP address
IP = "192.168.100.20"

# Declare a variable for storing username
user = input("Enter your username :")

# Use getpass module which we imported, to get the password from the user
password = getpass.getpass()

# Pass the IP variable value in to the telnetlib
tn = telnetlib.Telnet(IP)

# Now the code will read each output from the cisco switch
tn.read_until(b"Username: ")
tn.write(user.encode("ascii") + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode("ascii") + b"\n")

""" Now specify the commands in the right sequence.enable password,
then change to configuration terminal and change the hostname, 
finally save the configuration and exit """

tn.write(b"enable\n")
tn.write(b"cisco\n")
tn.write(b"conf t\n")
tn.write(b"hostname CoreSW\n")
tn.write(b"end\n")
tn.write(b"write memory\n")
tn.write(b"exit\n")

print(tn.read_all().decode("ascii"))
