import unittest
from core.device.legacy_device import LegacyDevice

class TestLegacyDevice(unittest.TestCase):

    def setUp(self):
        self.device = LegacyDevice("TestManufacturer", "TestMake", "TestModel", "12345", "TestDevice")

    def test_convert_analog_to_digital(self):
        self.assertEqual(self.device.convert_analog_to_digital(0), 0)
        self.assertEqual(self.device.convert_analog_to_digital(5), 128)
        self.assertEqual(self.device.convert_analog_to_digital(10), 255)
        with self.assertRaises(ValueError):
            self.device.convert_analog_to_digital(-1)
        with self.assertRaises(ValueError):
            self.device.convert_analog_to_digital(11)

    def test_convert_digital_to_analog(self):
        self.assertAlmostEqual(self.device.convert_digital_to_analog(0), 0)
        self.assertAlmostEqual(self.device.convert_digital_to_analog(128), 5, places=1)
        self.assertAlmostEqual(self.device.convert_digital_to_analog(255), 10)
        with self.assertRaises(ValueError):
            self.device.convert_digital_to_analog(-1)
        with self.assertRaises(ValueError):
            self.device.convert_digital_to_analog(256)

    def test_add_noise_to_signal(self):
        analog_value = 5
        noise_level = 0.1
        noisy_value = self.device.add_noise_to_signal(analog_value, noise_level)
        self.assertTrue(0 <= noisy_value <= 10)
        self.assertNotEqual(analog_value, noisy_value)

if __name__ == '__main__':
    unittest.main()