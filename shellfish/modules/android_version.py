from shellfish.lib.module import Module, ModuleInfo
from shellfish.core.cli.badges import Badges


class MyGhostModule(Module):
    """Show device battery information."""

    def __init__(self) -> None:
        super().__init__(ModuleInfo("android", "android", needs_root=False))

    def run(self, device, *args, **kwargs):
        Badges.print_process("Getting Android version information...")
        # Android version:
        version: str = device.send_command("getprop ro.build.version.release")
        # API level
        info = device.send_command("getprop ro.build.version.sdk")
        all_info = device.send_command("getprop")
        Badges.print_empty(f"Android version: {version}\n"
                           f"Info: {info}\n"
                           f"All: {all_info}")
