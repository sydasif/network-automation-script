from napalm import get_network_driver

driver = get_network_driver("ios")
iosv_l2 = driver("192.168.10.10", "admin", "cisco")
iosv_l2.open()

print("loading config from file......192.168.10.10")
iosv_l2.load_merge_candidate(filename="config1.cfg")

diffs = iosv_l2.compare_config()
if len(diffs) > 0:
    print(diffs)
    iosv_l2.commit_config()
else:
    print("No changes required.")
    iosv_l2.discard_config()

iosv_l2.close()
