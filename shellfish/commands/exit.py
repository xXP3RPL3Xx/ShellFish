import sys

# from shellfish.commands
from shellfish.lib.command import Command, CommandInfo
from shellfish.commands.clear_screen import MyGhostCommand as Clear
from shellfish.commands.disconnect import MyGhostCommand as Disconnect


class MyGhostCommand(Command):
    def __init__(self):
        super().__init__(CommandInfo("exit", "exit", "Disconnect all connected devices and exit session."))

    def clean_up(self):
        """Do the cleanup."""

    def run(self, *args, **kwargs) -> None:
        Disconnect().run(["all"])
        Clear().run()
        sys.exit(0)

