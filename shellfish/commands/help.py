from shellfish.lib.command import Command, CommandInfo
from shellfish.core.base.loader import Loader
from shellfish.core.cli.tables import Tables


class MyGhostCommand(Command):
    def __init__(self):
        super().__init__(CommandInfo("help", "help", "Show this help menu"))
        self.loader = Loader()
        self.commands: list[Command] = []
        self.modules: list = []

    def check_arguments(self, arguments: list[str]):
        match arguments:
            case [name]:
                for command in Loader.command_list:
                    if name == command.name:
                        Tables.print_table(f"{name}", ("Help Information", "Usage"), *[(command.help, command.usage)])
                        return

                self.print_error(f"No command named: {name}.")
            case _:
                """Print help menu for all commands and modules."""
                self.command_help()
                self.module_help()

    def command_help(self):
        """Load help text from all available commands and print them."""
        self.commands: list[Command] = [command for command in self.loader.load_commands()]
        Tables.print_table("Commands", ('Command', 'Description'), *[(command.name, command.help)
                                                                     for command in self.commands])

    def module_help(self):
        self.modules = [module for module in self.loader.load_modules()]
        Tables.print_table("Modules", ('Module', 'Description'), *[(module.name, module.help)
                                                                   for module in self.modules])

    def run(self, arguments: list[str] = None) -> None:
        """Load help text from all available commands and print them."""
        self.check_arguments(arguments)
