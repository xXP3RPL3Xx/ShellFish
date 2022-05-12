import sys

# from myghost.commands
from myghost.lib.command import Command, CommandInfo
from myghost.commands.clear_screen import MyGhostCommand as Clear
from myghost.commands.disconnect import MyGhostCommand as Disconnect


class MyGhostCommand(Command):
    def __init__(self):
        super().__init__(CommandInfo("exit", "exit", "Disconnect all connected devices and exit session."))

    def run(self, *args, **kwargs) -> None:
        Disconnect().run()
        Clear().run()
        sys.exit(0)
