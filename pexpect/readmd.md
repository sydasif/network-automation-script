# Automating Network Device Interaction with Pexpect

In network automation, managing devices like switches and routers efficiently is essential. One powerful tool for automating interactions with these devices is `pexpect`. This Python module allows you to spawn child applications, control them, and respond to expected patterns in their output, making it ideal for automating SSH and Telnet sessions. In this blog post, we will explore how to use `pexpect` for both Telnet and SSH connections to Cisco devices.

## What is Pexpect?

`Pexpect` is a Python module that facilitates automating interactions with command-line applications. It works by spawning child processes, sending commands, and waiting for specific outputs. This is particularly useful for automating tasks in environments where manual input is typically required, such as when logging into network devices.

## Setting Up Pexpect

Before we dive into examples, you need to install `pexpect`. You can install it via pip:

```bash
pip install pexpect
```

## Example 1: Automating Telnet to a Cisco Device

Let's start with a simple example of connecting to a Cisco device via Telnet, executing a command, and logging the output. Here’s the code:

```python
import sys
import pexpect

# Start Telnet session to the device
child = pexpect.spawn("telnet 192.168.100.20")

# Login process
child.expect("Username: ")  # Wait for the username prompt
child.sendline("admin")      # Send the username
child.expect("Password: ")   # Wait for the password prompt
child.sendline("cisco")      # Send the password

# Expect the device prompt after login
child.expect("CoreSW#")

# Open log file to write the output
with open("debug", "wb") as log_file:
    # Function to log output to both console and file
    def log_output(data):
        log_file.write(data)              # Write output to log file
        sys.stdout.buffer.write(data)     # Write output to console

    # Command to execute on the device
    command = "show version | i V"
    child.sendline(command)  # Send the command to the device
    
    # Expect the prompt after the command execution
    child.expect("CoreSW#")
    
    # Get command output
    output = child.before  # Store the output received before the prompt
    log_output(output)      # Log output to file and console

# Exit the Telnet session
child.sendline("exit")  # Send exit command to close the session
```

### Breakdown of the Code

1. **Starting the Telnet Session**: The script begins by spawning a Telnet session to the specified IP address.
2. **Logging In**: It waits for the username and password prompts, sending the credentials automatically.
3. **Executing Commands**: After logging in, the script sends the command `show version | i V`, captures the output, and logs it to both a file and the console.
4. **Graceful Exit**: Finally, the script sends the exit command to close the session properly.

## Example 2: Automating SSH to a Cisco Device

Now, let’s look at how to perform similar automation using SSH. Here’s a sample code for SSH connection:

```python
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
    child.sendline("exit")  # Send exit command to close the session
```

### Breakdown of the Code

1. **Device Definitions**: The script defines a list of devices to connect to with their IP addresses.
2. **SSH Connection**: For each device, it initiates an SSH session using the defined username.
3. **Authentication**: It handles the password prompt and checks for the appropriate user and privileged mode prompts.
4. **Command Execution**: The script sends a command to show the version information, captures the output, and prints it.
5. **Session Closure**: Finally, it exits the session gracefully.

## Conclusion

Using `pexpect` allows for efficient automation of network device management through command-line interactions. With the provided examples, you can quickly get started with automating tasks on Cisco devices using both Telnet and SSH.

These scripts can be extended to include more complex command sequences, error handling, and logging features, making them a valuable addition to your network automation toolkit.
