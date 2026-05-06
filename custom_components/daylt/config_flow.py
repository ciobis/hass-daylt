"""Config flow for Day LT integration."""
import voluptuous as vol

from homeassistant.config_entries import ConfigFlow
from homeassistant.const import CONF_NAME

from . import DOMAIN

DEFAULT_NAME = "Day LT Info"


class DayLtConfigFlow(ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Day LT."""

    VERSION = 1

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        await self.async_set_unique_id(DOMAIN)
        self._abort_if_unique_id_configured()

        if user_input is not None:
            return self.async_create_entry(
                title=user_input.get(CONF_NAME, DEFAULT_NAME),
                data=user_input,
            )

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema(
                {vol.Optional(CONF_NAME, default=DEFAULT_NAME): str}
            ),
        )
