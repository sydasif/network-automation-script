# Useing for loop to configure device 
import paramiko
import time

username = 'admin'
password = 'cisco'

for sw in range(20,23):
    ip = "192.168.100." + str(sw)
    print ('\n Connecting to the device ------> ' + ip)
    
    SESSION = paramiko.SSHClient()
    SESSION.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    SESSION.connect(ip,port=22,
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
    DEVICE_ACCESS.send(b'do term length 0\n')
    DEVICE_ACCESS.send(b'do show ip int brief\n')
    time.sleep(3)
    output = DEVICE_ACCESS.recv(65000)
    print (output.decode('ascii'))

    SESSION.close()