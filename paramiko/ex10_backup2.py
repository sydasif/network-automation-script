import paramiko
import time
import datetime

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
    
    DEVICE_ACCESS.send('terminal len 0\n')
    DEVICE_ACCESS.send('sh run\n')
    time.sleep(10)
    
    output = DEVICE_ACCESS.recv(65000)
    print (output.decode('ascii'))
    save_output = open('sw_' + sw + tnow, 'w')
    save_output.write(output.decode('ascii'))
    save_output.close()
    print ('Device backup successfull ========>>>' + sw)
    SESSION.close()