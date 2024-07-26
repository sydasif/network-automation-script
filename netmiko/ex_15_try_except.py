from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoTimeoutException
from paramiko.ssh_exception import SSHException
from netmiko.ssh_exception import AuthenticationException

IP_LIST = open('devices_list')
for IP in IP_LIST:
    print('\n' + IP.strip() + '  \n')
    device = {
        'ip': IP,
        'username': 'admin',
        'password': 'cisco',
        'device_type': 'cisco_ios',
    }
    print('Connecting to device' + IP)
    try:
        net_connect = ConnectHandler(**device)
    except NetMikoTimeoutException:
        print('Device not reachable.')
        continue
    except AuthenticationException:
        print('Authentication Failure.')
        continue
    except SSHException:
        print('Make sure SSH is enabled in device.')
        continue

    output = net_connect.send_config_from_file(config_file='config_file')
    print(output)
