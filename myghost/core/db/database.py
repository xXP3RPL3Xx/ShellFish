import sqlite3
import functools

# ShellFish imports
from myghost.core.cli.badges import Badges
from myghost.core.base.device import Device
from myghost.core.db.setup_database import create_database, get_table_name, get_tables_by_db_name


class Database:
    """A sqlite3 database, which stores all connected devices."""

    def __init__(self, db_name="shellfish.db"):
        create_database(db_name)

        self.db_name: str = db_name
        self.device_table: str = get_tables_by_db_name(self.db_name)[0]

    @staticmethod
    def db_connection(func):
        """connection decorator for the database."""
        @functools.wraps(func)
        def _db_connect(*args, **kwargs):
            self = args[0]
            with sqlite3.connect(self.db_name) as connection:
                cursor = connection.cursor()
                result = func(cursor=cursor, *args, **kwargs)
                # connection.commit()
                return result

        return _db_connect

    @db_connection
    def execute_query(self, query: str, cursor=None) -> None:
        """'Execute the given query.'"""
        cursor.execute(query)

    @db_connection
    def read_query(self, query: str, cursor=None):
        """Return result of a query."""
        cursor.execute(query)
        result = cursor.fetchall()
        return result

    def add_device(self, device: Device) -> None:
        """Add the device to the database."""
        host, port = device.host, device.port
        self.execute_query(f"INSERT INTO {self.device_table}(device_ip, device_port) VALUES (\"{host}\", {port})")

    def remove_device(self, device_id: int):
        """Remove the device with the given id from the database."""
        self.execute_query(f"DELETE FROM connected_devices WHERE device_id = {device_id}")

    @property
    def connected_devices(self):
        """Get the corresponding device information."""
        return self.read_query("SELECT * FROM connected_devices ORDER BY device_id")

    @property
    def all_device_ids(self):
        """Get a list of all device ids."""
        all_ids = self.read_query("SELECT device_id FROM connected_devices")
        return [device_id[0] for device_id in all_ids]

    def get_device_by_id(self, device_id: int):
        try:
            entry = self.read_query(f"SELECT device_ip, device_port FROM {self.device_table} WHERE device_id = {device_id}")
            return entry[0]
        except IndexError:
            Badges().print_error(f"Device {device_id} not found.")


class InMemoryDataBase:
    """Database for all connected devices in memory."""
    def __init__(self, db_name=":memory:"):
        self.cursor = create_database(db_name)
        self.db_name: str = db_name
        self.device_table: str = get_table_name(self.cursor)[0]

    def execute_query(self, query: str) -> None:
        """'Execute the given query.'"""
        self.cursor.execute(query)

    def read_query(self, query: str):
        """Return result of a query."""
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return result

    def add_device(self, device: Device) -> None:
        """Add the device to the database."""
        host, port = device.host, device.port
        self.execute_query(f"INSERT INTO {self.device_table}(device_ip, device_port) VALUES (\"{host}\", {port})")

    def remove_device(self, device_id: int):
        """Remove the device with the given id from the database."""
        self.execute_query(f"DELETE FROM connected_devices WHERE device_id = {device_id}")

    @property
    def connected_devices(self):
        """Get the corresponding device information."""
        return self.read_query("SELECT * FROM connected_devices ORDER BY device_id")

    @property
    def all_device_ids(self):
        """Get a list of all device ids."""
        all_ids = self.read_query("SELECT device_id FROM connected_devices")
        return [device_id[0] for device_id in all_ids]


def database_entry_to_device(entry: list[str, int]):
    try:
        host, port = entry
        device = Device(host, port)
        device.connect()
        return device

    except TypeError:
        Badges().print_error("Device not in DB.")


def main():
    db = Database()
    db.add_device(Device('10.10.10.10', 4444))
    print(db.connected_devices)
    print(db.get_device_by_id(5))
    entry = db.get_device_by_id(5)
    device = database_entry_to_device(entry)
    #device.disconnect()


if __name__ == '__main__':
    main()
