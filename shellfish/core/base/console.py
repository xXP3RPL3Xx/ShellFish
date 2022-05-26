from abc import abstractmethod

# shellfish imports
from shellfish.core.base.loader import Loader
from shellfish.lib.command import Command
from shellfish.lib.module import Module


class Console:
    def __init__(self):
        self.loader = Loader()
        self.commands: dict[str, Command | Module] = {}

    def autocomplete(self, text, state) -> str | None:
        """Try to complete a user's input."""
        options: list[str] = [command_name for command_name in self.commands.keys() if command_name.startswith(text)]

        if state < len(options):
            return options[state]
        else:
            return None

    def load_commands(self) -> None:
        self.commands: dict[str, Command] = {command.name: command for command in self.loader.load_commands()}

    @abstractmethod
    def match_command(self, command_name: str, arguments: list[str]):
        """Match the command name with the right command."""

    @abstractmethod
    def shell(self):
        """Start shell"""
