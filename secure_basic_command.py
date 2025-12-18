"""
Secure Network Command Execution Script
Replaces the insecure telnet/01_basic_command.py with a secure SSH version
"""
from network_utils import execute_command, connect_to_device
from config_manager import ConfigManager
import getpass
import sys


def main():
    # Initialize configuration manager
    config_mgr = ConfigManager()

    # Get device name from command line or default to R1
    device_name = sys.argv[1] if len(sys.argv) > 1 else 'R1'

    # Get device configuration
    device_config = config_mgr.get_device_config(device_name)
    if not device_config:
        print(f"Error: Device {device_name} not found in configuration")
        return

    print(f"Connecting to device: {device_config.host}")

    # Get command from user
    cmd = input("Enter the Command: ")

    # Execute the command
    result = execute_command(device_config, cmd)

    if result is not None:
        print("Command output:")
        print(result)
    else:
        print("Failed to execute command")


if __name__ == "__main__":
    main()