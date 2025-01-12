class BaseDevice:
    def __init__(
        self, manufacturer, make, model, serial_number, name, description=None
    ):
        """
        Base class for all devices.

        :param manufacturer: (str) The manufacturer of the device.
        :param make: (str) The make or family of the device.
        :param model: (str) The specific model of the device.
        :param serial_number: (str) A unique identifier for the device.
        :param name: (str) A user-defined name for the device.
        :param description: (str, optional) Additional details about the device.
        """
        self.manufacturer = manufacturer
        self.make = make
        self.model = model
        self.serial_number = serial_number
        self.name = name
        self.description = description or "No description provided."

        # Core properties
        self.status = "inactive"  # Default lifecycle state
        self.inputs = {}  # A dictionary to define input ports or signals
        self.outputs = {}  # A dictionary to define output ports or signals
        self.metadata = {}  # Arbitrary metadata for extensions

        # Event log
        self.log = []  # Event log

    def activate(self):
        """Activate the device."""
        self.status = "active"
        self._log_event(f"{self.name} activated.")
        self.on_activate()

    def deactivate(self):
        """Deactivate the device."""
        self.status = "inactive"
        self._log_event(f"{self.name} deactivated.")
        self.on_deactivate()

    def on_activate(self):
        """Hook for additional activation behavior."""
        pass

    def on_deactivate(self):
        """Hook for additional deactivation behavior."""
        pass

    def add_input(self, input_name, signal_type):
        """Add an input to the device."""
        self.inputs[input_name] = signal_type
        self._log_event(f"Input '{input_name}' ({signal_type}) added.")

    def add_output(self, output_name, signal_type):
        """Add an output to the device."""
        self.outputs[output_name] = signal_type
        self._log_event(f"Output '{output_name}' ({signal_type}) added.")

    def read_input(self, input_name):
        """Simulate reading from an input."""
        if input_name in self.inputs:
            value = f"Simulated value from {input_name}"
            self._log_event(f"Read from input '{input_name}': {value}")
            return value
        else:
            raise ValueError(f"Input '{input_name}' does not exist.")

    def write_output(self, output_name, value):
        """Simulate writing to an output."""
        if output_name in self.outputs:
            self._log_event(f"Wrote value '{value}' to output '{output_name}'.")
        else:
            raise ValueError(f"Output '{output_name}' does not exist.")

    def reset(self):
        """Reset the device to its initial state."""
        self.status = "inactive"
        self.inputs.clear()
        self.outputs.clear()
        self.metadata.clear()
        self.log.clear()
        self._log_event(f"{self.name} reset to initial state.")

    def get_info(self):
        """Return a summary of the device information."""
        info = {
            "manufacturer": self.manufacturer,
            "make": self.make,
            "model": self.model,
            "serial_number": self.serial_number,
            "name": self.name,
            "description": self.description,
            "status": self.status,
            "inputs": self.inputs,
            "outputs": self.outputs,
            "metadata": self.metadata,
            "log": self.log,
        }
        return info

    def update_metadata(self, key, value):
        """Update metadata for the device."""
        self.metadata[key] = value
        self._log_event(f"Metadata updated: {key} = {value}")

    def get_log(self):
        """Return the event log."""
        return self.log

    def _log_event(self, message):
        """Log an event."""
        self.log.append(message)
