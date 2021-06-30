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
    
    connection = paramiko.SSHClient()
    connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    connection.connect(sw, port=22,
                       username=username,
                       password=password,
                       look_for_keys=False,
                       allow_agent=False)
    remote_connection = connection.invoke_shell()
    
    remote_connection.send('terminal len 0\n')
    remote_connection.send('sh run\n')
    time.sleep(10)
    
    output = remote_connection.recv(65000)
    print (output.decode('ascii'))
    save_output = open('sw_' + sw + tnow, 'w')
    save_output.write(output.decode('ascii'))
    save_output.close()
    print ('Device backup successfull ========>>>' + sw)
    connection.close()