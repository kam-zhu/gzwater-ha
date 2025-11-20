"""Sensor platform for gzwater integration."""

from homeassistant.const import CONF_NAME
from homeassistant.helpers.entity import Entity
from homeassistant.helpers.update_coordinator import CoordinatorEntity

# 设置正确的Python路径，确保能够导入const模块
import sys
import os

# 获取当前文件所在目录的父目录（即gzwater目录）
gzwater_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 将gzwater目录添加到Python路径，这样就能直接导入custom_components模块
sys.path.append(gzwater_dir)

# 导入常量
from custom_components.const import DOMAIN, SENSOR_TYPES

async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    """Set up the gzwater sensor platform."""
    if discovery_info is None:
        return
    
    coordinator = hass.data[DOMAIN]["coordinator"]
    
    sensors = []
    for sensor_type in SENSOR_TYPES:
        sensors.append(GzWaterSensor(coordinator, sensor_type))
    
    async_add_entities(sensors, True)

class GzWaterSensor(CoordinatorEntity, Entity):
    """Representation of a gzwater sensor."""
    
    def __init__(self, coordinator, sensor_type):
        """Initialize the sensor."""
        super().__init__(coordinator)
        self.sensor_type = sensor_type
        self._name = f"广州自来水 {SENSOR_TYPES[sensor_type]['name']}"
        self._unit_of_measurement = SENSOR_TYPES[sensor_type]["unit"]
        self._icon = SENSOR_TYPES[sensor_type]["icon"]
        self._state = None
    
    @property
    def name(self):
        """Return the name of the sensor."""
        return self._name
    
    @property
    def state(self):
        """Return the state of the sensor."""
        if self.coordinator.data:
            return self.coordinator.data.get(self.sensor_type)
        return None
    
    @property
    def unit_of_measurement(self):
        """Return the unit of measurement."""
        return self._unit_of_measurement
    
    @property
    def icon(self):
        """Return the icon of the sensor."""
        return self._icon
    
    @property
    def unique_id(self):
        """Return a unique ID."""
        return f"{DOMAIN}_{self.sensor_type}"
    
    @property
    def device_info(self):
        """Return device information."""
        return {
            "identifiers": {(DOMAIN, "gzwater_device")},
            "name": "广州市自来水",
            "manufacturer": "广州市自来水公司",
        }