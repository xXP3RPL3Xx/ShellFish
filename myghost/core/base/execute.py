class Executer:
    @staticmethod
    def execute_command(command, *args, **kwargs):
        command.run(*args, **kwargs)

    def execute_core_command(self):
        """Execute a built-in command."""

    def execute_plugin_command(self):
        """Execute a plugin command."""
