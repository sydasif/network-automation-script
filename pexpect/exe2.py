# Basic code sample SSH

import pexpect

child = pexpect.spawn('ssh admin@192.168.100.20')
child.expect('Password: ')
child.sendline('cisco')
child.expect('CoreSW>')
child.sendline('enable')
child.expect('Password: ')
child.sendline('cisco')
child.expect('CoreSW#')
child.sendline('show version | i V')
child.expect('CoreSW#')
print(child.before)
child.sendline('exit')
