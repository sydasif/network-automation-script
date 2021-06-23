import paramiko, time

f = "switche.txt"
# The first four lines create an instance of the SSHClient class from Paramiko
connection = paramiko.SSHClient()
# Sets the policy that the client should use regarding keys
connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# The next few lines invoke a new interactive shell from the connection
connection.connect('192.168.100.20', username='admin1', password='cisco1', look_for_keys=False, allow_agent=False)
new_connection = connection.invoke_shell()
new_connection.recv(5000)

# Send command to the remote device
new_connection.send("sh ip int bri\n")
# Wait for the command to be finished on the remote device before retrieving the output
time.sleep(3)
output = new_connection.recv(5000)
print(output.decode())
new_connection.close()

with open('switch.txt', 'wb') as f:
    f.write(output)
new_connection.close()