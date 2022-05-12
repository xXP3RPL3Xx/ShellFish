"""A simple plugin loader."""

import importlib.util
import os

# myghost imports
from myghost.lib.plugin import Plugin
from myghost.lib.command import Command
from myghost.core.cli.badges import Badges


class Loader:
    """Responsible for loading all commands and plugins."""

    def __init__(self) -> None:
        self.plugin_list: list = []
        self.plugin_path: str = f"{os.path.dirname(__file__)}/../../plugins"

        self.command_list: list = []
        self.command_path: str = f"{os.path.dirname(__file__)}/../../commands"

    def load_all(self) -> list[Command]:
        """Load all available commands (built-in and plugin commands)."""
        self.load_commands()

        return self.command_list

    def import_plugin(self, name: str) -> Plugin:
        """Import a module given it's filename."""
        try:
            spec = importlib.util.spec_from_file_location(name, self.plugin_path + "/" + name)
            plugin = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(plugin)
            plugin = plugin.MyGhostPlugin()

            return plugin

        except Exception as err:
            Badges.print_error(f"Cannot import module {name}. Reason: {err}")

    def import_command(self, name: str) -> Command:
        """Import a module given it's filename."""
        try:
            spec = importlib.util.spec_from_file_location(name, self.command_path + "/" + name)
            command = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(command)
            command = command.MyGhostCommand()

            return command

        except Exception as err:
            Badges.print_error(f"Cannot import module {name}. Reason: {err}")

    def load_plugins(self) -> None:
        """Load the plugins defined in the plugins list."""
        for plugin_name in self.get_plugin_files():
            plugin = self.import_plugin(plugin_name)
            plugin.initialize()
            self.plugin_list.append(plugin)

    def load_commands(self) -> None:
        """Load the commands defined in the command list."""
        for command_name in self.get_command_files():
            command = self.import_command(command_name)
            self.command_list.append(command)

    def get_plugin_files(self):
        """Returns all plugins in the plugins path."""
        return [plug_file for plug_file in os.listdir(self.plugin_path)
                if self.check_is_plugin(plug_file)]

    def get_command_files(self):
        """Returns all commands in the commands path."""
        return [command_file for command_file in os.listdir(self.command_path)
                if self.check_is_command(command_file)]

    @staticmethod
    def check_is_plugin(file_name: str):
        """Check whether a file_name is a valid plugin."""
        return file_name.endswith(".py") and file_name != "__init__.py"

    @staticmethod
    def check_is_command(file_name: str):
        """Check whether a file_name is a valid command"""
        return file_name.endswith(".py") and file_name != "__init__.py"


def main():
    loader = Loader()
    loader.load_plugins()
    loader.load_commands()

    print(f"Loaded plugins: {loader.plugin_list}")
    print(f"Loaded commands: {loader.command_list}")


if __name__ == '__main__':
    main()
