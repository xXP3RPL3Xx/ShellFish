from shellfish.lib.module import Module, ModuleInfo


class MyGhostModule(Module):
    """Show device battery information."""

    def __init__(self) -> None:
        super().__init__(ModuleInfo("battery", "battery", needs_root=False))

    def run(self, device, *args, **kwargs):
        self.print_process("Getting battery information...")

        output = device.send_command("dumpsys battery")
        self.print_empty(output)
