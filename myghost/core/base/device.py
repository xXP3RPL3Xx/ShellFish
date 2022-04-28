"""The Device class represents an Android device."""
import socket
from dataclasses import dataclass

from adb_shell.adb_device import AdbDeviceTcp
from adb_shell.exceptions import AdbConnectionError

# myghost imports
from myghost.core.cli.badges import Badges
from myghost.core.base.loader import Loader


@dataclass
class DeviceInfo:
    """Stores basic information about the device."""

    name: str = None
    id: int = None
    android_version: str = None
    is_rooted: bool = False


class Device:
    """Represents a device e.g. a Samsung phone."""

    def __init__(self, host, port: int = 5555, timeout=10) -> None:
        self.host = host
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

        except socket.gaierror:
            Badges.print_error(f"Name or service {self.host} not known!")

    def disconnect(self):
        """Disconnect from the connected device."""
        self.device.close()

    @staticmethod
    def interact():
        """Interact with a connected device."""
        Badges.print_success("Interactive connection spawned!")
        Badges.print_empty("")
        Badges.print_process("Loading plugins...")

        # Load plugins here and available commands.
        plugins = None   # Update line!!!
        commands = None  # Update line!!!

        Badges.print_information(f"Plugins loaded: {None}")  # print loaded plugins here!

        # Start new Interact session.
        session_active: bool = True

        while session_active:
            command = input("Interactive Session> ")

            if command in commands:
                pass
                # execute proper command.
            # handle help, clear, exit

    def send_command(self, command: str):
        """Send command to connected device."""
        try:
            self.device.shell(command)

        except AdbConnectionError:
            Badges.print_error("Socket is not connected. Connect first to a device!")

    def is_rooted(self) -> bool:
        """Returns whether a device is rooted or not."""

    def upload_file(self, file_path: str):
        """Upload a file to the connected device."""

    def download_file(self, file_path: str):
        """Downloads a file from the connected device."""

    @property
    def name(self):
        return self.info.name

    @name.setter
    def name(self, new_name: str):
        self.info.name = new_name

    @property
    def id(self):
        return self.info.id

    @id.setter
    def id(self, new_id: int):
        self.info.id = new_id


def main():
    device = Device("0.0.0.0")
    device.id = 1
    device.name = "Sasha"

    device.connect()
    device.send_command("command")

    print(device.id)
    print(device.name)


if __name__ == '__main__':
    main()
