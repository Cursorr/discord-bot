from bot import BasicBot

if __name__ == '__main__':
    bot = BasicBot("config.json")  # Create new instance of a bot with his config
    bot.start_bot()  # Run the bot
