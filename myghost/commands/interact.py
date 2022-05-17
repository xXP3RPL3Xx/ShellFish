from myghost.core.base.device_manager import DeviceManager
from myghost.lib.command import Command, CommandInfo


class MyGhostCommand(Command):
    """Connect to a Android device."""

    def __init__(self) -> None:
        super().__init__(CommandInfo("interact", "interact <id>", "Interact with device."))
        self.device = None

    def check_arguments(self, arguments: list[str]):
        match arguments:
            case [device_id]:
                """Interact with device"""
                try:
                    DeviceManager().devices[device_id].interact()

                except KeyError:
                    self.print_error(f"No device with id: {device_id}")
            case _:
                self.print_empty(f"Usage:{self.info.usage}")

    def run(self, arguments: list[str]):
        """Connect to the device with the given ip."""
        self.check_arguments(arguments)
