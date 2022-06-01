from abc import abstractmethod

# shellfish imports
from shellfish.core.base.loader import Loader
from shellfish.lib.command import Command
from shellfish.lib.module import Module
from shellfish.core.cli.badges import Badges


class Console(Badges):
    """Represents a base console."""

    def __init__(self):
        self.loader = Loader()
        self.commands: dict[str, Command] = {}
        self.modules: dict[str, Module] = {}

    def autocomplete(self, text, state) -> str | None:
        """Try to complete a user's input."""
        options: list[str] = [command_name for command_name in self.commands.keys() if command_name.startswith(text)]

        if state < len(options):
            return options[state]
        else:
            return None

    def load_commands(self) -> None:
        """Load all commands."""
        self.commands: dict[str, Command] = {command.name: command for command in self.loader.load_commands()}

    def load_modules(self) -> None:
        """Load all modules."""
        self.modules: dict[str, Module] = {module.name: module for module in self.loader.load_modules()}

    def match_command(self, command_name: str, arguments: list[str], device=None):
        """Match the command name with the right command."""
        if command_name in self.commands.keys():
            self.commands[command_name].run(arguments)

        elif command_name in self.modules.keys():
            self.modules[command_name].run(device, arguments)

        else:
            self.print_error("Unrecognized command!")

    @abstractmethod
    def shell(self):
        """Start shell"""
