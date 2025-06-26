import json

from napalm import get_network_driver

driver = get_network_driver("ios")
device = driver("192.168.122.72", "david", "cisco")
device.open()

output = device.get_bgp_neighbors()
print(json.dumps(output, indent=4))

device.close()
