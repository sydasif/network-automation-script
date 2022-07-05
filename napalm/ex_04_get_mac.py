import json
from napalm import get_network_driver

driver = get_network_driver('ios')
device = driver('192.168.122.72', 'david', 'cisco')
device.open()

output = device.get_mac_address_table()
print (json.dumps(output, sort_keys=True, indent=4))

device.close()

