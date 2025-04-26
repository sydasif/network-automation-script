# Enable mode on devices

from getpass import getpass

from netmiko import ConnectHandler

password = getpass()
secret = getpass("Enter secret: ")

R1 = {
    "device_type": "cisco_ios",
    "host": "192.168.10.11",
    "username": "admin",
    "password": password,
    "secret": secret,
}

net_connect = ConnectHandler(**R1)

# Call 'enable()' method to elevate privileges

net_connect.enable()
print(net_connect.find_prompt())
net_connect.disconnect()
