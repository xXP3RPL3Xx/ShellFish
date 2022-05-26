import sqlite3


def create_database(db_name: str) -> sqlite3.Cursor:
    """Create a database for all connected devices."""
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()

    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS connected_devices
                   ([device_id] INTEGER PRIMARY KEY, 
                    [device_ip] TEXT,
                    [device_port] INTEGER)
                   """)

    connection.commit()

    return cursor


def get_tables_by_db_name(db_name):
    """Get the first table name (indicated by index 0) from a database."""
    with sqlite3.connect(db_name) as connection:
        result = connection.execute("SELECT name FROM sqlite_master WHERE type='table'")
        return [name[0] for name in result.fetchall()]


def get_table_name(cursor):
    result = cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    return [name[0] for name in result.fetchall()]
