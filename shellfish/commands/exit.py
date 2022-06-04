import sys

# from shellfish.commands
from shellfish.lib.command import Command, CommandInfo
from shellfish.commands.clear_screen import MyGhostCommand as Clear
from shellfish.commands.disconnect import MyGhostCommand as Disconnect


class MyGhostCommand(Command):
    def __init__(self):
        super().__init__(CommandInfo("exit", "exit", "Disconnect all connected devices and exit session."))

    @staticmethod
    def clean_up():
        """Do the cleanup."""
        Disconnect().run(["all"])
        Clear().run()

    def run(self) -> None:
        self.clean_up()
        sys.exit(0)
