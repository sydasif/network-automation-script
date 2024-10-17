import pexpect

# Start a telnet session to the Cisco device
child = pexpect.spawn("telnet 172.16.141.11")
child.expect("Username: ")
child.sendline("admin")
child.expect("Password: ")
child.sendline("cisco")
child.expect("#")  # Wait for the device prompt

# Send the command to show the version
child.sendline("show version | i V")
child.expect("#")  # Wait for the prompt after the command

# Convert the output to a string and print it
show_output = child.before.decode("utf-8")
print(show_output)

# Exit the session
child.sendline("exit")
