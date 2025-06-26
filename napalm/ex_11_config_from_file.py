from napalm import get_network_driver

driver = get_network_driver("ios")
ios_vl2 = driver("192.168.10.10", "admin", "cisco")
ios_vl2.open()

print("loading config file 192.168.10.10")
ios_vl2.load_merge_candidate(filename="config1.cfg")

diffs = ios_vl2.compare_config()
if len(diffs) > 0:
    print(diffs)
    ios_vl2.commit_config()
else:
    print("No ACL changes required.")
    ios_vl2.discard_config()

ios_vl2.load_merge_candidate(filename="ospf1.cfg")

diffs = ios_vl2.compare_config()
if len(diffs) > 0:
    print(diffs)
    ios_vl2.commit_config()
else:
    print("No OSPF changes required.")
    ios_vl2.discard_config()

ios_vl2.close()
