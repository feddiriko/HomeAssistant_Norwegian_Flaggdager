from homeassistant.components.sensor import SensorEntity
from homeassistant.helpers.update_coordinator import CoordinatorEntity
from .const import DOMAIN

async def async_setup_entry(hass, config_entry, async_add_entities):
    coordinator = hass.data[DOMAIN][config_entry.entry_id]
    async_add_entities([FlaggdagNavnSensor(coordinator)])

class FlaggdagNavnSensor(CoordinatorEntity, SensorEntity):
    def __init__(self, coordinator):
        super().__init__(coordinator)
        self._attr_name = "Flaggdag Navn"
        self._attr_unique_id = "no_flaggdager_flaggdag_navn"
        self._attr_icon = "mdi:flag-variant" 

    @property
    def native_value(self):
        return self.coordinator.data["flaggdag_navn"]

