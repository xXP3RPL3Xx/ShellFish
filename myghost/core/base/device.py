"""Simple representation of a mobile device"""
import socket

from adb_shell.adb_device import AdbDeviceTcp
from adb_shell.exceptions import AdbConnectionError

# myghost imports
from myghost.core.cli.badges import Badges


class Device:
    """Represents a device e.g. a Samsung phone."""

    def __init__(self, host, port: int = 5555, timeout=10) -> None:
        self.host = host
        self.port: int = port

        self.device = AdbDeviceTcp(self.host, self.port, default_transport_timeout_s=timeout)

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

    def interact(self):
        """Interact with a connected device."""
        Badges.print_success("Interactive connection spawned!")

        Badges.print_empty("")
        Badges.print_process("Loading device modules...")

    def send_command(self, command: str):
        """Send command to connected device."""
        try:
            self.device.shell(command)

        except AdbConnectionError:
            Badges.print_error("Socket is not connected. Connect first to a device!")

    def is_rooted(self) -> bool:
        """Returns whether a device is rooted or not."""


def main():
    device = Device("0.0.0.0")
    device.connect()
    device.send_command("command")


if __name__ == '__main__':
    main()
