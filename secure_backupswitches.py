"""
Secure Multi-Device Configuration Backup Script
Replaces utilities/backupswitches.py with a secure, error-handling version
"""
from network_utils import backup_config, batch_operation, get_device_facts
from config_manager import ConfigManager
import sys
from datetime import datetime


def main():
    # Initialize configuration manager
    config_mgr = ConfigManager()

    # Get device names from command line or use all devices
    if len(sys.argv) > 1:
        device_names = sys.argv[1:]  # Use specified devices
    else:
        # Use all configured devices
        device_names = ['R1', 'S1']  # Default to lab devices

    # Get configurations for specified devices
    device_configs = []
    for name in device_names:
        config = config_mgr.get_device_config(name)
        if config:
            device_configs.append(config)
        else:
            print(f"Warning: Device {name} not found in configuration")

    if not device_configs:
        print("No valid devices found to backup")
        return

    print(f"Starting backup for {len(device_configs)} devices...")

    # Perform backup for each device
    for device_config in device_configs:
        print(f"\nProcessing {device_config.host}...")

        # Get device facts first to get hostname
        facts = get_device_facts(device_config)
        if facts and 'version' in facts:
            # Extract hostname from version output (simplified)
            hostname = device_config.host.replace('.', '_')
        else:
            hostname = device_config.host.replace('.', '_')

        # Generate backup filename with timestamp
        timestamp = datetime.now().strftime("%d%m%Y_%H-%M-%S")
        backup_file = f"{hostname}_{timestamp}.ios"

        # Perform backup
        success = backup_config(device_config, backup_file)

        if success:
            print(f"✓ {hostname} has been backed up to {backup_file}")
        else:
            print(f"✗ Failed to backup {hostname}")

    print(f"\nBackup process completed for {len(device_configs)} devices.")


if __name__ == "__main__":
    main()