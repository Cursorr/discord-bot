import discord
from discord.ext import commands


class Welcome(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.color = 0xffffff

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(self.bot.config.content["JOIN_CHANNEL_ID"])
        embed = (discord.Embed(title="Welcome !",
                               color=self.color,
                               description=f"Welcome {member.mention}, we are now {member.guild.member_count} in the server !"))\
            .set_thumbnail(url=member.avatar_url)\
            .set_author(name=member.name, icon_url=member.avatar_url)\
            .set_footer(text="New join !", icon_url=self.bot.user.avatar_url)
        await channel.send(embed=embed)


def setup(bot):
    bot.add_cog(Welcome(bot))
