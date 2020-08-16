import sys
from argparse import ArgumentParser
from os import path
import os
import importlib


class Runner:
    def __init__(self):
        __usage = """
runner <command> [<args>] 
Commands available:
    - generate
    - run 
"""
        parser = ArgumentParser(description="Entry point for all bots inside this folder.",
                                prog="NeuroTeks Bot CLI",
                                usage=__usage)

        parser.add_argument("command")
        command_args = parser.parse_args(sys.argv[1:2])

        if not hasattr(self, command_args.command):
            print('Unrecognized command')
            parser.print_help()
            exit(1)

        getattr(self, command_args.command)()

    @staticmethod
    def generate():
        parser = ArgumentParser("generator", usage="""
generate [<args>]
- All bots is created inside a "bots" folder
""")
        parser.add_argument("--bot_location",
                            "-bl",
                            type=str,
                            help="Bot folder related to the location of main.py",
                            dest="bot_location",
                            required=True)

        parser.add_argument("--bot_file_name",
                            "-bfn",
                            type=str,
                            dest="bot_file_name",
                            help="Name of the file containing the bot without .py",
                            required=True)

        parser.add_argument("--name",
                            "-n",
                            type=str,
                            help="Name of the class that refers to the bot",
                            dest="bot_name",
                            required=True,
                            default="Bot")

        args = parser.parse_args(sys.argv[2:])
        file_location = f"bots/{args.bot_location}"
        file = f"bots/{args.bot_location}/{args.bot_file_name}.py"

        if not path.isdir(file_location):
            os.makedirs(file_location)

        bot_class_name = args.bot_name
        class_as_string = f"""
from Core.web_driver_bot import WebDriverBot


class {bot_class_name}(WebDriverBot):
    def __init__(self, enable_log, temp_download_path, driver_path, bot_name):
        super().__init__(enable_log=enable_log,
                         temp_download_path=temp_download_path,
                         driver_path=driver_path,
                         bot_name=bot_name)
"""

        if not path.isfile(file_location):
            with open(file, "w") as file:
                file.write(f"".join(class_as_string))
                file.close()

    @staticmethod
    def run():
        parser = ArgumentParser("run", usage="""
        run [<args>]
        - All bots is created inside a "bots" folder
        """)

        parser.add_argument("--driver",
                            "-d",
                            type=str,
                            help="Absolute path of Chrome driver location",
                            dest='driver',
                            required=False,
                            default=None)

        parser.add_argument("--temp_download_folder",
                            "-tdf",
                            type=str,
                            help="Absolute path of temporary folder",
                            dest="temp_download_folder",
                            required=False)

        parser.add_argument("--log",
                            "-l",
                            type=bool,
                            help="Enable the activity log",
                            dest="logger",
                            required=False)

        parser.add_argument("--bot_location",
                            "-bl",
                            type=str,
                            help="Bot folder relative to the location of main.py",
                            dest="bot_location",
                            required=True)

        parser.add_argument("--bot_file_name",
                            "-bfn",
                            type=str,
                            dest="bot_file_name",
                            help="Name of the file containing the bot without .py",
                            required=True)

        parser.add_argument("--name",
                            "-n",
                            type=str,
                            help="Name of the class that refers to the bot",
                            dest="bot_name",
                            required=True,
                            default="Bot")

        arguments = parser.parse_args(sys.argv[2:])

        bot_location = str(path.sep).join([x for x in arguments.bot_location.split("/")])
        bot_location = f"bots{path.sep}{bot_location}{path.sep}{arguments.bot_file_name}"
        bot_import = bot_location.replace(path.sep, ".")
        bot_location = bot_location + ".py"

        enable_log = bool(arguments.logger)
        temp_path = bool(arguments.temp_download_folder)
        driver_path = bool(arguments.driver)
        bot_class_name = str(arguments.bot_name)
        module = importlib.import_module(bot_import)

        bot = getattr(module, bot_class_name)

        bot(enable_log=enable_log,
            temp_download_path=temp_path,
            driver_path=driver_path,
            bot_name=bot_class_name).run()
