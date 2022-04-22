"""A simple plugin loader."""

import importlib


class Loader:
    """Responsible for loading all plugins."""

    def __init__(self):
        pass

    def import_module(self, name: str) -> PluginInterface:
        return importlib.import_module(name)

    def load_plugins(self, plugins: list[str]) -> None:
        """Load the plugins defined in the plugins list."""
        for plugin_name in plugins:
            plugin = self.import_module(plugin_name)
            plugin.initialize()


class PluginInterface:
    """A plugin has a single function called initialize."""

    @staticmethod
    def initialize() -> None:
        """Initialize the plugin."""


