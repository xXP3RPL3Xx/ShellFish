from enum import Enum


class SpecialCharacter(Enum):
    """Enum for special characters."""

    END = '\033[0m'
    BOLD = '\033[1m'
    DARK = '\033[2m'
    BENT = '\033[3m'
    LINE = '\033[4m'
    TWINK = '\033[5m'
    BACK = '\033[7m'

    REMOVE = '\033[1K\r'
    CLEAR = '\033[H\033[J'
    NEWLINE = '\n'
