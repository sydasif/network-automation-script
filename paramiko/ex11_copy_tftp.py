import paramiko
import datetime, time

username = 'admin'
password = 'cisco'

tnow = datetime.datetime.now().replace(microsecond=0)

list = open ('device')
for sw in list:
    sw = sw.strip()
    print ('\nConnecting to the device ------> ' + sw)
    
    SESSION = paramiko.SSHClient()
    SESSION.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    SESSION.connect(sw,port=22,
                    username=username,
                    password=password,
                    look_for_keys=False,
                    allow_agent=False)
    DEVICE_ACCESS = SESSION.invoke_shell()
    DEVICE_ACCESS.send('copy running-config tftp://192.168.100.100' + '\n\n\n')
    time.sleep(5)
    output = DEVICE_ACCESS.recv(65000)
    time.sleep(3)
    print ()
    print ('Device backup is complete =======>> ' + sw + '\n')
    print ('#' * 50)
    print ()
    SESSION.close()