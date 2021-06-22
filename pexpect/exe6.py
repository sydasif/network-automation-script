import pexpect
import sys

child = pexpect.spawn('telnet 192.168.100.20')
child.expect('Username: ') 
child.sendline('admin')
child.expect('Password: ') 
child.sendline('cisco')
child.expect('CoreSW#')
# The following will turn on logging 
child.logfile = open('debug', 'wb') # output send to file
child.logfile = sys.stdout.buffer # output send to screen
child.sendline('show version | i V')
child.expect('CoreSW#')
print(child.before)
print(child.after) 
child.sendline('exit')
