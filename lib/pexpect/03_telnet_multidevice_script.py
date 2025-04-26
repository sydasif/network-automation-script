# Telnet to Device
import pexpect

# Define devices with their prompts and IP addresses
devices = {
    "CoreSW": {"ip": "192.168.100.20"},
    "SW1": {"ip": "192.168.100.21"},
}

# Credentials for login
username = "admin"
password = "cisco"

# Loop through each device in the devices dictionary
for device in devices.keys():
    ip_address = devices[device]["ip"]

    # Start a telnet session to the device
    child = pexpect.spawn("telnet " + ip_address)

    # Login process
    child.expect("Username: ")
    child.sendline(username)
    child.expect("Password: ")
    child.sendline(password)

    # Expect the user EXEC prompt
    child.expect(">")

    # Enter privileged mode
    child.sendline("enable")
    child.expect("Password: ")
    child.sendline(password)  # Optional if the user has privilege level 15
    child.expect("#")  # Expect the privileged EXEC prompt

    # Send command to show version
    child.sendline("show version | i V")
    child.expect("#")  # Wait for the prompt after the command

    # Retrieve and print the output
    show_output = child.before.decode("utf-8")
    print(f"Output from {device}:\n{show_output}")

    # Exit the session
    child.sendline("exit")
