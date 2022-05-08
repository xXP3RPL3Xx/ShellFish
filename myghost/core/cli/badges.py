class Badges:
    @staticmethod
    def print_empty(message: str = "", end: str = '\n') -> None:
        print(f"\033[1K\r{message}", end=end)

    @staticmethod
    def print_process(message, end='\n'):
        print(f"\033[1K\r\033[1;34m[*]\033[0m {message}", end=end)

    @staticmethod
    def print_success(message, end='\n'):
        print(f"\033[1K\r\033[1;32m[+]\033[0m {message}", end=end)

    @staticmethod
    def print_error(message, end='\n'):
        print(f"\033[1K\r\033[1;31m[-]\033[0m {message}", end=end)

    @staticmethod
    def print_warning(message, end='\n'):
        print(f"\033[1K\r\033[1;33m[!]\033[0m {message}", end=end)

    @staticmethod
    def print_information(message, end='\n'):
        print(f"\033[1K\r\033[1;77m[i]\033[0m {message}", end=end)
