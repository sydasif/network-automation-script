import napalm
import json


def main():
    driver_ios = napalm.get_network_driver("ios")
    device_list = [["192.168.10.10", "ios", "switch"], ["192.168.10.11", "ios", "router"]]

    network_devices = []
    for device in device_list:
        network_devices.append(
            driver_ios(
                hostname=device[0],
                username="admin",
                password="cisco"
            )
        )

    for device in network_devices:
        print("#" * 40)
        print("Connecting to {} ...".format(device.hostname))
        device.open()

        print("Getting device facts")
        device_facts = device.get_facts()

        device.close()
        print("#" * 40)
        print(json.dumps(device_facts, indent=4))


if __name__ == '__main__':
    main()
