# Enable mode sample
from netmiko import ConnectHandler

# Create a dictionary for a particular device
S1 = {
    "device_type": "cisco_ios",
    "ip": "192.168.121.102",
    "username": "admin",
    "password": "admin",
    "secret": "cisco",
}

"""calling the ConnectHandler Library [**S1] means telling
python to consider the contents of the dictionary as key value pairs
instead of single elements."""

net_connect = ConnectHandler(**S1)
net_connect.enable()  # device enable mode

# Sending a command in to the switch --->
output = net_connect.send_command("show ip int br")
print(output)
