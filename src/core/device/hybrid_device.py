from core.device.iot_device import IoTDevice
from core.device.legacy_device import LegacyDevice

class HybridDevice(IoTDevice, LegacyDevice):
    def __init__(self, *args, **kwargs):
        IoTDevice.__init__(self, *args, **kwargs)
        LegacyDevice.__init__(self, *args, **kwargs)
        self._log_event(f"{self.name} initialized as a hybrid device.")