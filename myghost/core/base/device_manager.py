from myghost.core.base.device import Device


class DeviceManager:
    def __init__(self):
        self.device_dict: dict[int, Device] = {}

    def add_device(self, device: Device):
        """Add new connected to device to device dict."""
        self.device_dict.update({self.generate_next_id(): device})

    def remove_device(self, device_id: int):
        self.device_dict.pop(device_id)

    def generate_next_id(self):
        return len(self.device_dict)

    @property
    def devices(self) -> dict[int, Device]:
        return self.device_dict


def main():
    manager = DeviceManager()
    manager.add_device(Device("10.10.10.10"))
    manager.add_device(Device("10.10.10.1"))
    print(manager.devices)
    manager.remove_device(1)
    print(manager.devices)


if __name__ == '__main__':
    main()
