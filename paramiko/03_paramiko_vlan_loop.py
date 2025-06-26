import time
from getpass import getpass

import paramiko

# Define connection details
ip_address = "172.16.10.11"
username = "admin"
password = getpass("Enter SSH password: ")

# Create an instance of the SSHClient class from Paramiko
ssh_client = paramiko.SSHClient()
# Set the policy to automatically add the host key
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# Establish an SSH connection to the target device
ssh_client.connect(
    hostname=ip_address,
    username=username,
    password=password,
    look_for_keys=False,
    allow_agent=False,
)

print("Successful connection to", ip_address)
# Invoke an interactive shell session on the remote device
remote_connection = ssh_client.invoke_shell()

# Enter configuration mode
remote_connection.send(b"configure terminal\n")

# Loop to create VLANs 2 through 20
for n in range(2, 10):
    print("Creating VLAN " + str(n))
    remote_connection.send(b"vlan " + str(n).encode() + b"\n")
    remote_connection.send(b"name Python_VLAN_" + str(n).encode() + b"\n")
    time.sleep(1)  # Ensure the device processes each command

# Exit configuration mode
remote_connection.send(b"end\n")

# Wait for the commands to be processed
time.sleep(5)
# Retrieve the output from the buffer
output = remote_connection.recv(65535)
# Print the received output after decoding it
print(output.decode())

# Close the SSH connection
ssh_client.close()
