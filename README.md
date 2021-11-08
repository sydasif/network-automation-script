# Network Automation

--------------------

What is Network Automation?

Network automation is the process of automating the configuration, management and operations of a computer network. The tasks that were normally done by the network or system administrator can be automated using a number of tools and technologies.

Scripting languages are widely used by Network and System administrators for automating the tasks. This saves time, effort and thereby reducing human errors as well. Among the automation tools, Python and Ansible are the most popular ones. With Software Defined Networking (SDN) in picture, knowing any of these programming languages is vital for the future of administering the network and systems. See [How to Install Python 3?](https://www.python.org/downloads/) and [*Intallation of python and NotePad++*](02_Install_Python3_on_WIN10_Notepad.pdf)

## Python for Network Engineer

### Free Ebooks

**Natasha Samoilenko** [*Python for Network Engineer*](https://pyneng.readthedocs.io/en/latest/)

**Lisa Tagliaferri** [*How to Code in Python*](https://www.digitalocean.com/community/books/digitalocean-ebook-how-to-code-in-python)

### Setting up the Lab

#### Software’s and images used

Item                     | Software
------------------------ | --------
Lab simulation software  | GNS3
Switches | Cisco L2 virtual
Network Automation PC | Docker in GNS3

#### Topology

In this lab topology, I have used the following components in GNS3.

1. A Network Automation Appliance. We will be coding python in this PC.
2. A Layer2 Ethernet Switch.
3. A NAT cloud, this is used to provide internet connectivity and also acts as a DHCP server.
4. Three Cisco Virtual IOS switches.
5. [Device Configuration](/configuration)
6. [Ubuntu Server Configuration](https://github.com/sydasif/linux-lab)

![lab diagram](topology.png)

In this lab we will use following python module:

#### [telnetlib](https://docs.python.org/3/library/telnetlib.html) — Telnet client

The python telnetlib module provides a Telnet class that implements the Telnet protocol.
This telnetlib (scripts) in *[my repo](telnet)* has been completely tested and verified on 20 Jun, 2021 using GNS3.

#### [Pexpect](https://pexpect.readthedocs.io/en/stable/index.html)

Pexpect can be used for automating interactive applications such as ssh, ftp, passwd, telnet, etc.
This pexpect (scripts) in *[my repo](pexpect)* has been completely tested and verified on 22 Jun, 2021 using GNS3.

#### [paramiko](http://www.paramiko.org/)

Paramiko is a Python (2.7, 3.4+) implementation of the SSHv2 protocol, providing both client and server functionality.
Paramiko itself is a pure Python interface around SSH networking concepts.
This Paramiko(scripts) in *[my repo](paramiko)* has been completely tested and verified on 24 Jun, 2021 using GNS3.

#### [Netmiko](https://pypi.org/project/netmiko/)

developed by Kirk Byers is an open-source multi vendor library that is used for SSH connections to network devices. Multi-vendor library means, Netmiko supports network devices from different vendors such as Cisco, Juniper , HP etc.

#### [Python Exercise](python_exe)
