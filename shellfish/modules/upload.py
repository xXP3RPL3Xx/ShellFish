from shellfish.lib.module import Module, ModuleInfo
from shellfish.core.base.device import Device


class MyGhostModule(Module):
    """Show device battery information."""

    def __init__(self) -> None:
        super().__init__(ModuleInfo("battery", "battery", needs_root=False, help_text="Get battery information."))

    def run(self, device: Device, arguments: list[str] = None):
        self.print_process("Getting battery information...")

        output = device.send_command("dumpsys battery")
        self.print_empty(output)
