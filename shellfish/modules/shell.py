from shellfish.lib.module import Module, ModuleInfo
from shellfish.core.base.device import Device

from shellfish.core.cli.special_character import SpecialCharacter as SpChar


class MyGhostModule(Module):
    """Show device battery information."""

    def __init__(self) -> None:
        super().__init__(ModuleInfo(name="shell",
                                    usage="download <option>",
                                    needs_root=False,
                                    help_text="Send a command to device."))

    @staticmethod
    def match_arguments(device: Device, arguments: list[str]) -> None:
        match arguments:
            case ["-c", command]:
                device.send_command(command)

            case _:
                while True:
                    user_input: str = input(f'{SpChar.REMOVE}({device.host})> ')
                    device.send_command(user_input)

    def run(self, device: Device, arguments: list[str] = None):
        self.match_arguments(device, arguments)
