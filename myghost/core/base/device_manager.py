from myghost.core.base.device import Device


class DeviceManager:
    def __init__(self):
        self.connected_devices: dict[int, Device] = {}
        self.serialized_devices = None

    def add_device(self, host: str, port: int = 5555):
        """Add new connected to device to device dict."""
        device = self._connect_device(host, port)
        self.connected_devices.update({self.generate_next_id(): device})

    def remove_device(self, device_id: int):
        self._disconnect_device(device_id)
        self.connected_devices.pop(device_id)

    def generate_next_id(self):
        return len(self.connected_devices)

    def load_device(self):
        pass

    @staticmethod
    def _connect_device(host: str, port: int):
        """Connect to a new device."""
        device = Device(host, port)
        connected = device.connect()
        if connected:
            return device

    def _disconnect_device(self, device_id: int):
        """Disconnect a device"""
        self.devices[device_id].disconnect()

    @property
    def devices(self) -> dict[int, Device]:
        return self.connected_devices


class BorgDeviceManager:
    _shared_borg_state = {}
    connected_devices: dict[int, Device] = {}

    def __new__(cls, *args, **kwargs):
        obj = super().__new__(cls, *args, **kwargs)
        obj.__dict__ = cls._shared_borg_state
        return obj

    def add_device(self, device: Device):
        """Add new connected to device to device dict."""
        self.connected_devices.update({self.generate_next_id(): device})

    def remove_device(self, device_id: int):
        self.connected_devices.pop(device_id)

    def generate_next_id(self):
        return len(self.connected_devices)

    def get_device_by_id(self, device_id: int) -> Device:
        try:
            return self.connected_devices[device_id]
        except KeyError:
            print(f"No device with id {device_id}")

    @property
    def devices(self) -> dict[int, Device]:
        return self.connected_devices

    @property
    def all_device_ids(self) -> list[int]:
        """Get a list of all device ids."""
        return [device_id for device_id in self.connected_devices.keys()]


def main():
    manager = BorgDeviceManager()
    manager.add_device(Device("10.10.10.0"))
    manager.add_device(Device("10.10.10.1"))
    manager2 = BorgDeviceManager()
    print(manager2.all_device_ids)


if __name__ == '__main__':
    main()
