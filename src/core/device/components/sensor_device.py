from core.device.base_device import BaseDevice

# Handle Sensor Specific Functionality in Device Building
class SensorDevice(BaseDevice):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sensors = {}

    def add_sensor(self, sensor_name, sensor_type):
        """Add a sensor to the device."""
        self.sensors[sensor_name] = sensor_type
        self._log_event(f"Sensor '{sensor_name}' ({sensor_type}) added.")

    def read_sensor(self, sensor_name):
        """Simulate reading from a sensor."""
        if sensor_name in self.sensors:
            value = f"Simulated value from {sensor_name}"
            self._log_event(f"Read from sensor '{sensor_name}': {value}")
            return value
        else:
            raise ValueError(f"Sensor '{sensor_name}' does not exist.")