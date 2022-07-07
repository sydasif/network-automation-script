import json
from napalm import get_network_driver
driver = get_network_driver('ios')
iosvl2 = driver('192.168.10.10', 'admin', 'cisco')
iosvl2.open()

print ('loding config file 192.168.10.10')
iosvl2.load_merge_candidate(filename='config1.cfg')

diffs = iosvl2.compare_config()
if len(diffs) > 0:
    print(diffs)
    iosvl2.commit_config()
else:
    print('No ACL changes required.')
    iosvl2.discard_config()

iosvl2.load_merge_candidate(filename='ospf1.cfg')

diffs = iosvl2.compare_config()
if len(diffs) > 0:
    print(diffs)
    iosvl2.commit_config()
else:
    print('No OSPF changes required.')
    iosvl2.discard_config()

iosvl2.close()
