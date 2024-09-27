from napalm import get_network_driver

driver = get_network_driver('ios')
iosv_l2 = driver('192.168.10.10', 'admin', 'cisco')
iosv_l2.open()

print('loading config file..... 192.168.10.10')
iosv_l2.load_merge_candidate(filename='config1.cfg')
iosv_l2.commit_config()
iosv_l2.close()
