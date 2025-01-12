from core import Device, IoTDevice, LegacyDevice

if __name__ == "__main__":
    # Test enhanced Device
    base_device = Device("Generic", "Standard", "Model X", "12345", "Base Device")
    base_device.activate()
    base_device.add_input("input_1", "analog")
    base_device.add_output("output_1", "digital")
    print(base_device.read_input("input_1"))
    base_device.update_metadata("location", "Room 101")
    base_device.deactivate()
    print("Event Log:", base_device.get_log())

    # Test enhanced IoTDevice
    smart_plug = IoTDevice("SmartCo", "PlugPro", "S100", "67890", "Smart Plug", "192.168.1.10", "AA:BB:CC:DD:EE:FF")
    smart_plug.add_protocol("MQTT")
    smart_plug.update_firmware("2.0.1")
    print("Battery Level:", smart_plug.report_battery())
    print("Simulated Delay:", smart_plug.simulate_network_delay())

    # Test enhanced LegacyDevice
    thermometer = LegacyDevice("OldTech", "A100", "12345", "Thermometer")
    analog_value = 5.0
    digital_value = thermometer.convert_analog_to_digital(analog_value)
    thermometer.convert_digital_to_analog(digital_value)
    thermometer.add_noise_to_signal(analog_value)
    print("Event Log:", thermometer.get_log())