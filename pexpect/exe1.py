""" 
1. The expect() method in Pexpect process is an indicator for the 
returned string from the remote device.
2. The sendline() method indicates which words should be sent to the
remote device as the command.
"""
import pexpect

child = pexpect.spawn('telnet 192.168.100.20')
child.expect('Username: ')  # child.expect('[Uu]sername: ')
child.sendline('admin')
child.expect('Password: ')  # child.expect(['Password', 'password'])
child.sendline('cisco')
child.expect('CoreSW>')
child.sendline('enable')
child.expect('Password: ')
child.sendline('cisco')
child.expect('CoreSW#')
child.sendline('show version | i V')
child.expect('CoreSW#')
# print out the sendline('show version | i V') before expect('CoreSW#') line
print(child.before)
# print out the expect('CoreSW#') line which is 'CoreSW#' 
print(child.after) 
child.sendline('exit')

# Read the Pexpect docs at 
# https://pexpect.readthedocs.io/en/stable/index.html