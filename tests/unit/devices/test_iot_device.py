import unittest
from core.device.iot_device import IoTDevice

class TestIoTDevice(unittest.TestCase):
    def setUp(self):
        self.device = IoTDevice(
            manufacturer="TestManufacturer",
            make="TestMake",
            model="TestModel",
            serial_number="123456789",
            name="TestDevice",
            ip_address="192.168.1.1",
            mac_address="00:1B:44:11:3A:B7"
        )

    def test_add_protocol(self):
        self.device.add_protocol("HTTP")
        self.assertIn("HTTP", self.device.protocols_supported)

    def test_remove_protocol(self):
        self.device.add_protocol("HTTP")
        self.device.remove_protocol("HTTP")
        self.assertNotIn("HTTP", self.device.protocols_supported)

    def test_update_firmware(self):
        self.device.update_firmware("2.0.0")
        self.assertEqual(self.device.firmware_version, "2.0.0")

    def test_report_battery(self):
        battery_level = self.device.report_battery()
        self.assertEqual(battery_level, 100)

    def test_simulate_network_delay(self):
        delay = self.device.simulate_network_delay()
        self.assertGreaterEqual(delay, 50)
        self.assertLessEqual(delay, 300)

if __name__ == '__main__':
    unittest.main()