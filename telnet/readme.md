# Automating Network Management with Python: Telnet Scripts for Network Engineers

In today's fast-paced network environments, automation is key to efficiency. Python, with its powerful libraries, allows network engineers to automate repetitive tasks. This blog post showcases several Telnet scripts that demonstrate how to manage network devices effectively. We will cover scripts for backing up configurations, creating VLANs, and executing commands on multiple switches.

## Prerequisites

Before you dive into the scripts, ensure you have Python installed along with the `telnetlib` and `getpass` modules. These libraries are part of Python’s standard library, so you won't need to install anything extra.

## Exercise 1: Simple Command Execution

The first exercise demonstrates how to execute a command on a network device via Telnet. This script prompts for a username, password, and command, establishing a connection to the specified device.

```python
import getpass
import telnetlib

HOST = "172.16.141.11"
user = input("Enter your Username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)
tn.read_until(b"Username: ")
tn.write(user.encode("ascii") + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode("ascii") + b"\n")

tn.write(b"sh ip int brief\n")
tn.write(b"exit\n")

print(tn.read_all().decode("ascii"))
```

### Key Features:

- Prompts for user credentials.
- Executes the command `show ip interface brief`.

## Exercise 2: Backup Running Configuration

This script allows you to retrieve the running configuration from a device. The script requests user credentials and saves the device's configuration to a file.

```python
import getpass
import telnetlib

IP = input("Enter the IP Address: ")
user = input("Enter your username: ")
password = getpass.getpass()
tn = telnetlib.Telnet(IP)
tn.read_until(b"Username: ")
tn.write(user.encode("ascii") + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode("ascii") + b"\n")
tn.write(b"enable\n")
tn.write(b"cisco\n")
tn.write(b"terminal length 0\n")
tn.write(b"show run\n")
tn.write(b"exit\n")
print(tn.read_all().decode("ascii"))
```

### Key Features:

- Uses `enable` mode for privileged commands.
- Retrieves the running configuration and displays it.

## Exercise 3: Create Multiple VLANs on Multiple Switches

In this exercise, we automate the creation of multiple VLANs across several switches. A file containing the IP addresses of the switches is required.

```python
import getpass
import telnetlib

user = input("Enter your username: ")
password = getpass.getpass()

f = open("switch.cfg")

for IP in f:
    IP = IP.strip()
    print("Configuring Switch " + IP)
    tn = telnetlib.Telnet(IP)
    tn.read_until(b"Username: ")
    tn.write(user.encode("ascii") + b"\n")
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode("ascii") + b"\n")
    tn.write(b"enable\n")
    tn.write(b"cisco\n")
    tn.write(b"conf t\n")

    for n in range(2, 10):
        tn.write(b"vlan " + str(n).encode("ascii") + b"\n")
        tn.write(b"name VLAN_" + str(n).encode("ascii") + b"\n")
    tn.write(b"end\n")
    tn.write(b"show vlan br\n\n")
    tn.write(b"exit\n")
    print(tn.read_all().decode("ascii"))
```

### Key Features:

- Reads a list of switch IPs from a file.
- Configures VLANs 2 through 9 on each switch.

## Exercise 4: Backup Configuration of All Switches

This script backs up the configuration of multiple switches by reading their IPs from a file and saving the output to individual files.

```python
import getpass
import telnetlib

user = input("Enter your username: ")
password = getpass.getpass()
f = open("device_ip.cfg")
for IP in f:
    IP = IP.strip()
    print("Taking backup of device " + IP)
    tn = telnetlib.Telnet(IP)
    tn.read_until(b"Username: ")
    tn.write(user.encode("ascii") + b"\n")
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode("ascii") + b"\n")
    tn.write(b"terminal length 0\n")
    tn.write(b"show run\n")
    tn.write(b"exit\n")
    
    output = tn.read_all()
    config = open("device_" + IP, "w")
    config.write(output.decode("ascii"))
    config.write("\n")
    config.close()
    print(tn.read_all().decode("ascii"))
```

### Key Features:

- Reads device IPs from a file.
- Saves each switch's running configuration in separate files.

## Conclusion

These Python scripts provide a solid foundation for automating network management tasks via Telnet. By leveraging these tools, network engineers can streamline their workflows, reduce human error, and save valuable time. Remember to modify and adapt the scripts according to your network environment and security practices.
