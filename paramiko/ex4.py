import paramiko
import time

host = '192.168.100.22' #Remote device we want to interact with
user = 'admin' #SSH user
passw = 'cisco' #SSH password
enable_pass = 'cisco' #Privileged-exec mode password

#Creating a function to just take a command and send it to the device.
#This reduces the amount of time, need to add in the "\n", sleep and clear the buffer.
#There is a default sleep time of 1 second, but can always change it for something 
#that may need to sit for a bit longer.
def issue_command(channel, command, delay=1):
    connection = channel
    command_str = command + "\n"
    connection.send(command_str)
    time.sleep(delay)
    output = connection.recv(99999)
    return output

#Sets up the ssh session and log in as "admin" with password "cisco" to host '192.168.100.22' . 
#Also added "look_for_keys=False" and "allow_agent=False". 
try:
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connection(host, username=user, password=passw, look_for_keys=False, allow_agent=False)
    connection = ssh.invoke_shell()
except:
    print ("Login to {} failed".format(host))
    connection = False


if connection:
    issue_command(connection, "enable")
    issue_command(connection, enable_pass)
    issue_command(connection, "terminal length 0")
    output = issue_command(connection, "show vlan brief", 2)
    ssh.close()
    print (output.decode())
else:
    print ("Sorry, there is no connection to the host {}".format(host))