import json

from napalm import get_network_driver

driver = get_network_driver('ios')
device = driver('192.168.10.10', 'admin', 'cisco')
device.open()

output = device.get_interfaces()
print(json.dumps(output, indent=4))

device.close()
print('Done.....')
