"""A simple plugin loader."""

import importlib

# myghost imports
from myghost.lib.plugin import PluginInterface


class Loader:
    """Responsible for loading all plugins."""

    def __init__(self):
        pass

    def import_plugin(self, name: str) -> PluginInterface:
        return importlib.import_module(name)

    def load_plugins(self, plugins: list[str]) -> None:
        """Load the plugins defined in the plugins list."""
        for plugin_name in plugins:
            plugin = self.import_plugin(plugin_name)
            plugin.initialize()
