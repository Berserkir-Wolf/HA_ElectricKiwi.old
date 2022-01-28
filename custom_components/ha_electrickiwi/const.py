"""Constants for the Electric Kiwi Sensor integration."""

# Base component constants
NAME = "Electric Kiwi"
DOMAIN = "electrickiwi"
DOMAIN_DATA = f"{DOMAIN}_data"
#VERSION = "0.1.0"

#ATTRIBUTION = "Data provided by http://jsonplaceholder.typicode.com/"
ISSUE_URL = "https://github.com/Berserkir-Wolf/HA_ElectricKiwi/issues"

# Icons
ICON = "mdi:home-lightning-bolt"

# Device classes
BINARY_SENSOR_DEVICE_CLASS = "connectivity"

# Platforms
BINARY_SENSOR = "binary_sensor"
SENSOR = "sensor"
SWITCH = "switch"
PLATFORMS = [SENSOR]


# Configuration and options
CONF_ENABLED = "enabled"
CONF_NAME = "name"
CONF_CUSTOMERNUMBER = "customernumber"
CONF_PASSWORD = "password"

# Defaults
DEFAULT_NAME = DOMAIN

STARTUP_MESSAGE = f"""
-------------------------------------------------------------------
{NAME}
Version: {VERSION}
This is a custom integration!
If you have any issues with this you need to open an issue here:
{ISSUE_URL}
-------------------------------------------------------------------
"""