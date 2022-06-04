from shellfish.lib.command import Command, CommandInfo
from shellfish.core.cli.tables import Tables
from shellfish.core.base.device_manager import BorgDeviceManager


class MyGhostCommand(Command):
    """List all connected devices."""

    def __init__(self) -> None:
        super().__init__(CommandInfo("devices", "devices", "List all connected devices."))
        self.device_manager = BorgDeviceManager

    def run(self, arguments: list[str]):
        device_ids = [device_id for device_id in self.device_manager.connected_devices.keys()]
        device_hosts = [device.host for device in self.device_manager.connected_devices.values()]
        device_ports = [device.port for device in self.device_manager.connected_devices.values()]

        devices = [(device_id, host, port) for device_id, host, port in zip(device_ids, device_hosts, device_ports)]
        Tables.print_table("Connected devices", ("id", "host", "port"), *devices)
