import os
from os import path
import platform
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from uuid import uuid4
from pyautogui import (confirm, alert)

class WebDriverBot(Chrome):
    def __init__(self,
                 executable_path: str = None,
                 temp_download_path: str = None,
                 enable_log: bool = False):
        """
        WebDriverBot constructor returns a WebDriverBot instance.
        The WebDriverBot is an inheritance of Selenium Chrome Driver
        :param executable_path:
        :param temp_download_path:
        :param enable_log:
        """

        self.enable_log = enable_log

        super().__init__(executable_path=self.__web_driver_path(web_driver_path=executable_path),
                         options=self.__web_driver_bot_config(temp_download_folder_path=temp_download_path),
                         service_log_path=self.__get_log_path)
        self.implicitly_wait(10)

    @property
    def __get_log_path(self):
        if not self.enable_log:
            return None
        log_path = path.join(path.abspath(""), "logs")
        if not path.isdir(log_path):

            os.mkdir(log_path)
        return path.join(log_path, f"log-{uuid4()}.txt")

    @staticmethod
    def __web_driver_path(web_driver_path: str = None) -> str:
        """
        Webdriver can be set passing path through param instead use the default value \n
        :param web_driver_path:
        :return : web driver path
        """
        if web_driver_path:
            return web_driver_path

        system_name = platform.system()

        web_driver_folder_path = path.join(path.abspath(""), "Drivers", system_name)

        if not path.isdir(web_driver_folder_path):
            raise Exception("Cannot found the driver folder.")

        drivers = os.listdir(web_driver_folder_path)

        if not len(drivers):
            raise Exception("Driver not found. Please download the driver or set the driver path")

        driver_name = drivers.pop()

        web_driver_path = path.join(web_driver_folder_path, driver_name)

        return web_driver_path

    @property
    def __get_temp_download_path(self) -> str:
        """
        :return: str with temp_download_path
        """
        temp_download_path = path.join(path.abspath(""), "tmp")

        return temp_download_path

    def __web_driver_bot_config(self, temp_download_folder_path: str = None, headless: bool = False) -> Options:
        """
        Set up all configs for WebDriver \n
        Temp download folder path can be set passing path through param instead use the default value
        \t - Download path
        :param temp_download_folder_path: str
        :param headless: bool
        :return: Options
        """

        if not temp_download_folder_path:
            temp_download_folder_path = self.__get_temp_download_path

        options = Options()
        options.headless = headless
        options.add_experimental_option("prefs", {
            "download.default_directory": temp_download_folder_path,
            "plugins.always_open_pdf_externally": True,
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing.enabled": True,
        })

        return options

    @staticmethod
    def confirm_pop_up(title: str = "Please confirm",
                       text: str = "Confirm?",
                       buttons: list = None):
        """

        :param title: str contains the title of pop-up
        :param text: str contains the text of pop-up
        :param buttons: str contains the buttons of pop-up
        :return: the text of button pressed
        """
        if not buttons:
            buttons = ["Confirm", "Cancel"]

        return confirm(text, title, buttons)

    @staticmethod
    def alert_pop_up(title: str = "Alert",
                     text: str = "Something went wrong",
                     button: str = "Ok"):
        """

        :param title: str contains the title of pop-up
        :param text: str contains the text of pop-up
        :param button: str contains the text of button
        :return: the text of button pressed
        """
        return alert(text, title, button)

    def __del__(self):
        self.close()
