import readline

# myghost imports
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
        self.banner = """{}{}
        
         .--. .-.         .-.  .-.  .---.  _       .-.   
        : .--': :         : :  : :  : .--':_;      : :   
        `. `. : `-.  .--. : :  : :  : `;  .-. .--. : `-. 
         _`, :: .. :' '_.': :_ : :_ : :   : :`._-.': .. :
        `.__.':_;:_;`.__.'`.__;`.__;:_;   :_;`.__.':_;:_;
                                                                                               
                                                                                               
        --=[ {}ShellFish Framework 1.0.0{}
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
            user_input: list[str] = input(f'{SpChar.REMOVE.value}(shellfish)> ').split()
            command: str = user_input[0]
            arguments: list[str] = user_input[1:]
            self.match_command(command, arguments)

    def show_help(self) -> None:
        """Print a basic help menu for available commands."""
        Tables().print_table("Commands", ('Command', 'Description'),
                             *[(command.name, command.help) for command in self.commands.values()])


class InteractConsole:
    """Represents the interactive session."""

    def __init__(self):
        self.session_active: bool = False
        self.commands: dict[str, Command] = dict()
        self.loader = Loader()

        self.arrow = Color.RED.value + "└──>" + SpChar.END.value
        self.arrow = str(" " + self.arrow)

    def autocomplete(self, text, state):
        """Try to complete a user's input."""
        options = [command_name for command_name in self.commands.keys() if command_name.startswith(text)]

        if state < len(options):
            return options[state]
        else:
            return None

    def shell(self) -> None:
        self.session_active = True
        # Load all available commands and their names
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
            self.commands[command_name].run(arguments)
        else:
            Badges.print_error("Unrecognized command!")


def main():
    console = MainConsole()
    console.shell()


if __name__ == '__main__':
    main()
