"""A simple plugin loader."""

import importlib.util
import os

# myghost imports
from myghost.lib.plugin import Plugin


class Loader:
    """Responsible for loading all plugins."""

    def __init__(self) -> None:
        self.plugin_list: list = list()
        self.plugins_path: str = f"{os.path.dirname(__file__)}/../../plugins"

    def import_plugin(self, name: str) -> Plugin:
        """Imports a module given a name."""
        spec = importlib.util.spec_from_file_location(name, self.plugins_path + "/" + name)
        plugin = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(plugin)

        plugin = plugin.MyGhostPlugin()
        return plugin

    def load_plugins(self) -> None:
        """Load the plugins defined in the plugins list."""
        plugins = self.get_plugins()
        for plugin_name in plugins:
            plugin = self.import_plugin(plugin_name)
            plugin.initialize()
            self.plugin_list.append(plugin)

    def get_plugins(self):
        """Returns all plugins in the plugins path."""
        return [plug_file for plug_file in os.listdir(self.plugins_path) if self.check_is_plugin(plug_file)]

    @staticmethod
    def check_is_plugin(file_name: str):
        """Check whether a file_name is a plugin."""
        return file_name.endswith(".py") and file_name != "__init__.py"
