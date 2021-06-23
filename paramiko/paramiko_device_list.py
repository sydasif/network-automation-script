import paramiko
import time

username = 'admin'
password = 'cisco'

list = ['192.168.100.' + str(n) for n in range(20,23)]
for sw in list:
    print ('\nConnecting to the device ------> ' + sw)
    
    SESSION = paramiko.SSHClient()
    SESSION.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    SESSION.connect(sw,port=22,
                    username=username,
                    password=password,
                    look_for_keys=False,
                    allow_agent=False)
    DEVICE_ACCESS = SESSION.invoke_shell()
    
    DEVICE_ACCESS.send(b'config t\n')
    
    for N in range (2,5):
        DEVICE_ACCESS.send('int lo ' +str(N) + '\n')
        DEVICE_ACCESS.send('ip address 1.1.1.' +str(N) + ' 255.255.255.255\n')  

    time.sleep(5)
    DEVICE_ACCESS.send(b'end\n')
    DEVICE_ACCESS.send(b'term length 0\n')
    DEVICE_ACCESS.send(b'show ip int brief\n')
    time.sleep(3)
    output = DEVICE_ACCESS.recv(65000)
    print (output.decode('ascii'))

    SESSION.close()