# SSH to Devices
import pexpect

# Define devices with their IP addresses
devices = {
    "CoreSW": {"ip": "192.168.100.20"},
    "SW1": {"ip": "192.168.100.21"},
}

username = "admin"
password = "cisco"

# Loop through each device
for device in devices.keys():
    ip_address = devices[device]["ip"]

    # Start an SSH session to the device
    child = pexpect.spawn("ssh " + username + "@" + ip_address)

    # Login process
    child.expect("Password: ")
    child.sendline(password)

    # Expect the user EXEC prompt
    child.expect(">")  # User mode prompt

    # Enter privileged mode
    child.sendline("enable")
    child.expect("Password: ")
    child.sendline(password)  # Optional if the user has privilege level 15
    child.expect("#")  # Privileged mode prompt

    # Send command to show version
    child.sendline("show version | i V")
    child.expect("#")  # Wait for the prompt after the command

    # Retrieve and print the output
    show_output = child.before.decode("utf-8")
    print(f"Output from {device}:\n{show_output}")

    # Exit the session
    child.sendline("exit")
