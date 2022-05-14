from myghost.lib.command import Command, CommandInfo
from myghost.core.cli.badges import Badges
from myghost.core.cli.special_character import SpecialCharacter


class MyGhostCommand(Command):
    """List all connected devices."""

    def __init__(self) -> None:
        super().__init__(CommandInfo("devices", "devices", "List all connected devices."))

    def run(self, *args, **kwargs):
        Badges.print_empty("Connected devices: ")
