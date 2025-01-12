class Device:
    def __init__(self, manufacturer, make, model, serial_number, name, description=None):
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
        self.status = "inactive"  # Default status: inactive
        self.inputs = {}  # A dictionary to define input ports or signals
        self.outputs = {}  # A dictionary to define output ports or signals
        self.metadata = {}  # Arbitrary metadata for extensions

    def activate(self):
        """
        Activate the device, setting its status to active.
        """
        self.status = "active"

    def deactivate(self):
        """
        Deactivate the device, setting its status to inactive.
        """
        self.status = "inactive"

    def add_input(self, input_name, signal_type):
        """
        Add an input to the device for digital or analog signals.

        :param input_name: (str) Name of the input (e.g., "analog_input_1").
        :param signal_type: (str) Type of the signal (e.g., "digital" or "analog").
        """
        self.inputs[input_name] = signal_type

    def add_output(self, output_name, signal_type):
        """
        Add an output to the device for digital or analog signals.

        :param output_name: (str) Name of the output (e.g., "digital_output_1").
        :param signal_type: (str) Type of the signal (e.g., "digital" or "analog").
        """
        self.outputs[output_name] = signal_type

    def read_input(self, input_name):
        """
        Simulate reading from an input.

        :param input_name: (str) Name of the input to read.
        :return: Simulated input data (placeholder for now).
        """
        if input_name in self.inputs:
            return f"Reading {self.inputs[input_name]} signal from {input_name}"
        else:
            raise ValueError(f"Input '{input_name}' does not exist.")

    def write_output(self, output_name, value):
        """
        Simulate writing to an output.

        :param output_name: (str) Name of the output to write to.
        :param value: Value to write.
        """
        if output_name in self.outputs:
            print(f"Writing {value} to {output_name} ({self.outputs[output_name]} signal).")
        else:
            raise ValueError(f"Output '{output_name}' does not exist.")

    def get_info(self):
        """
        Returns a dictionary containing all the device's properties.
        """
        return {
            "Manufacturer": self.manufacturer,
            "Make": self.make,
            "Model": self.model,
            "Serial Number": self.serial_number,
            "Name": self.name,
            "Description": self.description,
            "Status": self.status,
            "Inputs": self.inputs,
            "Outputs": self.outputs,
            "Metadata": self.metadata,
        }

    def __str__(self):
        """
        String representation of the device.
        """
        return f"{self.name} ({self.manufacturer} {self.make} {self.model}) - Status: {self.status}"

    def __repr__(self):
        """
        Developer-friendly representation of the device.
        """
        return (
            f"Device(manufacturer={self.manufacturer!r}, make={self.make!r}, model={self.model!r}, "
            f"serial_number={self.serial_number!r}, name={self.name!r}, description={self.description!r}, "
            f"status={self.status!r}, inputs={self.inputs!r}, outputs={self.outputs!r})"
        )