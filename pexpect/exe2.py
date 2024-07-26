# Basic code sample SSH

import pexpect

child = pexpect.spawn('ssh admin@192.168.100.20')
child.expect('Password: ')
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
