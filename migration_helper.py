"""
Migration Helper Script
This script demonstrates how to migrate old insecure scripts to the new secure approach
"""
from config_manager import ConfigManager
from network_utils import execute_command, connect_to_device
import os


def show_migration_example():
    """
    Shows examples of how to migrate from old insecure code to new secure code
    """
    print("Network Automation Migration Guide")
    print("=" * 50)

    print("\n1. OLD (Insecure) - telnet/01_basic_command.py:")
    print("```python")
    print("# INSECURE - DO NOT USE IN PRODUCTION")
    print("from telnetlib import Telnet")
    print("ip = \"192.168.121.101\"  # Hardcoded IP")
    print("tn = Telnet(ip)")
    print("tn.write(b\"admin\\n\")      # Hardcoded credentials")
    print("tn.write(b\"admin\\n\")")
    print("# Plain text transmission - very insecure!")
    print("```")

    print("\n1. NEW (Secure) - Using our refactored approach:")
    print("```python")
    print("from network_utils import execute_command")
    print("from config_manager import ConfigManager")
    print("")
    print("config_mgr = ConfigManager()")
    print("device_config = config_mgr.get_device_config('R1')")
    print("result = execute_command(device_config, cmd)")
    print("# Uses SSH, secure credentials, proper error handling")
    print("```")

    print("\n2. OLD (Insecure) - Hardcoded credentials:")
    print("```python")
    print("password = \"cisco\"  # Visible in code!")
    print("device = {")
    print("    \"ip\": \"192.168.100.20\",  # Hardcoded IP")
    print("    \"password\": \"cisco\",     # Hardcoded password")
    print("}")
    print("```")

    print("\n2. NEW (Secure) - Environment-based credentials:")
    print("```python")
    print("from config_manager import ConfigManager")
    print("")
    print("config_mgr = ConfigManager()")
    print("device_config = config_mgr.get_device_config('R1')")
    print("# Credentials loaded from environment variables")
    print("```")

    print("\n3. OLD (Insecure) - No error handling:")
    print("```python")
    print("tn = telnetlib.Telnet(HOST)")
    print("tn.write(user.encode(\"ascii\") + b\"\\n\")")
    print("# No error handling - will crash on failure")
    print("```")

    print("\n3. NEW (Secure) - With error handling:")
    print("```python")
    print("from network_utils import execute_command")
    print("")
    print("result = execute_command(device_config, cmd)")
    print("if result is not None:")
    print("    print(result)")
    print("else:")
    print("    print(\"Command failed\")")
    print("```")


def check_environment():
    """
    Check if the environment is properly configured
    """
    print("\nEnvironment Check")
    print("=" * 20)

    # Check for required environment variables
    required_vars = ['NETWORK_USERNAME', 'NETWORK_PASSWORD', 'NETWORK_ENABLE_PASSWORD']
    missing_vars = []

    for var in required_vars:
        if not os.getenv(var):
            missing_vars.append(var)

    if missing_vars:
        print(f"⚠️  Missing environment variables: {', '.join(missing_vars)}")
        print("Please set them in your .env file and source it:")
        print("  cp .env.example .env")
        print("  # Edit .env with your values")
        print("  export $(grep -v '^#' .env | xargs)")
    else:
        print("✅ All required environment variables are set")

    # Check if config manager can load configuration
    try:
        config_mgr = ConfigManager()
        devices = config_mgr.get_all_devices()
        print(f"✅ Configuration manager loaded successfully")
        print(f"✅ Found {len(devices)} configured devices: {', '.join(devices.keys())}")
    except Exception as e:
        print(f"❌ Configuration manager failed: {e}")


def run_basic_test():
    """
    Run a basic connectivity test to verify the new system works
    """
    print("\nBasic Connectivity Test")
    print("=" * 25)

    try:
        config_mgr = ConfigManager()
        r1_config = config_mgr.get_device_config('R1')

        if r1_config:
            print(f"Testing connection to R1 ({r1_config.host})...")

            # Test basic command execution
            result = execute_command(r1_config, "show version | i uptime", use_textfsm=False)

            if result:
                print("✅ Connection successful!")
                print("Device uptime (sample output):")
                print(result[:200] + "..." if len(result) > 200 else result)
            else:
                print("❌ Connection failed - check device connectivity and credentials")
        else:
            print("❌ R1 device configuration not found")
    except Exception as e:
        print(f"❌ Test failed with error: {e}")


def main():
    print("Network Automation Migration Helper")
    print("This tool helps migrate from insecure to secure network automation scripts")
    print()

    show_migration_example()
    check_environment()
    run_basic_test()

    print("\nNext Steps:")
    print("1. Review SECURE_README.md for complete setup instructions")
    print("2. Update your .env file with real credentials")
    print("3. Replace old scripts with new secure versions")
    print("4. Test connectivity before deploying to production")
    print("5. Use the new config_manager.py and network_utils.py modules")


if __name__ == "__main__":
    main()