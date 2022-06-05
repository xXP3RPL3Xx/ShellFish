import os

# shellfish imports
from shellfish.core.cli.badges import Badges


def exists(path: str):
    """Returns whether a file or directory exists."""
    if file_exists(path, quiet=True) or dir_exists(path, quiet=True):
        return True
    return False


def file_exists(file_path: str, quiet=False):
    """Returns whether a file exists."""
    if os.path.exists(file_path):
        if os.path.isdir(file_path):
            if not quiet:
                Badges.print_error(f"Error: {file_path}: not a file!")
            return False
        return True
    if not quiet:
        Badges.print_error(f"Local file: {file_path}: does not exist!")
    return False


def dir_exists(dir_path: str, quiet: bool = False) -> bool:
    """Returns whether a directory exists."""
    if os.path.exists(dir_path):
        if not os.path.isdir(dir_path):
            if not quiet:
                Badges.print_error(f"Error: {dir_path}: not a directory!")
            return False
        return True

    if not quiet:
        Badges.print_error(f"Local directory: {dir_path} does not exist!")
    return False


def main():
    print(file_exists("not_a_file"))
    print(dir_exists("not_a_directory"))


if __name__ == '__main__':
    main()
