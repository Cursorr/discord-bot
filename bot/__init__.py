import discord
from discord.ext.commands import bot
import config
import os.path


class BasicBot(bot.Bot):
    def __init__(self, conf_path):
        if not os.path.exists(conf_path):
            os.makedirs(os.path.dirname(conf_path))
            self.config = config.JsonConfig(conf_path)

            # Setting up default config
            self.config.content["PREFIX"] = "!"  # Bot's prefix
            self.config.content["TOKEN"] = "Your token here"  # Bot's token
            self.config.content["JOIN_CHANNEL_ID"] = "Your join channel ID"  # Join channel ID (for welcomer)
            self.config.content["COGS"] = ["simple_cog"]  # List of cogs to load

            # Save default configuration
            self.config.write()
        else:
            self.config = config.load_json(conf_path)

        super().__init__(command_prefix=self.config.content["PREFIX"],
                         intents=discord.Intents.all())

        for cog in self.config.content["COGS"]:
            self.load_extension("bot.cogs." + cog)

    def start_bot(self):
        """
        Start the bot
        """

        super().run(self.config.content["TOKEN"])
