### ==============================================================
# Controlling the flow of a Python program
### ==============================================================

# First, define the two network parts
lan = "10.2.10."
wan = "10.20.1."
# user input
device_type = input("What network type [lan/wan]? ")
host_part = input("What's the host part? ")
# if statement
if device_type == "lan":
    ip = lan + host_part
    print(f"Your lan device ip: {ip}")
elif device_type == "wan":
    ip = wan + host_part
    print(f"Your wan device ip: {ip}")
else:
    print(f"Sorry, I don't know how to handle the {device_type}")
