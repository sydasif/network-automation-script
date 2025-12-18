"""
Secure VLAN Creation Script
Replaces the insecure telnet/05_create_vlans.py with a secure SSH version
"""
from network_utils import create_vlan, batch_operation
from config_manager import ConfigManager
import sys


def create_vlans_on_device(device_config, start_vlan, end_vlan):
    """
    Create multiple VLANs on a single device
    """
    print(f"Creating VLANs {start_vlan} to {end_vlan} on {device_config.host}")

    success_count = 0
    for vlan_id in range(start_vlan, end_vlan + 1):
        vlan_name = f"Python_VLAN_{vlan_id}"
        if create_vlan(device_config, vlan_id, vlan_name):
            print(f"✓ VLAN {vlan_id} ({vlan_name}) created successfully")
            success_count += 1
        else:
            print(f"✗ Failed to create VLAN {vlan_id}")

    print(f"Created {success_count} out of {end_vlan - start_vlan + 1} VLANs on {device_config.host}")
    return success_count == (end_vlan - start_vlan + 1)


def main():
    # Initialize configuration manager
    config_mgr = ConfigManager()

    # Get device name from command line or default to R1
    device_name = sys.argv[1] if len(sys.argv) > 1 else 'R1'

    # Get start and end VLAN numbers
    start_vlan = int(sys.argv[2]) if len(sys.argv) > 2 else 2
    end_vlan = int(sys.argv[3]) if len(sys.argv) > 3 else 9

    # Get device configuration
    device_config = config_mgr.get_device_config(device_name)
    if not device_config:
        print(f"Error: Device {device_name} not found in configuration")
        return

    # Create VLANs
    success = create_vlans_on_device(device_config, start_vlan, end_vlan)

    if success:
        print(f"\nAll VLANs created successfully on {device_name} ({device_config.host})")
    else:
        print(f"\nSome VLANs failed to create on {device_name} ({device_config.host})")


if __name__ == "__main__":
    main()