from myghost.lib.module import Module, ModuleInfo


class MyGhostModule(Module):
    """Show device battery information."""

    def __init__(self) -> None:
        super().__init__(ModuleInfo("battery", "battery"))

    def run(self, device, *args, **kwargs):
        print("Try to run battery")
        device.send_command("dumpsys battery")
