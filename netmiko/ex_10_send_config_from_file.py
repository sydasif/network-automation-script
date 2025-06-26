# demonstrates, how to use the method send_config_from_file
# in netmiko for device configuration.
from netmiko import ConnectHandler

IP_LIST = open("devices_list")
for IP in IP_LIST:
    device = {
        "ip": IP,
        "username": "admin",
        "password": "cisco",
        "device_type": "cisco_ios",
        "global_delay_factor": False,
    }

    print("Connecting to device" + IP)
    net_connect = ConnectHandler(**device)

    output = net_connect.send_config_from_file(config_file="config_file")
    print(output)

    print("\n Saving the Configuration" + "\n")
    output = net_connect.send_command("wr", delay_factor=False)
    print(output)
