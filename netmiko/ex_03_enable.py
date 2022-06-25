#Enable mode on devices

from netmiko import ConnectHandler
from getpass import getpass

password = getpass()
secret = getpass("Enter secret: ")

R2 = {
    "device_type": "cisco_ios",
    "host": "192.168.80.9",
    "username": "admin",
    #"password": "cisco",
    #"secret": "secret",
}

net_connect = ConnectHandler(**R2)

# Call 'enable()' method to elevate privileges

net_connect.enable()
print(net_connect.find_prompt())
net_connect.disconnect()