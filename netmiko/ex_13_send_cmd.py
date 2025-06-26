# Execute configuration commands and save configuration

from netmiko import ConnectHandler

device = {
    "device_type": "cisco_ios",
    "host": "192.168.100.20",
    "username": "admin",
    "password": "cisco",
    "port": 22,  # optional, defaults to 22
}

# Establish an SSH connection to the device

net_connect = ConnectHandler(**device)
config_commands = ["int lo0", "ip add 172.16.10.1 255.255.255.0"]
output = net_connect.send_config_set(config_commands)
net_connect = net_connect.send_command("wr")
print(output)
print(net_connect)
