import sys

# myghost imports
from myghost.core.base.device import Device
from myghost.core.cli.colors import Color
from myghost.core.cli.badges import Badges
from myghost.core.cli.tables import Tables
from myghost.core.cli.special_character import SpecialCharacter as SpChar


class Console:
    def __init__(self):
        self.devices: dict = dict()
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

    def match_command(self, command: str):
        match command.split():
            case ['help']:
                self._help()

            case ['exit']:
                self._exit()

            case ['clear']:
                self._clear()

            case ['connect', host, port]:
                self._connect(host, port)

            case ['disconnect', *args]:
                self._disconnect()
            case _:
                self._command_unrecognized()

    def shell(self):
        # Print banner
        Badges.print_empty(self.banner)
        # cmd loop
        while True:
            command: str = input(f'{SpChar.REMOVE.value}(myghost)> ')
            self.match_command(command)

    @staticmethod
    def _help() -> None:
        print("Core commands:\n")
        print("help: show help menu")
        print("clear: clear screen")
        print("exit: exit myghost")

        Tables().print_table("Core Commands", ('Command', 'Description'), *[
            ('clear', 'Clear terminal window.'),
            ('connect', 'Connect device.'),
            ('devices', 'Show connected devices.'),
            ('disconnect', 'Disconnect device.'),
            ('exit', 'Exit Ghost Framework.'),
            ('help', 'Show available commands.'),
            ('interact', 'Interact with device.')
        ])

    def _exit(self):
        for device in list(self.devices):
            self.devices[device]['device'].disconnect()
            del self.devices[device]
        sys.exit(0)

    @staticmethod
    def _clear():
        """Clear terminal screen (works only for linux)."""
        Badges.print_empty(SpChar.CLEAR.value, end='')

    def _connect(self, arguments: list):
        """Connect to mobile device."""
        try:
            host, port = arguments
            device = Device(host, port)

        except ValueError:
            raise ValueError(f"Wrong input: {arguments}")

        connected = device.connect()

        if connected:
            self.devices.update({
                len(self.devices): {
                    'host': host,
                    'port': str(port),
                    'device': device
                }
            })

    def _disconnect(self, *args):
        raise NotImplementedError

    def _devices(self):
        raise NotImplementedError

    def _interact(self, *args):
        raise NotImplementedError

    @staticmethod
    def _command_unrecognized():
        Badges.print_error("Unrecognized command!")


def main():
    console = Console()
    console.shell()


if __name__ == '__main__':
    main()
