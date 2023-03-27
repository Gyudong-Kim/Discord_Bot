# 1. 봇 실행

import discord
from discord.ext import commands


def main():
    prefix = "!"  # 접두사 설정
    intents = discord.Intents.all()  # 서버 멤버의 정보나, 멤버 리스트를 불러올 수 있도록 허용

    client = commands.Bot(command_prefix=prefix, intents=intents)  # 봇 객체 생성

    with open("token.txt", encoding="utf-8") as file:
        token = file.read()

    client.run(token)


if __name__ == "__main__":
    main()
