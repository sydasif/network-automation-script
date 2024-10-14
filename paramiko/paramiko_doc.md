# [Paramiko Module](https://www.paramiko.org/)

-----------------------------------------------

The Paramiko module is the most widely used library for SSH in Python. It is
written and developed in Python, though some core functions, like cryptography,
depend on the C language.

## Module Installation

To install the latest Paramiko module from PyPI, open your Windows command
prompt or Linux shell and execute the following command. This will also
download additional dependency packages such as `cryptography`, `ipaddress`,
and `six`:

```bash
pip3 install paramiko
```

You can verify the installation by entering the Python shell and importing the
Paramiko module. Python should import it without any errors:

```bash
(.venv) user@hostname:~/network-automation-script$ python3
Python 3.10.12 (main, Nov 20 2023, 15:14:05) [GCC 11.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import paramiko
>>>
```

## SSH to the Network Device

First, import the Paramiko module into your Python script. Then, create an SSH
client by inheriting from `SSHClient()`. Configure Paramiko to automatically
add any unknown host keys and trust the connection between you and the server.
Use the `connect` function and provide the remote host credentials:

```python
#!/usr/bin/python

import paramiko
import time

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(
    hostname="172.16.10.12", 
    username='admin', 
    password='cisco', 
    look_for_keys=False,
    allow_agent=False
)
shell = ssh.invoke_shell()
```

> `AutoAddPolicy()` is one of the policies that can be used inside
> the `set_missing_host_key_policy()` function. It's preferred and acceptable in
> a lab environment. However, use a more restrictive policy in a production
> environment, such as `WarningPolicy()` or `RejectPolicy()`.

The `invoke_shell()` function will start the interactive shell session towards
your SSH server. You can provide additional parameters to it, such as the
terminal type, width, and height.

**Paramiko Connect Parameters:**

- `look_for_keys`: By default, this is `True`, which forces Paramiko to use
  key-pair authentication where the user uses both private and public keys to
  authenticate against the network device. In this case, it is set to `False`
  because password authentication is used.
- `allow_agent`: This parameter allows connection to a local SSH agent OS. This
  is necessary when working with keys. Since authentication is performed using
  a login/password, it is disabled.

The final step is to send a series of commands such as `show ip int bri` to the
device terminal and get the output back to the Python shell:

```python
shell.send("terminal length 0\n")
shell.send("show ip int b\n")
time.sleep(2)
print(shell.recv(5000).decode())
ssh.close()
```

**Script Output Example:**

```bash
(.venv) user@hostname:~/network-automation-script$ paramiko_doc.py

IOSv - Cisco Systems Confidential -

Supplemental End User License Restrictions

This IOSv software is provided AS-IS without warranty of any kind. Under no circumstances may this software be used separate from the Cisco Modeling Labs Software that this software was provided with, or deployed or used as part of a production environment.

By using the software, you agree to abide by the terms and conditions of the Cisco End User License Agreement at http://www.cisco.com/go/eula. Unauthorized use or distribution of this software is expressly prohibited.

core1#terminal length 0
core1#show ip int b
Interface              IP-Address      OK? Method Status                Protocol
GigabitEthernet0/0     unassigned      YES unset  up                    up      
GigabitEthernet0/1     unassigned      YES unset  down                  down    
GigabitEthernet0/2     unassigned      YES unset  down                  down    
GigabitEthernet0/3     unassigned      YES unset  down                  down    
GigabitEthernet1/0     unassigned      YES unset  down                  down    
GigabitEthernet1/1     unassigned      YES unset  down                  down    
GigabitEthernet1/2     unassigned      YES unset  down                  down    
GigabitEthernet1/3     unassigned      YES unset  down                  down    
GigabitEthernet2/0     unassigned      YES unset  down                  down    
GigabitEthernet2/1     unassigned      YES unset  down                  down    
GigabitEthernet2/2     unassigned      YES unset  down                  down    
GigabitEthernet2/3     unassigned      YES unset  down                  down    
GigabitEthernet3/0     unassigned      YES unset  down                  down    
GigabitEthernet3/1     unassigned      YES unset  down                  down    
GigabitEthernet3/2     unassigned      YES unset  down                  down    
GigabitEthernet3/3     unassigned      YES unset  down                  down    
Vlan1                  172.16.10.11    YES NVRAM  up                    up      
core1#
```

> It is preferable to use `time.sleep()` when executing commands that will take
> a long time on a remote device. This forces Python to wait until the device
> generates output and sends it back to Python. Otherwise, Python may return
> blank output to the user.
