import discord
from discord.ext import commands
import utils.humidity_request as humidity_request


class Humidity(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Humidity control Cog is Ready")

    @commands.command(name="가습기ON")
    async def power_on(self, ctx):
        r = humidity_request.on_req()
        if r.status_code == 200:
            embed = discord.Embed(
                title="가습기 ON", description="가습기 전원을 켭니다.", color=discord.Color.red()
            )
            await ctx.send(embed=embed)

    @commands.command(name="가습기OFF")
    async def power_off(self, ctx):
        r = humidity_request.off_req()
        if r.status_code == 200:
            embed = discord.Embed(
                title="가습기 OFF", description="가습기 전원을 끕니다.", color=discord.Color.red()
            )
            await ctx.send(embed=embed)

    @commands.command(name="가습기습도")
    async def set_temp(self, ctx, arg):
        r = humidity_request.humidity_req(arg)
        if r.status_code == 200:
            embed = discord.Embed(
                title="가습기 습도 설정",
                description=f"가습기 습도를 {arg}%로 설정합니다.",
                color=discord.Color.blue(),
            )
            await ctx.send(embed=embed)


async def setup(client):
    await client.add_cog(Humidity(client))
