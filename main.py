import discord
import json
import asyncio

from discord.ext import commands


with open("config.json", "r") as f:
    token = json.load(f)["token"]

EXTENTIONS = [
    "cogs.welcome"
]


class BasicBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!",
                         intents=discord.Intents.all(),
                         description="A Simple discord bot !")

        self.token = token

        for extention in EXTENTIONS:
            try:
                self.load_extension(extention)
                print("{} Loaded Successfully".format(
                    extention
                ))
            except Exception as e:
                print("Failed to load extention {}".format(
                    extention, type(e).__name__
                ))

    async def bot_presence(self):
        while True:
            await self.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"Hi there !"))
            await asyncio.sleep(120)

    async def on_ready(self):
        print("Bot ON")
        self.gamesLoop = asyncio.ensure_future(self.bot_presence())

    def run(self):
        super().run(self.token)


if __name__ == '__main__':
    bot = BasicBot()
    bot.run()