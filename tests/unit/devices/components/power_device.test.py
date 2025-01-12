import time
import unittest
from src.core.device.components.power_device import PowerDevice

class TestPowerDevice(unittest.TestCase):
    def setUp(self):
        self.device = PowerDevice(name="TestDevice")

    def test_initial_state(self):
        self.assertEqual(self.device.power_consumption, 0)
        self.assertEqual(self.device.total_energy, 0)
        self.assertIsNone(self.device.last_update_time)

    def test_report_power(self):
        self.device.report_power(100)
        self.assertEqual(self.device.power_consumption, 100)

    def test_update_energy(self):
        self.device.report_power(100)
        self.device.last_update_time = time.time() - 3600  # Simulate 1 hour ago
        self.device.update_energy()
        self.assertAlmostEqual(self.device.total_energy, 0.1, places=4)

    def test_get_energy(self):
        self.device.report_power(100)
        self.device.last_update_time = time.time() - 3600  # Simulate 1 hour ago
        energy = self.device.get_energy()
        self.assertAlmostEqual(energy, 0.1, places=4)

if __name__ == "__main__":
    unittest.main()