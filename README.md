# Aegaeon

Aegaeon is a lightweight library for web scraping developments with bots. 
Developed by NeuroTeks, the library consists of an implementation of the Selenium library using the Chrome driver.

All project is OOP for best reuse of modules inside a new bots.

---

## File Structure

```bash
.
├── Core
│   ├── generator.py
│   ├── __init__.py
│   ├── logger.py
│   ├── runner.py
│   └── web_driver_bot.py
├── Drivers
│   ├── Linux
│   │   └── chromedriver
│   └── Windows
│       └── chromedriver.exe
├── logs
│   └── log-BotGol_36d149fa-2b5f-4f4e-ba60-f76964d0fd66.txt
├── main.py
├── Pipfile
├── Pipfile.lock
├── README.md
└── test.py
```

---

### Dependencies

All dependencies below is necessary to project to work

- Chrome Web Browser
    - Version above 83


### Installation

Just need to clone the repository and install all dependencies inside you machine. You can use `pip`,
`venv`, `pipenv` or other python package manager.

```shell script
git clone https://github.com/Onmaedi/Aegaeon.git

pip install -r requirements
```

To maintain comfort, we left the browser driver inside the project. 

---

### A simple bot

All new bots go extend the WebDriverBot class

```python
from Core.web_driver_bot import WebDriverBot

class Bot(WebDriverBot):
    def __init__(self):
        super().__init__()
    
    def run(self):
        # all executions goes here
        # this method need to be implemented
        # run() is a default entry point of bot
        # it's called automatically for the `main.py`
        ...
```

---

## Generate Bot

Bots can be generated automatically from the command line.
Only by sending the necessary arguments for its creation.
```shell script
python main.py generate -n BotGol -bl test/new -bfn bot_go
```

### Run Bot

`main.py` is the default entry point for all bots, this file receives args for the name of the bot you want to run.

Some arguments are optional and can be passed to specify some settings

However, a new `.py` file can be created as the entry point for a specific bot, 
causing it to start differently if any additional configuration is needed.


```shell script
python main.py run -n BotGol -bl test/new -bfn bot_go
```

## Info
For help of usage of the available commands you can use `-h` for more information about commands
```shell script
python main.py -h
python main.py generate -h
```