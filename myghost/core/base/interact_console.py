import readline

from myghost.lib.command import Command
from myghost.core.cli.badges import Badges
from myghost.core.cli.colors import Color
from myghost.core.cli.special_character import SpecialCharacter as SpChar
from myghost.core.base.device import Device
from myghost.core.base.console import Console


class InteractConsole(Console):
    """Represents the interactive session."""

    def __init__(self, device: Device):
        super().__init__()
        self.device = device
        self.session_active: bool = False

        self.arrow = Color.RED.value + "└──>" + SpChar.END.value
        self.arrow = str(" " + self.arrow)

    def shell(self) -> None:
        self.session_active = True
        # Load all available commands and modules with their names
        self.commands: dict[str, Command] = {command.name: command for command in self.loader.load_all()}
        # cmd loop
        readline.parse_and_bind("tab: complete")
        readline.set_completer(self.autocomplete)
        # cmd loop
        Badges.print_empty("Interactive connection spawned.")
        while self.session_active:
            user_input: list[str] = input(f'{SpChar.REMOVE.value}{self.arrow}(INTERACTIVE)> ').split()
            command: str = user_input[0]
            arguments: list[str] = user_input[1:]
            self.match_command(command, arguments)

    def match_command(self, command_name: str, arguments: list[str]):
        """Match the command name with the right command."""
        if command_name in self.commands.keys():
            self.commands[command_name].run(self.device, arguments)

        elif command_name in self.commands.keys():
            self.commands[command_name].run(self.device, arguments)

        else:
            Badges.print_error("Unrecognized command!")
