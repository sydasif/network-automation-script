"""
Network Utilities for Network Automation Scripts
Provides reusable functions for network operations with proper error handling.
"""
from contextlib import contextmanager
from typing import Dict, Any, Generator, Optional
import logging
from netmiko import ConnectHandler
from netmiko.exceptions import NetMikoTimeoutException, AuthenticationException
from paramiko.ssh_exception import SSHException
from config_manager import ConfigManager, DeviceConfig


# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class NetworkError(Exception):
    """Custom exception for network operations"""
    pass


@contextmanager
def connect_to_device(device_config: DeviceConfig) -> Generator[Any, None, None]:
    """
    Context manager for connecting to network devices with proper cleanup
    """
    connection = None
    try:
        logger.info(f"Connecting to {device_config.host}")

        net_connect = ConnectHandler(
            device_type=device_config.device_type,
            host=device_config.host,
            username=device_config.username,
            password=device_config.password,
            secret=device_config.secret,
            port=device_config.port,
            timeout=device_config.timeout,
            # More secure defaults
            use_keys=False,
            allow_agent=False,
            auth_timeout=30
        )

        # Enter enable mode if secret is provided
        if device_config.secret:
            net_connect.enable()

        yield net_connect

    except NetMikoTimeoutException:
        logger.error(f"Timeout connecting to {device_config.host}")
        raise NetworkError(f"Device {device_config.host} not reachable")
    except AuthenticationException:
        logger.error(f"Authentication failed for {device_config.host}")
        raise NetworkError(f"Authentication failed for {device_config.host}")
    except SSHException as e:
        logger.error(f"SSH error connecting to {device_config.host}: {str(e)}")
        raise NetworkError(f"SSH error connecting to {device_config.host}: {str(e)}")
    except Exception as e:
        logger.error(f"Unexpected error connecting to {device_config.host}: {str(e)}")
        raise NetworkError(f"Unexpected error connecting to {device_config.host}: {str(e)}")
    finally:
        if connection:
            try:
                connection.disconnect()
                logger.info(f"Disconnected from {device_config.host}")
            except:
                logger.warning(f"Could not disconnect from {device_config.host}")


def execute_command(device_config: DeviceConfig, command: str, use_textfsm: bool = False) -> Optional[str]:
    """
    Execute a command on a network device
    """
    try:
        with connect_to_device(device_config) as conn:
            output = conn.send_command(command, use_textfsm=use_textfsm)
            logger.info(f"Command '{command}' executed successfully on {device_config.host}")
            return output
    except NetworkError as e:
        logger.error(f"Failed to execute command on {device_config.host}: {str(e)}")
        return None


def send_config(device_config: DeviceConfig, config_commands: list) -> Optional[str]:
    """
    Send configuration commands to a network device
    """
    try:
        with connect_to_device(device_config) as conn:
            output = conn.send_config_set(config_commands)
            logger.info(f"Configuration sent successfully to {device_config.host}")
            return output
    except NetworkError as e:
        logger.error(f"Failed to send configuration to {device_config.host}: {str(e)}")
        return None


def backup_config(device_config: DeviceConfig, filename: Optional[str] = None) -> bool:
    """
    Backup device configuration to file
    """
    try:
        config = execute_command(device_config, "show running-config")
        if config is None:
            return False

        # Generate filename if not provided
        if filename is None:
            import datetime
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            hostname = device_config.host.replace('.', '_')
            filename = f"{hostname}_backup_{timestamp}.cfg"

        with open(filename, 'w') as f:
            f.write(config)

        logger.info(f"Configuration backed up to {filename}")
        return True
    except Exception as e:
        logger.error(f"Failed to backup configuration from {device_config.host}: {str(e)}")
        return False


def create_vlan(device_config: DeviceConfig, vlan_id: int, vlan_name: Optional[str] = None) -> bool:
    """
    Create a VLAN on a network device
    """
    if vlan_name is None:
        vlan_name = f"VLAN_{vlan_id}"

    config_commands = [
        f"vlan {vlan_id}",
        f"name {vlan_name}",
        "exit"
    ]

    try:
        result = send_config(device_config, config_commands)
        if result is not None:
            logger.info(f"VLAN {vlan_id} created successfully on {device_config.host}")
            return True
        return False
    except Exception as e:
        logger.error(f"Failed to create VLAN {vlan_id} on {device_config.host}: {str(e)}")
        return False


def get_device_facts(device_config: DeviceConfig) -> Optional[Dict[str, Any]]:
    """
    Get device facts using show commands
    """
    facts = {}

    # Get device version
    version_output = execute_command(device_config, "show version")
    if version_output:
        facts['version'] = version_output

    # Get interface status
    interface_output = execute_command(device_config, "show ip interface brief")
    if interface_output:
        facts['interfaces'] = interface_output

    # Get VLAN information
    vlan_output = execute_command(device_config, "show vlan brief")
    if vlan_output:
        facts['vlans'] = vlan_output

    return facts if facts else None


def batch_operation(device_configs: list, operation_func, *args, **kwargs) -> Dict[str, Any]:
    """
    Perform an operation on multiple devices
    """
    results = {}

    for device_config in device_configs:
        try:
            result = operation_func(device_config, *args, **kwargs)
            results[device_config.host] = {'success': True, 'result': result}
        except Exception as e:
            logger.error(f"Operation failed on {device_config.host}: {str(e)}")
            results[device_config.host] = {'success': False, 'error': str(e)}

    return results


# Example usage
if __name__ == "__main__":
    # Example: Initialize config manager and connect to device
    config_mgr = ConfigManager()
    r1_config = config_mgr.get_device_config('R1')

    if r1_config:
        # Test connection
        with connect_to_device(r1_config) as conn:
            output = conn.send_command("show version | i uptime")
            print(f"Device uptime: {output}")