# 3. Cog (ping pong)

from discord.ext import commands


class Example(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("example Cog is Ready")

    @commands.command(name="ping")
    async def _ping(self, ctx):
        await ctx.send("pong!")


async def setup(client):
    await client.add_cog(Example(client))
