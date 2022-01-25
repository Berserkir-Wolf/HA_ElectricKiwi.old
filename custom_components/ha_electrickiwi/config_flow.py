"""Config flow for Electric Kiwi Sensor integration."""
import logging

import voluptuous as vol

from homeassistant import config_entries, core, exceptions

from .const import ( CONF_NAME, CONF_PASSWORD, CONF_CUSTOMERNUMBER, DOMAIN, PLATFORMS)

from .api_wrapper import create_client

_LOGGER = logging.getLogger(__name__)

STEP_USER_DATA_SCHEMA = vol.Schema( { 
                 vol.Optional(CONF_NAME, default='Electric Kiwi'): str,
                 vol.Required(CONF_CUSTOMERNUMBER): str,
                 vol.Optional(CONF_PASSWORD): str} )

class HAElectricKiwiConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Electric Kiwi Sensor."""

    VERSION = 1
    CONNECTION_CLASS = config_entries.CONN_CLASS_LOCAL_POLL

    def __init__(self):
        """Initialize."""
        self._errors = {}
        _LOGGER.error("0")


    async def async_step_user(self, user_input=None ):
        """Handle the initial step."""
        if user_input is None:
            return self.async_show_form(
                step_id="user", data_schema=STEP_USER_DATA_SCHEMA
            )

        errors = {}

        valid = await self.hass.async_add_executor_job(
                            create_client,
                            user_input[CONF_CUSTOMERNUMBER], user_input[CONF_PASSWORD]
                        )

        if valid['error'] == 'ok':
            return self.async_create_entry(
                    title=user_input[CONF_NAME], data=user_input
                    )
        else:
            errors["base"] = valid["error"]

        return self.async_show_form(
            step_id="user", data_schema=STEP_USER_DATA_SCHEMA, errors=errors
        )