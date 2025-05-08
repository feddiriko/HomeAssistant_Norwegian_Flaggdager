import logging
from datetime import datetime, timedelta
from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator
from .flaggdager import get_flaggdag

_LOGGER = logging.getLogger(__name__)

class FlaggdagCoordinator(DataUpdateCoordinator):
    def __init__(self, hass: HomeAssistant):
        super().__init__(
            hass=hass,
            logger=_LOGGER,
            name="Norske Flaggdager",
            update_method=self._async_update_data,
            update_interval=timedelta(hours=1),  # oppdater én gang i timen
        )

    async def _async_update_data(self):
        today = datetime.now().date()
        flaggdag = get_flaggdag(today)
        return {
            "is_flaggdag": flaggdag is not None,
            "flaggdag_navn": flaggdag or "",
        }
