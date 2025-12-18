"""
Secure Multi-Device VLAN Creation Script
Replaces netmiko/ex_06_vlan_multi_device.py with secure, error-handling version
"""
from network_utils import create_vlan, batch_operation
from config_manager import ConfigManager
import sys


def create_vlans_on_multiple_devices(device_names, start_vlan, end_vlan):
    """
    Create VLANs on multiple devices
    """
    config_mgr = ConfigManager()

    # Get configurations for specified devices
    device_configs = []
    for name in device_names:
        config = config_mgr.get_device_config(name)
        if config:
            device_configs.append(config)
        else:
            print(f"Warning: Device {name} not found in configuration")

    if not device_configs:
        print("No valid devices found")
        return

    print(f"Creating VLANs {start_vlan} to {end_vlan} on {len(device_configs)} devices...")

    # Create VLANs on each device
    for device_config in device_configs:
        print(f"\nProcessing device {device_config.host}...")

        success_count = 0
        for vlan_id in range(start_vlan, end_vlan + 1):
            vlan_name = f"DevOps_VLAN_{vlan_id}"
            print(f"  Creating VLAN {vlan_id} ({vlan_name})...")

            if create_vlan(device_config, vlan_id, vlan_name):
                print(f"  ✓ VLAN {vlan_id} created successfully")
                success_count += 1
            else:
                print(f"  ✗ Failed to create VLAN {vlan_id}")

        print(f"  Completed: {success_count}/{end_vlan - start_vlan + 1} VLANs created on {device_config.host}")


def main():
    # Get device names from command line or use defaults
    if len(sys.argv) > 1:
        device_names = sys.argv[1:]  # Use specified devices
    else:
        # Default to lab devices
        device_names = ['R1', 'S1']

    # Get VLAN range from command line or use defaults
    start_vlan = int(sys.argv[len(device_names) + 1]) if len(sys.argv) > len(device_names) + 1 else 10
    end_vlan = int(sys.argv[len(device_names) + 2]) if len(sys.argv) > len(device_names) + 2 else 14

    create_vlans_on_multiple_devices(device_names, start_vlan, end_vlan)


if __name__ == "__main__":
    main()