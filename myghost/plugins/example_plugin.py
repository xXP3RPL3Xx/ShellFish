from dataclasses import dataclass

# myghost imports
from myghost.lib.plugin import Plugin, PluginInfo


@dataclass
class MyGhostPluginInfo(PluginInfo):
    """Separates plugin information from class."""

    def __init__(self):
        self.name = "Example Plugin"
        self.version = "version"
        self.description = "description"
        self.usage = "There is no usage."
        self.needs_root = False


class MyGhostPlugin(Plugin):
    """An example implementation of a plugin."""

    def __init__(self):
        super().__init__(MyGhostPluginInfo())

    def initialize(self) -> None:
        """Initialize the plugin."""

    def run(self) -> None:
        """The run method has to be implemented in a subclass of plugin."""
        print("run plugin ...")
