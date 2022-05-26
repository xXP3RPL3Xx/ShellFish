"""A simple plugin loader."""
import importlib.util
import os

# myghost imports
from myghost.lib.plugin import Plugin
from myghost.lib.command import Command
from myghost.lib.module import Module
from myghost.core.cli.badges import Badges


class Loader:
    """Responsible for loading all commands and plugins."""

    def __init__(self) -> None:
        self.plugin_list: list = []
        self.plugin_path: str = f"{os.path.dirname(__file__)}/../../plugins"

        self.command_list: list = []
        self.command_path: str = f"{os.path.dirname(__file__)}/../../commands"

        self.module_list: list = []
        self.module_path: str = f"{os.path.dirname(__file__)}/../../modules"

    def load_all(self) -> list:
        """Load all available commands (built-in and plugin commands)."""
        self.load_commands()
        self.load_modules()

        return self.command_list + self.module_list

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
        """Import a command given its filename."""
        try:
            spec = importlib.util.spec_from_file_location(name, self.command_path + "/" + name)
            command = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(command)
            command = command.MyGhostCommand()

            return command

        except Exception as err:
            Badges.print_error(f"Cannot import module {name}. Reason: {err}")

    def import_module(self, name: str) -> Module:
        """Import a module given it's filename."""
        try:
            spec = importlib.util.spec_from_file_location(name, self.module_path + "/" + name)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            module = module.MyGhostModule()

            return module

        except Exception as err:
            Badges.print_error(f"Cannot import module {name}. Reason: {err}")

    def load_plugins(self) -> list[Plugin]:
        """Load the plugins defined in the plugins list."""
        for plugin_name in self.get_plugin_files():
            plugin = self.import_plugin(plugin_name)
            self.plugin_list.append(plugin)

        return self.plugin_list

    def load_commands(self) -> list[Command]:
        """Load the commands defined in the command list."""
        for command_name in self.get_command_files():
            command = self.import_command(command_name)
            self.command_list.append(command)

        return self.command_list

    def load_modules(self) -> list[Module]:
        """Load the modules defined in the module list."""
        for module_name in self.get_module_files():
            module = self.import_module(module_name)
            self.module_list.append(module)

        return self.module_list

    def get_plugin_files(self):
        """Returns all plugins in the plugins path."""
        return [plug_file for plug_file in os.listdir(self.plugin_path)
                if self.check_is_plugin(plug_file)]

    def get_command_files(self):
        """Returns all commands in the commands path."""
        return [command_file for command_file in os.listdir(self.command_path)
                if self.check_is_command(command_file)]

    def get_module_files(self):
        """Returns all commands in modules path."""
        return [module_file for module_file in os.listdir(self.module_path)
                if self.check_is_command(module_file)]

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
