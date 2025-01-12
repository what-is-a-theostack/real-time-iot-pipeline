import unittest
from core.device.base_device import BaseDevice

class TestBaseDevice(unittest.TestCase):
    def setUp(self):
        self.device = BaseDevice(
            manufacturer="TestManufacturer",
            make="TestMake",
            model="TestModel",
            serial_number="12345",
            name="TestDevice",
            description="Test Description"
        )

    def test_initialization(self):
        self.assertEqual(self.device.manufacturer, "TestManufacturer")
        self.assertEqual(self.device.make, "TestMake")
        self.assertEqual(self.device.model, "TestModel")
        self.assertEqual(self.device.serial_number, "12345")
        self.assertEqual(self.device.name, "TestDevice")
        self.assertEqual(self.device.description, "Test Description")
        self.assertEqual(self.device.status, "inactive")
        self.assertEqual(self.device.inputs, {})
        self.assertEqual(self.device.outputs, {})
        self.assertEqual(self.device.metadata, {})
        self.assertEqual(self.device.log, [])

    def test_activate(self):
        self.device.activate()
        self.assertEqual(self.device.status, "active")
        self.assertIn("TestDevice activated.", self.device.log)

    def test_deactivate(self):
        self.device.activate()
        self.device.deactivate()
        self.assertEqual(self.device.status, "inactive")
        self.assertIn("TestDevice deactivated.", self.device.log)

    def test_add_input(self):
        self.device.add_input("input1", "signal_type1")
        self.assertIn("input1", self.device.inputs)
        self.assertEqual(self.device.inputs["input1"], "signal_type1")
        self.assertIn("Input 'input1' (signal_type1) added.", self.device.log)

    def test_add_output(self):
        self.device.add_output("output1", "signal_type1")
        self.assertIn("output1", self.device.outputs)
        self.assertEqual(self.device.outputs["output1"], "signal_type1")
        self.assertIn("Output 'output1' (signal_type1) added.", self.device.log)

    def test_read_input(self):
        self.device.add_input("input1", "signal_type1")
        value = self.device.read_input("input1")
        self.assertEqual(value, "Simulated value from input1")
        self.assertIn("Read from input 'input1': Simulated value from input1", self.device.log)

    def test_read_input_nonexistent(self):
        with self.assertRaises(ValueError):
            self.device.read_input("nonexistent_input")

    def test_write_output(self):
        self.device.add_output("output1", "signal_type1")
        self.device.write_output("output1", "value1")
        self.assertIn("Wrote value 'value1' to output 'output1'.", self.device.log)

    def test_write_output_nonexistent(self):
        with self.assertRaises(ValueError):
            self.device.write_output("nonexistent_output", "value1")

    def test_reset(self):
        self.device.activate()
        self.device.add_input("input1", "signal_type1")
        self.device.add_output("output1", "signal_type1")
        self.device.update_metadata("key1", "value1")
        self.device.reset()
        self.assertEqual(self.device.status, "inactive")
        self.assertEqual(self.device.inputs, {})
        self.assertEqual(self.device.outputs, {})
        self.assertEqual(self.device.metadata, {})
        self.assertIn("TestDevice reset to initial state.", self.device.log)

    def test_get_info(self):
        info = self.device.get_info()
        self.assertEqual(info["manufacturer"], "TestManufacturer")
        self.assertEqual(info["make"], "TestMake")
        self.assertEqual(info["model"], "TestModel")
        self.assertEqual(info["serial_number"], "12345")
        self.assertEqual(info["name"], "TestDevice")
        self.assertEqual(info["description"], "Test Description")
        self.assertEqual(info["status"], "inactive")
        self.assertEqual(info["inputs"], {})
        self.assertEqual(info["outputs"], {})
        self.assertEqual(info["metadata"], {})
        self.assertEqual(info["log"], [])

    def test_update_metadata(self):
        self.device.update_metadata("key1", "value1")
        self.assertEqual(self.device.metadata["key1"], "value1")
        self.assertIn("Metadata updated: key1 = value1", self.device.log)

    def test_get_log(self):
        self.device.activate()
        log = self.device.get_log()
        self.assertIn("TestDevice activated.", log)

if __name__ == "__main__":
    unittest.main()