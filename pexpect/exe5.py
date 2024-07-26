#!/usr/bin/env python
# for SSH create user with privilege level 15 
import getpass
from pexpect import pxssh

devices = {'S1': {'prompt': 'S1#', 'ip': '192.168.10.10'},
           'R1': {'prompt': 'R1#', 'ip': '192.168.10.11'}}

commands = ['term length 0', 'show run']

username = input('Username: ')
password = getpass.getpass('Password: ')

# Starts the loop for devices
for device in devices.keys():
    outputFileName = device + '_output.cfg'
    device_prompt = devices[device]['prompt']

    child = pxssh.pxssh()
    child.login(devices[device]['ip'], username.strip(), password.strip(), auto_prompt_reset=False)
    print("Backup Device Config....." + device)
    # Starts the loop for commands and write to output
    with open(outputFileName, 'wb') as f:
        for command in commands:
            child.sendline(command)
            child.expect(device_prompt)
            f.write(child.before)

    child.logout()
print("Done")
