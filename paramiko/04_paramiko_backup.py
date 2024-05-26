import paramiko
import time

# Define the backup file name
f = "switche.ios"

# Create an instance of the SSHClient class from Paramiko
connection = paramiko.SSHClient()
# Set the policy to automatically add the host key
connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Establish an SSH connection to the target device
connection.connect('192.168.100.20', username='admin1', password='cisco1', look_for_keys=False, allow_agent=False)

# Invoke an interactive shell session on the remote device
new_connection = connection.invoke_shell()

# Clear any initial buffer output
new_connection.recv(5000)

# Send command to the remote device
new_connection.send("sh ip int bri\n")
# Wait for the command to be finished on the remote device before retrieving the output
time.sleep(3)
# Retrieve the output from the buffer
output = new_connection.recv(5000)
# Print the received output after decoding it
print(output.decode())

# Open the backup file in binary write mode
with open('switch.ios', 'wb') as f:
    # Write the output to the backup file
    f.write(output)
# Ensure the remote connection is closed
new_connection.close()
