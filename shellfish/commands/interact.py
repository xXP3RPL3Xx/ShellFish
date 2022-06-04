# from shellfish.core.db.database import Database, database_entry_to_device
from shellfish.lib.command import Command, CommandInfo
from shellfish.core.base.device_manager import BorgDeviceManager


class MyGhostCommand(Command):
    """Connect to a Android device."""

    def __init__(self) -> None:
        super().__init__(CommandInfo("interact", "interact <id>", "Interact with device."))
        self.device = None
        self.device_manager = BorgDeviceManager()

    def check_arguments(self, arguments: list[str]):
        match arguments:
            case [device_id]:
                """Interact with device"""
                try:
                    self.device = self.device_manager.get_device_by_id(int(device_id))
                    if self.device:
                        self.device.interact()

                    else:
                        self.print_error(f"No device with id: {device_id}")

                except ValueError:
                    self.print_error(f"Invalid id: {device_id}")

            case _:
                self.print_usage()

    def run(self, arguments: list[str]):
        """Connect to the device with the given ip."""
        self.check_arguments(arguments)
