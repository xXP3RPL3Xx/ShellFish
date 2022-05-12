from myghost.lib.command import Command, CommandInfo


class MyGhostCommand(Command):
    def __init__(self):
        super().__init__(CommandInfo("disconnect", "disconnect <device id>",
                                     "Disconnects the device with corresponding id."))

    def run(self, *args, **kwargs) -> None:
        """Disconnects device with corresponding device id."""
