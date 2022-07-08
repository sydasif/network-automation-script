from napalm import get_network_driver
from termcolor import colored
from getpass import getpass

# Add different vendor list here 
cisco = ['192.168.10.10', '192.168.10.11']

username = input("Please Enter Your Username: ")
password = getpass("Please Enter Your Password: ")

def connect(ip, os_ver):
    for ip in cisco:
        driver = get_network_driver(os_ver)
        device = driver(hostname=ip, username=username, password=password)
        device.open()

        print()
        print (colored('GET OS VERSION......\n', 'red'))
        os_version = device.get_facts()["os_version"]
        
        if "vios_l2" in os_version:
            print(colored(f"{ip} os version is:\n\n" + os_version, 'magenta'))
        else:
            print(colored(f"{ip} os version is:\n\n" + os_version, 'blue'))


# calling function
connect(cisco, "ios")
