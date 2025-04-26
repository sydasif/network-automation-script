import time

import paramiko

username = 'admin'
password = 'cisco'

list = ['192.168.100.' + str(n) for n in range(20, 23)]
for sw in list:
    print('\nConnecting to the device ------> ' + sw)

    connection = paramiko.SSHClient()
    connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    connection.connect(sw, port=22,
                       username=username,
                       password=password,
                       look_for_keys=False,
                       allow_agent=False)
    remote_connection = connection.invoke_shell()

    remote_connection.send(b'config t\n')

    for N in range(2, 5):
        remote_connection.send('int lo ' + str(N) + '\n')
        remote_connection.send(
            'ip address 1.1.1.' + str(N) + ' 255.255.255.255\n')

    time.sleep(5)
    remote_connection.send(b'end\n')
    remote_connection.send(b'term length 0\n')
    remote_connection.send(b'show ip int brief\n')
    time.sleep(3)
    output = remote_connection.recv(65000)
    print(output.decode('ascii'))

    connection.close()
