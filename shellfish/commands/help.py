from shellfish.lib.command import Command, CommandInfo
from shellfish.core.base.loader import Loader
from shellfish.core.cli.tables import Tables


class MyGhostCommand(Command):
    def __init__(self):
        super().__init__(CommandInfo("help", "help", "Show this help menu"))
        self.loader = Loader()
        self.commands: list[Command] = []
        self.modules: list = []

    def command_help(self):
        """Load help text from all available commands and print them."""
        self.commands: list[Command] = [command for command in self.loader.load_commands()]
        Tables.print_table("Commands", ('Command', 'Description'), *[(command.name, command.help)
                                                                     for command in self.commands])

    def module_help(self):
        self.modules = [module for module in self.loader.load_modules()]
        Tables.print_table("Modules", ('Module', 'Description'), *[(module.name, module.help)
                                                                   for module in self.modules])

    def run(self, *args, **kwargs) -> None:
        """Load help text from all available commands and print them."""
        self.command_help()
        self.module_help()
