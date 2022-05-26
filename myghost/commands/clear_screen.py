from myghost.lib.command import Command, CommandInfo
from myghost.core.cli.special_character import SpecialCharacter


class MyGhostCommand(Command):
    """Clear terminal screen (works only for linux)."""
    
    def __init__(self) -> None:
        super().__init__(CommandInfo("clear", "clear", "Clear terminal screen"))

    def run(self, *args, **kwargs):
        self.print_empty(SpecialCharacter.CLEAR, end='')
