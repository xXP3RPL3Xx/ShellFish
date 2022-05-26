from myghost.lib.command import Command, CommandInfo
from myghost.core.db.database import Database, database_entry_to_device
from myghost.core.base.device_manager import BorgDeviceManager


class MyGhostCommand(Command):
    def __init__(self):
        super().__init__(CommandInfo(name="disconnect",
                                     usage="disconnect <device id>",
                                     help_text="Disconnects the device with corresponding id."))

        self.device_manager = BorgDeviceManager()

    def check_arguments(self, arguments: list[str]):
        match arguments:
            case["all"]:
                """Disconnect all devices."""
                [self.disconnect_device(device_id) for device_id in self.device_manager.all_device_ids]

            case [device_id]:
                self.disconnect_device(device_id)
            case _:
                self.print_empty(self.info.usage)

    def disconnect_device(self, device_id: int):
        """Disconnect the device with the given device id."""
        device = self.device_manager.get_device_by_id(device_id)
        device.disconnect()
        self.device_manager.remove_device(device_id)

    def run(self, arguments: list[str]) -> None:
        """Disconnects device with corresponding device id."""
        self.check_arguments(arguments)


'''
class MyGhostCommand(Command):
    def __init__(self):
        super().__init__(CommandInfo(name="disconnect",
                                     usage="disconnect <device id>",
                                     help_text="Disconnects the device with corresponding id."))

        self.database = Database()

    def check_arguments(self, arguments: list[str]):
        match arguments:
            case["all"]:
                """Disconnect all devices."""
                [self.disconnect_device(device_id) for device_id in self.database.all_device_ids]

            case [device_id]:
                self.disconnect_device(device_id)
            case _:
                self.print_empty(self.info.usage)

    def disconnect_device(self, device_id: int):
        """Disconnect the device with the given device id."""
        entry = self.database.get_device_by_id(device_id)
        device = database_entry_to_device(entry)
        device.disconnect()
        self.database.remove_device(device_id)

    def run(self, arguments: list[str]) -> None:
        """Disconnects device with corresponding device id."""
        self.check_arguments(arguments)
'''