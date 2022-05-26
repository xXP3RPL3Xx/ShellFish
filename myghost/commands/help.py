from myghost.lib.command import Command, CommandInfo
from myghost.core.base.loader import Loader
from myghost.core.cli.tables import Tables


class MyGhostCommand(Command):
    def __init__(self):
        super().__init__(CommandInfo("help", "help", "Show this help menu"))
        self.loader = Loader()
        self.commands: list[Command] = []

    def run(self, *args, **kwargs) -> None:
        """Load help text from all available commands and print them."""
        self.commands: list[Command] = [command for command in self.loader.load_commands()]
        Tables().print_table("Commands", ('Command', 'Description'),
                             *[(command.name, command.help) for command in self.commands])
