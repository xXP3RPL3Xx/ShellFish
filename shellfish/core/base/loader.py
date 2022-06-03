"""A simple plugin loader."""
import importlib.util
import os

# shellfish imports
from shellfish.lib.command import Command
from shellfish.lib.module import Module
from shellfish.core.cli.badges import Badges


class Loader:
    """
    Responsible for loading all commands and plugins.
    Uses the Borg design pattern.
    """

    _shared_borg_state = {}
    command_list: list = []
    command_path: str = f"{os.path.dirname(__file__)}/../../commands"

    module_list: list = []
    module_path: str = f"{os.path.dirname(__file__)}/../../modules"

    def __new__(cls, *args, **kwargs):
        obj = super().__new__(cls, *args, **kwargs)
        obj.__dict__ = cls._shared_borg_state
        return obj

    def load_all(self) -> list[Command, Module]:
        """Load all available commands (built-in and plugin commands)."""
        self.load_commands()
        self.load_modules()

        return self.command_list + self.module_list

    def import_command(self, name: str) -> Command:
        """Import a command given its filename."""
        # return cached command if already imported.
        for cached_command in self.command_list:
            if cached_command.name == name:
                return cached_command
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
        # return cached module if already imported.
        for cached_module in self.module_list:
            if cached_module.name == name:
                return cached_module

        try:
            spec = importlib.util.spec_from_file_location(name, self.module_path + "/" + name)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            module = module.MyGhostModule()

            return module

        except Exception as err:
            Badges.print_error(f"Cannot import module {name}. Reason: {err}")

    def load_commands(self) -> list[Command]:
        """Load the commands defined in the command list."""
        for command_file in self.get_command_files():
            command = self.import_command(command_file)
            if not self.command_cached(command):
                self.command_list.append(command)

        return self.command_list

    def load_modules(self) -> list[Module]:
        """Load the modules defined in the module list."""
        for module_file in self.get_module_files():
            module = self.import_module(module_file)
            if not self.module_cached(module):
                self.module_list.append(module)

        return self.module_list

    def get_command_files(self):
        """Returns all commands in the commands path."""
        return [command_file for command_file in os.listdir(self.command_path)
                if self.check_is_command(command_file)]

    def get_module_files(self):
        """Returns all commands in modules path."""
        return [module_file for module_file in os.listdir(self.module_path)
                if self.check_is_command(module_file)]

    @staticmethod
    def check_is_command(file_name: str):
        """Check whether a file_name is a valid command"""
        return file_name.endswith(".py") and file_name != "__init__.py"

    def module_cached(self, module: Module):
        """Returns whether a module is already imported."""
        if module.name in [module.name for module in self.module_list]:
            return True
        return False

    def command_cached(self, command: Command):
        """Returns whether a command is already imported."""
        if command.name in [command.name for command in self.command_list]:
            return True
        return False


def main():
    loader = Loader()
    loader.load_commands()


if __name__ == '__main__':
    main()
