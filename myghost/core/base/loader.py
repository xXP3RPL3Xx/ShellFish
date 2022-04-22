"""A simple plugin loader."""

import importlib


class PluginInterface:
    """A plugin has a single function called initialize."""

    @staticmethod
    def initialize() -> None:
        """Initialize the plugin."""


def import_module(name: str) -> PluginInterface:
    return importlib.import_module(name)


def load_plugins(plugins: list[str]) -> None:
    """Load the plugins defined in the plugins list."""
    for plugin_name in plugins:
        plugin = import_module(plugin_name)
        plugin.initialize()
