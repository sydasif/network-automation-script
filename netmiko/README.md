Netmiko Introduction.

So in all the previous exercises, we achieved our goals through telnet
sessions. As we all know, telnet is not secure and may not be using in all
environments. So we should be known to do all the automation tasks using
SSH as well.
Netmiko, developed by Kirk Byers is an open-source multivendor library
that is used for SSH connections to network devices. Multi-vendor library
means, Netmiko supports network devices from different vendors such as
Cisco, Juniper , HP etc.
You may take a look at Netmiko documentation page at
https://github.com/ktbyers/netmiko. We can perform configurations on
network devices through SSH using the Netmiko.

Install the required packages and libraries, including Netmiko.

#apt-get upgrade

#apt-get install python3-pip

#pip install --upgrade pip

#pip install -U netmiko

In case the setup tools missing error you receive, then try the following
commands.
#apt-get upgrade
#apt-get install python3-venv
#apt-get install python3-dev
#pip install -U setuptools
#python3 -m pip install --upgrade pip
#python3 -m pip install setuptools
#python3 -m pip install netmiko
