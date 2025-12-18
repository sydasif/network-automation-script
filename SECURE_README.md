# Network Automation - Refactored

This repository contains refactored network automation scripts with improved security, maintainability, and best practices.

## New Architecture

### Core Components

- `config_manager.py` - Centralized configuration management
- `network_utils.py` - Reusable network operations with error handling
- Secure credential management using environment variables
- Context managers for proper connection handling

### Key Improvements

1. **Security**: No hardcoded credentials, using environment variables
2. **Error Handling**: Comprehensive exception handling for network operations
3. **Maintainability**: Modular, reusable code components
4. **Best Practices**: Context managers, proper resource cleanup

## Setup

### 1. Environment Configuration

```bash
# Copy the example environment file
cp .env.example .env

# Edit .env with your actual credentials and IP addresses
nano .env
```

### 2. Install Dependencies

```bash
pip install netmiko paramiko pyyaml python-dotenv
```

### 3. Source Environment Variables

```bash
export $(grep -v '^#' .env | xargs)
```

## New Scripts

### Basic Command Execution

```bash
python secure_basic_command.py [device_name]
```

### VLAN Creation

```bash
# Create VLANs 2-9 on R1
python secure_create_vlans.py R1 2 9

# Create VLANs 10-15 on S1
python secure_create_vlans.py S1 10 15
```

### Multi-Device Operations

```bash
# Backup configurations from multiple devices
python secure_backupswitches.py R1 S1

# Create VLANs on multiple devices
python secure_vlan_multi_device.py R1 S1 10 14
```

## Configuration Management

### Using ConfigManager

```python
from config_manager import ConfigManager

config_mgr = ConfigManager()
device_config = config_mgr.get_device_config('R1')
```

### Configuration Sources (in priority order)

1. Environment variables
2. Configuration file (config.yml)
3. Default values

## Network Utilities

### Available Functions

- `connect_to_device()` - Context manager for secure connections
- `execute_command()` - Execute commands with error handling
- `send_config()` - Send configuration commands
- `backup_config()` - Backup device configurations
- `create_vlan()` - Create VLANs with error handling
- `get_device_facts()` - Get device information
- `batch_operation()` - Perform operations on multiple devices

## Migration Guide

### From Old Scripts to New

- Old: `telnet/01_basic_command.py` → New: `secure_basic_command.py`
- Old: `telnet/05_create_vlans.py` → New: `secure_create_vlans.py`
- Old: `utilities/backupswitches.py` → New: `secure_backupswitches.py`
- Old: `netmiko/ex_06_vlan_multi_device.py` → New: `secure_vlan_multi_device.py`

## Security Best Practices

1. Never commit credentials to version control
2. Use environment variables for sensitive data
3. Implement proper error handling to prevent information disclosure
4. Use SSH instead of telnet for all connections
5. Validate input parameters before using them

## Adding New Devices

### Method 1: Environment Variables

```bash
export DEVICE_NEW_ROUTER_IP=192.168.1.100
```

### Method 2: Configuration File

Create `config.yml`:

```yaml
devices:
  NEW_ROUTER:
    host: 192.168.1.100
    device_type: cisco_ios
    username: admin
    password: secure_password
    secret: enable_password
```

## Error Handling

All network operations now include:

- Connection timeout handling
- Authentication failure handling
- SSH exception handling
- Graceful connection cleanup
- Detailed logging

## Running the Scripts

### Example 1: Basic Command

```bash
# Load environment
export $(grep -v '^#' .env | xargs)

# Run basic command
python secure_basic_command.py R1
```

### Example 2: Multi-Device VLAN Creation

```bash
# Create VLANs 5-8 on both R1 and S1
python secure_vlan_multi_device.py R1 S1 5 8
```

### Example 3: Configuration Backup

```bash
# Backup configurations from all devices
python secure_backupswitches.py
```

## Development

When creating new scripts, use the provided utilities:

```python
from network_utils import execute_command, connect_to_device
from config_manager import ConfigManager

def my_network_script():
    config_mgr = ConfigManager()
    device_config = config_mgr.get_device_config('R1')

    # Use the utilities for all network operations
    result = execute_command(device_config, "show version")
    print(result)
```

This refactored approach provides a secure, maintainable foundation for network automation that follows industry best practices.
