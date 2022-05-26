import readline

from shellfish.core.base.console import Console
from shellfish.lib.command import Command

from shellfish.core.cli.badges import Badges
from shellfish.core.cli.colors import Color
from shellfish.core.cli.special_character import SpecialCharacter as SpChar


class MainConsole(Console):
    def __init__(self):
        super().__init__()
        self.banner = """{}{}

         .--. .-.         .-.  .-.  .---.  _       .-.   
        : .--': :         : :  : :  : .--':_;      : :   
        `. `. : `-.  .--. : :  : :  : `;  .-. .--. : `-. 
         _`, :: .. :' '_.': :_ : :_ : :   : :`._-.': .. :
        `.__.':_;:_;`.__.'`.__;`.__;:_;   :_;`.__.':_;:_;


        --=[ {}ShellFish Framework 1.0.0{}
        --=[ Developed by xXP3RPL3Xx
        """.format(SpChar.CLEAR, SpChar.END,
                   SpChar.BOLD + Color.WHITE,
                   SpChar.END, SpChar.LINE, SpChar.END)

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
        self.commands: dict[str, Command] = {command.name: command for command in self.loader.load_commands()}
        # cmd loop
        readline.parse_and_bind("tab: complete")
        readline.set_completer(self.autocomplete)
        while True:
            user_input: list[str] = input(f'{SpChar.REMOVE}(shellfish)> ').split()
            command: str = user_input[0]
            arguments: list[str] = user_input[1:]
            self.match_command(command, arguments)
