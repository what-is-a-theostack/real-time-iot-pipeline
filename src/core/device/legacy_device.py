from base_device import BaseDevice

class LegacyDevice(BaseDevice):
    def __init__(self, manufacturer, make, model, serial_number, name, voltage_range=10, description=None):
        super().__init__(manufacturer, make, model, serial_number, name, description)
        self.voltage_range = voltage_range

    def convert_analog_to_digital(self, analog_value):
        """Simulate analog-to-digital conversion."""
        if analog_value < 0 or analog_value > self.voltage_range:
            raise ValueError("Analog value out of range!")
        digital_value = round((analog_value / self.voltage_range) * 255)
        self._log_event(f"Analog-to-digital conversion: {analog_value}V -> {digital_value} (digital)")
        return digital_value

    def convert_digital_to_analog(self, digital_value):
        """Simulate digital-to-analog conversion."""
        if digital_value < 0 or digital_value > 255:
            raise ValueError("Digital value out of range!")
        analog_value = (digital_value / 255) * self.voltage_range
        self._log_event(f"Digital-to-analog conversion: {digital_value} -> {analog_value}V")
        return analog_value

    def add_noise_to_signal(self, analog_value, noise_level=0.05):
        """Add noise to an analog signal."""
        import random
        noise = random.uniform(-noise_level, noise_level) * self.voltage_range
        noisy_value = max(0, min(self.voltage_range, analog_value + noise))
        self._log_event(f"Added noise: {analog_value}V -> {noisy_value}V")
        return noisy_value