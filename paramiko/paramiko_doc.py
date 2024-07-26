#!/usr/bin/python

import paramiko
import time

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname="172.16.10.11", username='admin', password='cisco',
            look_for_keys=False, allow_agent=False)
shell = ssh.invoke_shell()
shell.send("terminal length 0\n")
shell.send("show ip int b\n")
time.sleep(2)
print(shell.recv(5000).decode())
ssh.close()
