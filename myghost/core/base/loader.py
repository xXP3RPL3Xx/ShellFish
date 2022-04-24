"""A simple plugin loader."""

import importlib

# myghost imports
from myghost.lib.plugin import Plugin


class Loader:
    """Responsible for loading all plugins."""

    def import_plugin(self, name: str) -> Plugin:
        """Imports a module given a name."""
        return importlib.import_module(name)  # type: ignore

    def load_plugins(self, plugins: list[str]) -> None:
        """Load the plugins defined in the plugins list."""
        for plugin_name in plugins:
            plugin = self.import_plugin(plugin_name)
            plugin.initialize()
