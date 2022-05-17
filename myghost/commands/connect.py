from myghost.core.base.device import Device
from myghost.lib.command import Command, CommandInfo
from myghost.core.base.device_manager import DeviceManager


class MyGhostCommand(Command):
    """Connect to an Android device via ADB Bridge."""

    def __init__(self) -> None:
        super().__init__(CommandInfo("connect", "connect <ip address>", "Connect to device."))

    def check_arguments(self, arguments: list[str]):
        match arguments:
            case [host, port]:
                """Connect to device with given ip and port"""
                try:
                    port = int(port)
                    self.connect(host, port)
                except ValueError:
                    self.print_error(f"Invalid port: {port}")

            case [host]:
                """Use default port."""
                self.connect(host)
            case _:
                self.print_empty(self.info.usage)

    def run(self, arguments: list[str]):
        """Connect to the device with the given ip."""
        self.check_arguments(arguments)

    @staticmethod
    def connect(host: str, port: int = None):
        if port:
            device = Device(host, port)
        else:
            device = Device(host)

        connected = device.connect()
        if connected:
            DeviceManager().add_device(device)
