# Exe 02 
from napalm import get_network_driver

driver = get_network_driver('ios')
device = driver('192.168.10.11', 'admin', 'cisco')
device.open()

device.load_merge_candidate(config='username test')
print(device.compare_config())

device.close()
print('Done.')

