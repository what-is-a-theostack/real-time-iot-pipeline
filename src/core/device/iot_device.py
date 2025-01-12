from base_device import BaseDevice

class IoTDevice(BaseDevice):
    def __init__(self, manufacturer, make, model, serial_number, name, ip_address, mac_address, description=None):
        super().__init__(manufacturer, make, model, serial_number, name, description)
        self.ip_address = ip_address
        self.mac_address = mac_address
        self.protocols_supported = []
        self.firmware_version = "1.0.0"
        self.battery_level = 100  # Default battery level (percent)

    def add_protocol(self, protocol):
        """Add a supported protocol."""
        if protocol not in self.protocols_supported:
            self.protocols_supported.append(protocol)
            self._log_event(f"Protocol '{protocol}' added.")

    def remove_protocol(self, protocol):
        """Remove a supported protocol."""
        if protocol in self.protocols_supported:
            self.protocols_supported.remove(protocol)
            self._log_event(f"Protocol '{protocol}' removed.")

    def update_firmware(self, new_version):
        """Simulate a firmware update."""
        self.firmware_version = new_version
        self._log_event(f"Firmware updated to version {new_version}.")

    def report_battery(self):
        """Report the battery level."""
        self._log_event(f"Battery level: {self.battery_level}%")
        return self.battery_level

    def simulate_network_delay(self, min_ms=50, max_ms=300):
        """Simulate network delay."""
        import random
        delay = random.randint(min_ms, max_ms)
        self._log_event(f"Simulated network delay: {delay}ms")
        return delay

