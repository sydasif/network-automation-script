import paramiko
import time

# Create an instance of the SSHClient class from Paramiko
connection = paramiko.SSHClient()
# Set the policy to automatically add the host key
connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# Establish an SSH connection to the target device
connection.connect(
    '172.16.10.12', 
    username='admin', 
    password='cisco', 
    look_for_keys=False, 
    allow_agent=False
    )

# Invoke an interactive shell session on the remote device
new_connection = connection.invoke_shell()

# Send the command to the remote device
new_connection.send("sh ip int bri\n")
# Wait for the command to be finished on the remote device before retrieving the output
time.sleep(3)

# Retrieve the output from the buffer
output = new_connection.recv(5000)
# Print the received output after decoding it
print(output.decode())

# Close the remote connection
new_connection.close()
