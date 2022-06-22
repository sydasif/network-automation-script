import paramiko
import time

username = 'admin'
password = 'cisco'

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
    
    cmd = open ('config_file')
    for lines in cmd:
        time.sleep(2)
        remote_connection.send(str(lines))
    
    time.sleep(3)
    output = remote_connection.recv(65000)
    print (output.decode('ascii'))

    connection.close()