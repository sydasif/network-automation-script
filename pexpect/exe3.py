# Telnet to Device
import pexpect

devices = {'CoreSW': {'prompt': 'CoreSW#', 'ip': '192.168.100.20', 'en': 'CoreSW>'}, 
           'SW1': {'prompt': 'SW1#', 'ip': '192.168.100.21', 'en': 'SW1>'}}
username = 'admin'
password = 'cisco'

for device in devices.keys(): 
    device_prompt = devices[device]['prompt']
    device_en = devices[device]['en']
    child = pexpect.spawn('telnet ' + devices[device]['ip'])
    child.expect('Username: ')
    child.sendline(username)
    child.expect('Password: ')
    child.sendline(password)
    # If user privilage level is 15, enable and enable password are not required
    child.expect(device_en)
    child.sendline('enable')
    child.expect('Password: ')
    child.sendline(password)
    child.expect(device_prompt)
    child.sendline('show version | i V')
    child.expect(device_prompt)
    # convert it to a string
    show_output = child.before.decode('utf-8')
    # print out the command 
    print(show_output) 
    child.sendline('exit')
