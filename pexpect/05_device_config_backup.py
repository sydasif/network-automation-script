#!/usr/bin/env python
# For SSH create user with privilege level 15
import getpass
from pexpect import pxssh

# Define devices and their details
devices = {
    "S1": {"ip": "172.16.141.11"},
    "R1": {"ip": "172.16.141.12"},
}

# Commands to execute on each device
commands = ["term length 0", "show run"]

# Get credentials from the user
username = input("Username: ")
password = getpass.getpass("Password: ")

# Loop through devices and backup configurations
for device in devices.keys():
    outputFileName = device + "_output.cfg"
    device_ip = devices[device]["ip"]

    # Initialize the SSH session
    child = pxssh.pxssh()
    # Manually specify the prompt to expect from the device (e.g., "#")
    child.PROMPT = r"[#>]"

    # Attempt to login with the specified prompt pattern
    child.login(
        device_ip,
        username.strip(),
        password.strip(),
        auto_prompt_reset=False,  # Do not attempt to auto-set the prompt
    )
    print(f"Backing up configuration for device: {device}")

    # Open the output file for writing
    with open(outputFileName, "wb") as f:
        # Loop through each command and write the output
        for command in commands:
            child.sendline(command)
            # Wait for the specified prompt to appear again
            child.expect(child.PROMPT)
            f.write(child.before)  # Write the command output to the file

    # Logout from the device
    child.logout()

print("Backup process complete.")
