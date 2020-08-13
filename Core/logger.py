import colorama
from colorama import Fore


class Logger:
    @staticmethod
    def log(msg: str, location: str = "LOGGER"):
        """
        Colorized print on console
        :param msg: text
        :param location: alias for location of call
        :return: None
        """
        colorama.init(autoreset=True)
        print(f"[{location}]: {msg}")

    @staticmethod
    def error(msg: str, location: str = "LOGGER"):
        """
        Colorized print on console
        :param msg: text
        :param location: alias for location of call
        :return: None
        """
        colorama.init(autoreset=True)
        print(Fore.RED + f"[{location}]: {msg}")

    @staticmethod
    def warn(msg: str, location: str = "LOGGER"):
        """
        Colorized print on console
        :param msg: text
        :param location: alias for location of call
        :return: None
        """
        colorama.init(autoreset=True)
        print(Fore.YELLOW + f"[{location}]: {msg}")


if __name__ == '__main__':
    Logger.error("error")
    Logger.log("log")
    Logger.warn("warn")
