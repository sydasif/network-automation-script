from netmiko import ConnectHandler

IP_LIST = open('ip_list.txt')

for IP in IP_LIST:
    print ('\n==========> Connecting Device '+ IP.strip() + '\n' )
    device = {
    'ip': IP,
    'username': 'admin',
    'password': 'cisco',
    'device_type': 'cisco_ios',
    }

    net_connect = ConnectHandler(**device)

    print ('Initiating Running Backup\n')
    showver = net_connect.send_command("show version", use_textfsm=True)
    output = net_connect.send_command("show run", delay_factor =False)
    hostname = showver[0]['hostname']
    filename = hostname
    save_backup = open (filename, "w")
    save_backup.write(output)
    save_backup.close()
    print ('Backup saved')