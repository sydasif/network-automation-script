import json
from napalm import get_network_driver

driver = get_network_driver('ios')
iosvl2 = driver('192.168.10.10', 'admin', 'cisco')
iosvl2.open()

print('loading config file..... 192.168.10.10')
iosvl2.load_merge_candidate(filename='config1.cfg')
iosvl2.commit_config()
iosvl2.close()
