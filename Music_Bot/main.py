import os
import asyncio
import discord
from discord.ext import commands


prefix = "!"  # 접두사 설정
intents = discord.Intents.all()  # 서버 멤버의 정보나, 멤버 리스트를 불러올 수 있도록 허용

client = commands.Bot(command_prefix=prefix, intents=intents)  # 봇 객체 생성


@client.event
async def on_ready():
    print("Success: Bot is connected to Discord")


async def load():
    for filename in os.listdir("./cogs"):  # cogs 디렉토리 내 파일 불러오기
        if filename.endswith(".py"):  # 파이썬 파일인 경우
            await client.load_extension(f"cogs.{filename[:-3]}")


async def main():
    with open("token.txt", "r", encoding="utf-8") as f:  # 토큰 불러오기
        token = f.read()

    async with client:
        await load()
        await client.start(token)


asyncio.run(main())
