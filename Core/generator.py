import os


__class = """from Core.web_driver_bot import WebDriverBot


class {BotClassName}(WebDriverBot):
    def __init__(self, enable_log, temp_download_path, driver_path, bot_name):
        super().__init__(enable_log=enable_log,
                         temp_download_path=temp_download_path,
                         driver_path=driver_path,
                         bot_name=bot_name)

    def run(self):
        ...
"""


class Generator:
    def __init__(self, bot_name):
        pass
