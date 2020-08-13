from Core.web_driver_bot import WebDriverBot


if __name__ == '__main__':
    bot = WebDriverBot(enable_log=True)

    print(bot.alert_pop_up())
    print(bot.confirm_pop_up())
