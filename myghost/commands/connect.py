from myghost.core.base.device import Device
from myghost.lib.command import Command, CommandInfo
from myghost.core.cli.badges import Badges
from myghost.core.cli.special_character import SpecialCharacter


class MyGhostCommand(Command):
    """Connect to a Android device."""

    def __init__(self) -> None:
        super().__init__(CommandInfo("connect", "connect <ip address>", "Connect to device."))

    def check_arguments(self, arguments: list[str]):
        match arguments:
            case [host, port]:
                """Connect device"""
                # device = Device(host, port)
            case [host]:
                device = Device(host)
            case _:
                Badges.print_empty(self.info.usage)

        connected = device.connect()

    def run(self, arguments: list[str]):
        """Connect to the device with the given ip."""
        self.check_arguments(arguments)
