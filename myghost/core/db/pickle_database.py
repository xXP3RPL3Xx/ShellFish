import pickle

from myghost.core.base.device import Device


def serialize(device: Device, file_path) -> None:
    """Serialize a device object."""
    with open(file_path, "wb") as f:
        pickle.dump(device, f)


def deserialize(file_path) -> Device:
    """Deserialize a device object."""
    with open(file_path, "rb") as f:
        return pickle.load(f)


class PickleDataBase:
    def __init__(self):
        self.db_path = "pickle_db.pickle"
        self.connected_devices: dict[int, Device] = {}

    def save_device(self, device: Device) -> None:
        """Add device to DB."""
        serialize(device, self.db_path)

    def load_device(self):
        """Deserialize """
        self.connected_devices.update({len(self.connected_devices): deserialize(self.db_path)})

    def get_device_by_id(self, device_id: int):
        """Return device with matching id."""
        return self.connected_devices[device_id]


def main():
    pickle_db: PickleDataBase = PickleDataBase()
    pickle_db.save_device(Device("10.10.10.10", 5555))


if __name__ == '__main__':
    main()
