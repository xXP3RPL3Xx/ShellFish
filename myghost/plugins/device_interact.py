from dataclasses import dataclass

# myghost imports
from myghost.lib.plugin import Plugin, PluginInfo
from myghost.lib.command import Command, CommandInfo
from myghost.core.base.device import Device


@dataclass
class MyGhostPluginInfo(PluginInfo):
    """Separates plugin information from class."""

    def __init__(self):
        self.name = "Device Commands Plugin"
        self.version = "1.0"
        self.description = "Collection of commands."
        self.usage = "battery."
        self.needs_root = False


class MyGhostPlugin(Plugin):
    """Show device battery information."""

    def __init__(self):
        super().__init__(MyGhostPluginInfo())
        self.commands: dict[str, Command] = {}

    def initialize(self) -> None:
        """Initialize the plugin."""

    def load_commands(self):
        self.commands = {"battery": MyGhostCommand()}
        return self.commands

    def run(self) -> None:
        """Show device battery information."""
        print("run plugin ...")


class MyGhostCommand(Command):
    """Show device battery information."""

    def __init__(self) -> None:
        super().__init__(CommandInfo("battery", "battery", "Show device battery information."))

    def run(self, device: Device):
        device.send_command("dumpsys battery")
