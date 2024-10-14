import time

import paramiko

# Create an instance of the SSHClient class from Paramiko
connection = paramiko.SSHClient()
# Set the policy to automatically add the host key
connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Establish an SSH connection to the target device
connection.connect('172.16.10.12', username='admin', password='cisco',
                   look_for_keys=False, allow_agent=False)

# Invoke an interactive shell session on the remote device
new_connection = connection.invoke_shell()

# Clear any initial buffer output
new_connection.recv(5000)

# Send command to the remote device
new_connection.send("ter len 0\n")
new_connection.send("sh run\n")
# Wait for the command to be finished on the remote device before retrieving the output
time.sleep(5)
# Retrieve the output from the buffer
output = new_connection.recv(65000)
# Print the received output after decoding it
print(output.decode())
# Ensure the remote connection is closed
new_connection.close()

# Open the backup file in binary write mode
with open('device_backup.ios', 'wb') as f:
    # Write the output to the backup file
    f.write(output)
