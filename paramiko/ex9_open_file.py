import paramiko
import time

username = 'admin'
password = 'cisco'

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
    
    cmd = open ('config_file')
    for lines in cmd:
        time.sleep(2)
        DEVICE_ACCESS.send(str(line))
    
    time.sleep(3)
    output = DEVICE_ACCESS.recv(65000)
    print (output.decode('ascii'))

    SESSION.close()