import json

from termcolor import colored

from napalm import get_network_driver

driver = get_network_driver("ios")
device = driver(hostname="192.168.10.11", username="admin", password="cisco")
device.open()

print(colored("#########\nGET FACTS\n#########", "red"))
facts = device.get_facts()
print(colored(json.dumps(facts, sort_keys=True, indent=4), "magenta"))

device.close()
