""" 
1. The expect() method in Pexpect process is an indicator for the 
returned string from the remote device.
2. The sendline() method indicates which words should be sent to the
remote device as the command.
"""
""" 
1. The expect() method in Pexpect process is an indicator for the 
returned string from the remote device.
2. The sendline() method indicates which words should be sent to the
remote device as the command.
"""
import pexpect

child = pexpect.spawn('telnet 192.168.10.10')
child.expect('Username: ')  # child.expect('[Uu]sername: ')
child.sendline('admin')
child.expect('Password: ')  # child.expect(['Password', 'password'])
child.sendline('cisco')
child.expect('S1>')
child.sendline('enable')
child.expect('Password: ')
child.sendline('cisco')
child.expect('S1#')
child.sendline('show version | i V')
child.expect('S1#')
# convert it to a string
show_output = child.before.decode('utf-8')
# print out the command 
print(show_output)
child.sendline('exit')

# Read the Pexpect docs at
# https://pexpect.readthedocs.io/en/stable/index.html
