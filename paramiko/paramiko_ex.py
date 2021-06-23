import paramiko
import time
from getpass import getpass

ip = '192.168.100.20'
username = 'admin'
password = 'cisco'

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(ip,port=22,
                username=username,
                password=password,
                look_for_keys=False,
                allow_agent=False)

device = ssh.invoke_shell()
device.send(b'term length 0\n')
device.send(b'show run\n')
time.sleep(5)
output = device.recv(65000)
print (output.decode('ascii'))

ssh.close()