from homeassistant.components.binary_sensor import BinarySensorEntity
from homeassistant.helpers.update_coordinator import CoordinatorEntity
from .const import DOMAIN

async def async_setup_entry(hass, config_entry, async_add_entities):
    coordinator = hass.data[DOMAIN][config_entry.entry_id]
    async_add_entities([FlaggdagBinarySensor(coordinator)])

class FlaggdagBinarySensor(CoordinatorEntity, BinarySensorEntity):
    def __init__(self, coordinator):
        super().__init__(coordinator)
        self._attr_name = "Flaggdag"
        self._attr_unique_id = "no_flaggdager_flaggdag"
        self._attr_icon = "mdi:flag"

    @property
    def is_on(self):
        return self.coordinator.data["is_flaggdag"]


