"""
Configuration Manager for Network Automation Scripts
Provides centralized configuration management and secure credential handling.
"""
import os
import yaml
from typing import Dict, Any, Optional
from dataclasses import dataclass


@dataclass
class DeviceConfig:
    """Data class for device configuration"""
    host: str
    device_type: str
    username: str
    password: str
    secret: Optional[str] = None
    port: int = 22
    timeout: int = 30


class ConfigManager:
    """Centralized configuration manager for network automation"""

    def __init__(self, config_file: Optional[str] = None):
        self.config_file = config_file
        self._config = self._load_config()

    def _load_config(self) -> Dict[str, Any]:
        """Load configuration from file or environment variables"""
        config = {
            'devices': {},
            'defaults': {
                'device_type': 'cisco_ios',
                'username': os.getenv('NETWORK_USERNAME', 'admin'),
                'password': os.getenv('NETWORK_PASSWORD', 'cisco'),
                'secret': os.getenv('NETWORK_ENABLE_PASSWORD', 'cisco'),
                'timeout': 30
            }
        }

        # Load from YAML file if it exists
        if self.config_file and os.path.exists(self.config_file):
            with open(self.config_file, 'r') as f:
                file_config = yaml.safe_load(f)
                if file_config:
                    config.update(file_config)

        # Load device configurations
        self._load_devices(config)

        return config

    def _load_devices(self, config: Dict[str, Any]) -> None:
        """Load device configurations from environment or defaults"""
        # Define default devices based on lab setup
        default_devices = {
            'R1': {
                'host': os.getenv('DEVICE_R1_IP', '192.168.121.101'),
                'device_type': 'cisco_ios',
                'username': config['defaults']['username'],
                'password': config['defaults']['password'],
                'secret': config['defaults']['secret']
            },
            'S1': {
                'host': os.getenv('DEVICE_S1_IP', '192.168.121.102'),
                'device_type': 'cisco_ios',
                'username': config['defaults']['username'],
                'password': config['defaults']['password'],
                'secret': config['defaults']['secret']
            }
        }

        # Override with any devices defined in config file
        config['devices'] = {**default_devices, **config.get('devices', {})}

    def get_device_config(self, device_name: str) -> Optional[DeviceConfig]:
        """Get configuration for a specific device"""
        device_info = self._config['devices'].get(device_name)
        if not device_info:
            return None

        return DeviceConfig(
            host=device_info['host'],
            device_type=device_info.get('device_type', self._config['defaults']['device_type']),
            username=device_info.get('username', self._config['defaults']['username']),
            password=device_info.get('password', self._config['defaults']['password']),
            secret=device_info.get('secret', self._config['defaults']['secret']),
            port=device_info.get('port', 22),
            timeout=device_info.get('timeout', self._config['defaults']['timeout'])
        )

    def get_all_devices(self) -> Dict[str, DeviceConfig]:
        """Get configurations for all devices"""
        devices = {}
        for name in self._config['devices']:
            devices[name] = self.get_device_config(name)
        return {k: v for k, v in devices.items() if v is not None}


# Example configuration file content
EXAMPLE_CONFIG = """
devices:
  R1:
    host: 192.168.121.101
    device_type: cisco_ios
    username: admin
  S1:
    host: 192.168.121.102
    device_type: cisco_ios
    username: admin

defaults:
  device_type: cisco_ios
  timeout: 30
"""


def create_example_config_file():
    """Create an example configuration file"""
    with open('config.example.yml', 'w') as f:
        f.write(EXAMPLE_CONFIG)


if __name__ == "__main__":
    # Create example config file
    create_example_config_file()
    print("Example configuration file created: config.example.yml")

    # Test the configuration manager
    config_mgr = ConfigManager()
    r1_config = config_mgr.get_device_config('R1')
    if r1_config:
        print(f"R1 configuration: {r1_config}")