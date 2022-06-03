from shellfish.lib.module import Module, ModuleInfo


class MyGhostModule(Module):
    """Show device battery information."""

    def __init__(self) -> None:
        super().__init__(ModuleInfo("info", "info <>", needs_root=False,
                                    help_text="Get information about android version, api and more."))

    def match_arguments(self, device, arguments: list[str]):
        match arguments:
            case ["extended"]:
                # All available information
                self.print_process("Getting advanced information...")
                advanced_info: str = device.send_command("getprop")
                self.print_empty("Advanced information: ")
                self.print_empty(advanced_info)

            case ["api"]:
                # API level information
                self.print_process("Getting Api level information...")
                api_info: str = device.send_command("getprop ro.build.version.sdk")
                self.print_empty("API level information: ")
                self.print_empty(api_info)

            case []:
                # Android version:
                self.print_process("Getting Android version information...")
                version: str = device.send_command("getprop ro.build.version.release")
                self.print_empty(f"Android version: {version}")

            case _:
                self.print_empty(self.info.usage)

    def run(self, device, arguments=None):
        self.match_arguments(device, arguments)
