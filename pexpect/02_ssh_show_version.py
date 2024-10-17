import pexpect

# Start an SSH session to the Cisco device
child = pexpect.spawn("ssh admin@192.168.100.20")
child.expect("Password: ")
child.sendline("cisco")
child.expect("SW1>")  # Expect the user mode prompt

# Enter privileged mode
child.sendline("enable")
child.expect("Password: ")
child.sendline("cisco")
child.expect("S1#")  # Expect the privileged mode prompt

# Send command to show version
child.sendline("show version | i V")
child.expect("S1#")  # Wait for the prompt after the command

# Convert the output to a string and print it
show_output = child.before.decode("utf-8")
print(show_output)

# Exit the session
child.sendline("exit")
