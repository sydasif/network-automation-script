# Napalm basic script

from napalm import get_network_driver

# Connect to device
driver = get_network_driver("ios")  # network driver is 'ios'
device = driver("192.168.10.11", "admin", "cisco")
device.open()

# Get facts from device
output = device.get_facts()
print(output)

device.close()
