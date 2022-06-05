from shellfish.lib.module import Module, ModuleInfo
from shellfish.core.base.device import Device


class MyGhostModule(Module):
    """Show device battery information."""

    def __init__(self) -> None:
        super().__init__(ModuleInfo(name="download",
                                    usage="download <remote_file> <local_path>",
                                    needs_root=False,
                                    help_text="Get battery information."))

    def match_arguments(self, device: Device, arguments: list[str]) -> None:
        match arguments:
            case [device_path, output_path]:
                device.download_file(device_path, output_path)
            case _:
                self.print_usage()

    def run(self, device: Device, arguments: list[str] = None):
        self.match_arguments(device, arguments)
