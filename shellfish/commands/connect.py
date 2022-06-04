from shellfish.core.base.device import Device
from shellfish.lib.command import Command, CommandInfo
from shellfish.core.base.device_manager import BorgDeviceManager


class MyGhostCommand(Command):
    """Connect to an Android device via Android Debug Bridge(ADB)."""

    def __init__(self) -> None:
        super().__init__(CommandInfo("connect", "connect <ip address>", "Connect to device."))
        self.device_manager = BorgDeviceManager()

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
                self.print_usage()

    def connect(self, host: str, port: int = None):
        if port:
            device = Device(host, port)
        else:
            device = Device(host)

        connected = device.connect()
        if connected:
            self.device_manager.add_device(device)

    def run(self, arguments: list[str]):
        """Connect to the device with the given ip."""
        self.check_arguments(arguments)
