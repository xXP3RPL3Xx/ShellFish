from shellfish.lib.module import Module, ModuleInfo
from shellfish.core.cli.badges import Badges


class MyGhostModule(Module):
    """Show device battery information."""

    def __init__(self) -> None:
        super().__init__(ModuleInfo("info", "info <>", needs_root=False))

    def match_arguments(self, device, arguments: list[str]):
        match arguments:
            case ["extended"]:
                # All available information
                Badges.print_process("Getting advanced information...")
                advanced_info: str = device.send_command("getprop")
                Badges.print_empty("Advanced information: ")
                Badges.print_empty(advanced_info)

            case ["api"]:
                # API level information
                Badges.print_process("Getting Api level information...")
                api_info: str = device.send_command("getprop ro.build.version.sdk")
                Badges.print_empty("API level information: ")
                Badges.print_empty(api_info)

            case []:
                # Android version:
                Badges.print_process("Getting Android version information...")
                version: str = device.send_command("getprop ro.build.version.release")
                Badges.print_empty(f"Android version: {version}")
                Badges.print_empty(version)

            case _:
                Badges.print_empty(self.info.usage)

    def run(self, device, arguments=None):
        self.match_arguments(device, arguments)
