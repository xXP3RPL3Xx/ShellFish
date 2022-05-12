from myghost.lib.command import Command


class Executer:
    def execute(self, command, *args, **kwargs):
        if self.execute_core_command(command, args, kwargs):
            return None
        if self.execute_command(command, args, kwargs):
            return None
        if self.execute_plugin_command(command, args, kwargs):
            return None

    @staticmethod
    def execute_command(command: Command, *args, **kwargs):
        command.run(args)

    def execute_core_command(self, command: Command, *args, **kwargs):
        """Execute a built-in command."""

    def execute_plugin_command(self, command: Command, *args, **kwargs):
        """Execute a plugin command."""
