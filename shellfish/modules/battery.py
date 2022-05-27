from shellfish.lib.module import Module, ModuleInfo
from shellfish.core.cli.badges import Badges


class MyGhostModule(Module):
    """Show device battery information."""

    def __init__(self) -> None:
        super().__init__(ModuleInfo("battery", "battery", needs_root=False))

    def run(self, device, *args, **kwargs):
        Badges.print_process("Getting battery information...")

        output = device.send_command("dumpsys battery")
        Badges.print_empty(output)
