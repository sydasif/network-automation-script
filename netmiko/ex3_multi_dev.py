#SSH to multiple Cisco devices, using multiple device dictionaries
#in Netmiko and lists. It uses for loop to get each device dictionary

from netmiko import ConnectHandler

CoreSW = {
    'ip':   '192.168.100.20',
    'username': 'admin',
    'password': 'cisco',
    'device_type': 'cisco_ios'
}

SW1 = {
    'ip':   '192.168.100.21',
    'username': 'admin',
    'password': 'cisco',
    'device_type': 'cisco_ios'
}

DEVICE_LIST = [CoreSW, SW1]
for DEVICE in DEVICE_LIST:
    print ('Connecting to the Device ' + DEVICE['ip'])
    net_connect = ConnectHandler(**DEVICE)

    config_commands = [ 'int lo0',
                        'ip add 1.1.1.1 255.255.255.0',
                        'no shut' ]
    output = net_connect.send_config_set(config_commands)
    print(output)