import unittest
from core.device.components.sensor_device import SensorDevice

class TestSensorDevice(unittest.TestCase):
    def setUp(self):
        self.device = SensorDevice()

    def test_add_sensor(self):
        self.device.add_sensor("temperature", "Thermometer")
        self.assertIn("temperature", self.device.sensors)
        self.assertEqual(self.device.sensors["temperature"], "Thermometer")

    def test_read_sensor(self):
        self.device.add_sensor("humidity", "Hygrometer")
        value = self.device.read_sensor("humidity")
        self.assertEqual(value, "Simulated value from humidity")

    def test_read_nonexistent_sensor(self):
        with self.assertRaises(ValueError) as context:
            self.device.read_sensor("pressure")
        self.assertEqual(str(context.exception), "Sensor 'pressure' does not exist.")

if __name__ == '__main__':
    unittest.main()