import readline

# myghost imports
from myghost.core.base.device import Device
from myghost.core.base.execute import Executer
from myghost.core.base.loader import Loader
from myghost.core.cli.colors import Color
from myghost.core.cli.badges import Badges
from myghost.core.cli.tables import Tables
from myghost.core.cli.special_character import SpecialCharacter as SpChar
from myghost.lib.command import Command


class MainConsole:
    def __init__(self):
        self.commands: dict[str, Command] = dict()
        self.loader = Loader()
        self.executer: Executer = Executer()
        self.devices: dict[Device: int] = dict()
        self.banner = """{}{}
           .--. .-.               .-.
          : .--': :              .' `.
          : : _ : `-.  .--.  .--.`. .'
          : :; :: .. :' .; :`._-.': :
          `.__.':_;:_;`.__.'`.__.':_;

        --=[ {}Ghost Framework 1.0.0{}
        --=[ Developed by xXP3RPL3Xx
        """.format(SpChar.CLEAR.value, SpChar.END.value,
                   SpChar.BOLD.value + Color.WHITE.value,
                   SpChar.END.value, SpChar.LINE.value, SpChar.END.value)

    def autocomplete(self, text, state):
        """Try to complete a user's input."""
        options = [command_name for command_name in self.commands.keys() if command_name.startswith(text)]

        if state < len(options):
            return options[state]
        else:
            return None

    def match_command(self, command_name: str, arguments: list[str]):
        """Match the command name with the right command."""
        if command_name in self.commands.keys():
            self.commands[command_name].run(arguments)
        else:
            Badges.print_error("Unrecognized command!")

    def shell(self):
        # Print banner
        Badges.print_empty(self.banner)
        # Load all available commands and their names
        self.commands: dict[str, Command] = {command.name: command for command in self.loader.load_all()}
        # cmd loop
        readline.parse_and_bind("tab: complete")
        readline.set_completer(self.autocomplete)
        while True:
            user_input: list[str] = input(f'{SpChar.REMOVE.value}(myghost)> ').split()
            command: str = user_input[0]
            arguments: list[str] = user_input[1:]
            self.match_command(command, arguments)

    def show_help(self) -> None:
        """Print a basic help menu for available commands."""
        Tables().print_table("Commands", ('Command', 'Description'),
                             *[(command.name, command.help) for command in self.commands.values()])

    def _connect(self, arguments: list):
        """Connect to mobile device."""
        match arguments:
            case [host, port]:
                device = Device(host, port)
            case [host]:
                device = Device(host)
            case _:
                Badges.print_empty("Usage: connect <address>")
                return

        connected = device.connect()

        # Override the following block
        if connected:
            self.devices.update({device: Device.id})


class InteractConsole:
    """Represents the interactive session."""

    def __init__(self):
        self.session_active: bool = False

    def shell(self) -> None:
        self.session_active = True
        # cmd loop
        while self.session_active:
            command: str = input(f'{SpChar.REMOVE.value}(INTERACTIVE)> ')
            self.match_command(command)

    def match_command(self, command: str):
        match command.split():
            case ['help']:
                self.show_help()

            case ['exit']:
                self.exit_session()

            case ['clear']:
                self.clear_screen()

            case _:
                self.command_unrecognized()

    def exit_session(self) -> None:
        """Exit interactive session"""
        self.session_active = False

    @staticmethod
    def clear_screen():
        """Clear terminal screen (works only for linux)."""
        Badges.print_empty(SpChar.CLEAR.value, end='')

    @staticmethod
    def show_help() -> None:
        Tables().print_table("Core Commands", ('Command', 'Description'), *[
            ('clear', 'Clear terminal window.'),
            ('exit', 'Exit current device.'),
            ('help', 'Show available commands.')
        ])

    @staticmethod
    def command_unrecognized():
        Badges.print_error("Unrecognized command!")


def main():
    console = MainConsole()
    console.shell()


if __name__ == '__main__':
    main()
