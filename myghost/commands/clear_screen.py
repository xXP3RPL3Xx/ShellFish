from myghost.lib.command import Command
from myghost.core.cli.special_character import SpecialCharacter


class MyGhostCommand(Command):
    """Clear terminal screen (works only for linux)."""
    def run(self):
        self.print_empty(SpecialCharacter.CLEAR.value, end='')


def run():
    command = MyGhostCommand()

    command.run()
