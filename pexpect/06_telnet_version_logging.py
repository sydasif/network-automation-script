import sys
import pexpect

# Start Telnet session to the device
child = pexpect.spawn("telnet 192.168.100.20")

# Login process
child.expect("Username: ")  # Wait for the username prompt
child.sendline("admin")  # Send the username
child.expect("Password: ")  # Wait for the password prompt
child.sendline("cisco")  # Send the password

# Expect the device prompt after login
child.expect("CoreSW#")

# Open log file to write the output
with open("debug", "wb") as log_file:
    # Function to log output to both console and file
    def log_output(data):
        log_file.write(data)  # Write output to log file
        sys.stdout.buffer.write(data)  # Write output to console

    # Command to execute on the device
    command = "show version | i V"
    child.sendline(command)  # Send the command to the device

    # Expect the prompt after the command execution
    child.expect("CoreSW#")

    # Get command output
    output = child.before  # Store the output received before the prompt
    log_output(output)  # Log output to file and console

# Exit the Telnet session
child.sendline("exit")  # Send exit command to close the session
