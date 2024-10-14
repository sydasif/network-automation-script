import time
from getpass import getpass

import paramiko

# Define the target device IP address
ip_addr = '172.16.10.11'
# Define the username for SSH login
username = 'admin'
# Securely get the password from the user
password = getpass('Enter SSH password: ')

# Create an SSH client instance
ssh = paramiko.SSHClient()
# Automatically add the remote host's SSH key (not recommended for production)
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# Connect to the remote device using the provided credentials
ssh.connect(
    ip_addr,
    port=22,
    username=username,
    password=password,
    look_for_keys=False,
    allow_agent=False
)

# Invoke an interactive shell session on the remote device
device = ssh.invoke_shell()
# Send command to set terminal length to 0 to avoid pagination
device.send(b'term length 0\n')
# Send command to display the running configuration
device.send(b'show run\n')

# Wait for the command to complete
time.sleep(10)
# Receive the output from the device
output = device.recv(65000)
# Print the received output after decoding it to ASCII
print(output.decode('ascii'))

# Close the SSH connection
ssh.close()
