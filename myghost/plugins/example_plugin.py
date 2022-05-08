from myghost.lib.plugin import Plugin, PluginInfo
from dataclasses import dataclass


@dataclass
class MyGhostPluginInfo(PluginInfo):
    name = "Example Plugin"
    version = "version"
    description = "description"
    usage = "There is no usage."
    needs_root = False


class MyGhostPlugin(Plugin):
    def __init__(self):
        super(MyGhostPlugin, self).__init__(MyGhostPluginInfo)

    def initialize(self) -> None:
        """Initialize the plugin."""

    def run(self):
        print("run plugin ...")
