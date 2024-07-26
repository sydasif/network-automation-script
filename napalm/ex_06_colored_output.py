import json
from napalm import get_network_driver
# Add color to the output
from termcolor import colored

device_ip = ['192.168.10.10', '192.168.10.11']

for ip in device_ip:
    print()
    print(colored("Connecting..." + ip, "red"))
    print()
    driver = get_network_driver('ios')
    device = driver(ip, 'admin', 'cisco')
    device.open()

    output = device.get_facts()
    config = json.dumps(output, indent=4)
    print(config)

    device.close()
    print()
    print(colored('#' * 50, "green"))
    print()
