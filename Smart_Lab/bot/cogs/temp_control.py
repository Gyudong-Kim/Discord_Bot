import discord
from discord.ext import commands
import utils.temp_request as temp_request


class Temp(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Temp control Cog is Ready")

    @commands.command(name="냉난방기ON")
    async def power_on(self, ctx):
        r = temp_request.on_req()
        if r.status_code == 200:
            embed = discord.Embed(
                title="냉난방기 ON", description="냉난방기 전원을 켭니다.", color=discord.Color.red()
            )
            await ctx.send(embed=embed)

    @commands.command(name="냉난방기OFF")
    async def power_off(self, ctx):
        r = temp_request.off_req()
        if r.status_code == 200:
            embed = discord.Embed(
                title="냉난방기 OFF", description="냉난방기 전원을 끕니다.", color=discord.Color.red()
            )
            await ctx.send(embed=embed)

    @commands.command(name="냉난방기온도")
    async def set_temp(self, ctx, arg):
        r = temp_request.temp_req(arg)
        if r.status_code == 200:
            embed = discord.Embed(
                title="냉난방기 온도 설정",
                description=f"냉난방기 온도를 {arg}℃로 설정합니다.",
                color=discord.Color.blue(),
            )
            await ctx.send(embed=embed)

    @commands.command(name="냉난방기바람세기")
    async def set_flow(self, ctx, arg):
        r = temp_request.flow_req(arg)
        if r.status_code == 200:
            embed = discord.Embed(
                title="냉난방기 바람세기 설정",
                description=f"냉난방기 바람세기를 {arg}로 설정합니다.",
                color=discord.Color.blue(),
            )
            await ctx.send(embed=embed)

    @commands.command(name="냉난방기모드")
    async def set_mode(self, ctx, arg):
        r = temp_request.mode_req(arg)
        if r.status_code == 200:
            embed = discord.Embed(
                title="냉난방기 모드 설정",
                description=f"냉난방기 모드를 {arg}으로 설정합니다.",
                color=discord.Color.blue(),
            )
            await ctx.send(embed=embed)


async def setup(client):
    await client.add_cog(Temp(client))
