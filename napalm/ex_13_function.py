import os

from dotenv import load_dotenv
from termcolor import colored

from napalm import get_network_driver

os_list = None  # Add different vendor list here
ip_list = ["192.168.10.10", "192.168.10.11"]

load_dotenv()

username = os.getenv("USER_ID")
password = os.getenv("PASSWORD")


def connect(os_ver):
    for ip in ip_list:
        driver = get_network_driver(os_ver)
        device = driver(hostname=ip, username=username, password=password)
        device.open()

        print()
        print(colored("GET OS VERSION......\n", "red"))
        os_version = device.get_facts()["os_version"]

        if "vios_l2" in os_version:
            print(colored(f"{ip} os version is:\n\n" + os_version, "magenta"))
        else:
            print(colored(f"{ip} os version is:\n\n" + os_version, "blue"))


connect("ios")

# See details about python-dotenv: https://sydasif.github.io/python/python-dot-env/
