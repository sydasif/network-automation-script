# Network Automation

--------------------

## What is Network Automation?

Network automation is the process of automating the configuration, management and operations of a computer network. The tasks that were normally done by the network or system administrator can be automated using a number of tools and technologies.

Scripting languages are widely used by Network and System administrators for automating the tasks. This saves time, effort and thereby reducing human errors as well. Among the automation tools, Python and Ansible are the most popular ones. With Software Defined Networking (SDN) in picture, knowing any of these
programming languages is vital for the future of administering the network and systems.

### Security Notice

⚠️ **Important**: The scripts in the individual directories (telnet/, paramiko/, netmiko/, etc.) contain hardcoded credentials and use insecure protocols like telnet. These are for educational purposes only.

For production use, please refer to our **secure refactored scripts** in the main directory:

- See `SECURE_README.md` for the new secure approach
- Use `config_manager.py` and `network_utils.py` for secure operations
- Follow security best practices with environment variables

### Python for Network Engineer

#### Free Ebooks

- **Natasha Samoilenko** [*Python for Network Engineer*](https://pyneng.readthedocs.io/en/latest/)
- **Lisa Tagliaferri** [*How to Code in Python*](https://www.digitalocean.com/community/books/digitalocean-ebook-how-to-code-in-python)

#### Python Libraries

- [Telnet Scripts for Network Engineers](docs/telnet.md) (Educational only)
- [Automating Network Device Interaction with Pexpect](docs/pexpect.md)
- [Paramiko Module](docs/paramiko.md)

#### Secure Network Automation

- [Secure Network Automation Guide](SECURE_README.md) (Recommended for production)
- [Configuration Management](config_manager.py)
- [Network Utilities](network_utils.py)
