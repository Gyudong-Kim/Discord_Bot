# 4. 메뉴 추천 Cog

import json
import random
from discord.ext import commands


class Menu(commands.Cog):
    def __init__(self, client):
        self.client = client

        with open("./data/menu.json", "r", encoding="utf-8") as f:
            self.menu_dict = json.load(f)

    @commands.Cog.listener()
    async def on_ready(self):
        print("Menu recommend Cog is Ready")

    @commands.command(name="메뉴추천")
    async def recommend_menu(self, ctx, arg=None):
        if arg is None:
            categories = list(self.menu_dict.keys())  # categories:["한식", "일식", ...]
            category = random.choice(categories)  # category: ex) "한식"
            menu = random.choice(self.menu_dict[category])  # menu: ex) "떡볶이"
            await ctx.send(f"'{category}' 중에서 '{menu}' 어떤가요?")
        else:
            category = arg
            menu = random.choice(self.menu_dict[category])
            await ctx.send(f"'{menu}' 어떤가요?")


async def setup(client):
    await client.add_cog(Menu(client))
