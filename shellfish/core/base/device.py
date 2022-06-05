"""The Device class represents an Android device."""
import socket
import readline
from dataclasses import dataclass

from adb_shell.adb_device import AdbDeviceTcp
from adb_shell.exceptions import AdbConnectionError, TcpTimeoutException

# shellfish imports
import shellfish.utils.utils as utils
from shellfish.core.base.console import Console
from shellfish.core.cli.badges import Badges
from shellfish.core.cli.colors import Color
from shellfish.core.cli.special_character import SpecialCharacter as SpChar


@dataclass
class DeviceInfo:
    """Stores basic information about the device."""

    android_version: str = None
    is_rooted: bool = False


class Device:
    """Represents an Android device e.g. a Samsung phone."""

    def __init__(self, host: str, port: int = 5555, timeout=10) -> None:
        self.host: str = host
        self.port: int = port

        self.device = AdbDeviceTcp(self.host, self.port, default_transport_timeout_s=timeout)

        self.info = DeviceInfo()

    def connect(self) -> bool:
        """Connect to the device via TCP."""
        try:
            Badges.print_process(f"Connecting to {self.host}...")
            self.device.connect()
            return True

        except ConnectionRefusedError:
            Badges.print_error(f"Connection refused: Failed to connect to {self.host}!")

        except TimeoutError:
            Badges.print_error(f"Timeout Error: Failed to connect to {self.host}!")

        except TcpTimeoutException:
            Badges.print_error(f"TCP Timeout Error: Failed to connect to  {self.host}!")

        except socket.gaierror:
            Badges.print_error(f"Name or service {self.host} not known!")

    def disconnect(self):
        """Disconnect from the connected device."""
        self.device.close()

    def interact(self):
        """Interact with a connected device."""
        interact_console: DeviceConsole = DeviceConsole(self)
        interact_console.shell()

    def send_command(self, command: str) -> str | None:
        """Send command to connected device."""
        try:
            cmd_output: str = self.device.shell(command)
            return cmd_output

        except AdbConnectionError:
            Badges.print_error("Socket is not connected. Connect first to a device!")

        except TimeoutError:
            Badges.print_error(f"Timeout Error: Can't send command to {self.host}!")

        except TcpTimeoutException:
            Badges.print_error(f"Timeout Error: Can't send command to {self.host}!")

        return None

    def is_rooted(self) -> bool:
        """Returns whether a device is rooted or not."""
        responder = self.send_command('which su')
        if not responder or responder.isspace():
            return False
        return True

    def upload_file(self, locale_file: str, device_path: str) -> bool:
        """Upload a file to the connected device."""
        if utils.file_exists(locale_file):
            Badges.print_process(f"Uploading {locale_file}...")
            self.device.push(locale_file, device_path)

            Badges.print_process(f"Saving to {device_path}...")
            Badges.print_success(f"Saved to {device_path}!")
            return True
        return False

    def download_file(self, device_file_path: str, locale_output_path: str):
        """Downloads a file from the connected device."""
        Badges.print_process(f"Downloading {device_file_path} ...")
        exists, is_dir = utils.exists(locale_output_path), utils.dir_exists(locale_output_path)

        if exists:
            if is_dir:
                Badges.print_process(f"Downloading {device_file_path}...")
                self.device.pull(device_file_path, locale_output_path)

                Badges.print_process(f"Saving to {locale_output_path}...")
                Badges.print_success(f"Saved to {locale_output_path}!")

                return True
            else:
                Badges.print_error(f"{locale_output_path} is not a directory!")
        else:
            Badges.print_error(f"Remote file: {device_file_path}: does not exist!")
            return False

    @property
    def android_version(self):
        return self.info.android_version

    @android_version.setter
    def android_version(self, new_android_version: str):
        self.info.android_version = new_android_version

    def __repr__(self):
        return f"Device(IP={self.host}, PORT={self.port})"


class DeviceConsole(Console):
    """Represents the interactive session."""

    def __init__(self, device: Device):
        super().__init__()

        self.device = device
        self.session_active: bool = False

        self.arrow = Color.RED + "└──>" + SpChar.END
        self.arrow = str(" " + self.arrow)

    def autocomplete(self, text, state) -> str | None:
        """Try to complete a user's input."""
        options: list[str] = [command_name for command_name in (self.commands.keys() | self.modules.keys())
                              if command_name.startswith(text)]

        if state < len(options):
            return options[state]
        else:
            return None

    def shell(self) -> None:
        self.session_active = True
        # Load all available commands and modules with their names
        self.load_commands()
        self.load_modules()
        # cmd loop
        readline.parse_and_bind("tab: complete")
        readline.set_completer(self.autocomplete)
        # cmd loop
        Badges.print_empty("Interactive connection spawned.")
        Badges.print_empty("Type 'quit' to exit interactive shell.")
        while self.session_active:
            user_input: list[str] = input(f'{SpChar.REMOVE}{self.arrow}(INTERACTIVE)> ').split()
            command: str = user_input[0]
            arguments: list[str] = user_input[1:]
            # self.match_command(command, arguments)
            if command == "quit":
                self.session_active = False
            else:
                if arguments:
                    self.match_command(command, arguments, self.device)
                else:
                    self.match_command(command, device=self.device)


def main():
    device = Device("0.0.0.0")
    device.name = "Sasha"
    device.android_version = "Oreo"

    device.connect()
    device.send_command("command")

    print(device.name, device.android_version)


if __name__ == '__main__':
    main()
