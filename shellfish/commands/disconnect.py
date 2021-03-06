from shellfish.lib.command import Command, CommandInfo
from shellfish.core.base.device_manager import BorgDeviceManager


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
                """Disconnect a single device with corresponding id."""
                self.disconnect_device(int(device_id))
            case _:
                """Wrong arguments"""
                self.print_usage()

    def disconnect_device(self, device_id: int):
        """Disconnect the device with the given device id."""
        device = self.device_manager.get_device_by_id(device_id)
        device.disconnect()
        self.device_manager.remove_device(device_id)

    def run(self, arguments: list[str] | None) -> None:
        """Disconnects device with corresponding device id."""
        self.check_arguments(arguments)
