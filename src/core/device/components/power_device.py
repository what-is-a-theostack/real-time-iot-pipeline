from core.device.base_device import BaseDevice
import time

class PowerDevice(BaseDevice):
    def __init__(self, *args, **kwargs):
        """
        A device with power consumption tracking.
        """
        super().__init__(*args, **kwargs)
        self.power_consumption = 0  # Current power usage in watts
        self.total_energy = 0  # Total energy usage in kWh
        self.last_update_time = None  # Time of last power update

    def report_power(self, watts):
        """Set and report power consumption."""
        self.power_consumption = watts
        self._log_event(f"Power consumption reported: {watts}W.")
        print(f"{self.name} is consuming {watts} watts.")

    def update_energy(self):
        """Update total energy usage based on elapsed time."""
        if self.last_update_time is None:
            self.last_update_time = time.time()
            return
        current_time = time.time()
        elapsed_time = (
            current_time - self.last_update_time
        ) / 3600  # Convert seconds to hours
        self.total_energy += (
            self.power_consumption * elapsed_time / 1000
        )  # Convert watts to kWh
        self.last_update_time = current_time
        self._log_event(f"Energy updated: Total = {self.total_energy:.4f} kWh.")

    def get_energy(self):
        """Get total energy usage."""
        self.update_energy()
        return self.total_energy
