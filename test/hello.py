import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")  # 봇이 실행되면 콘솔창에 표시


@client.event
async def on_message(message):
    if message.author == client.user:  # 봇이 보내는 메시지는 무시
        return

    if message.content.startswith("$hello"):  # $hello 메시지가 채팅창에 전송되면
        await message.channel.send("Hello!")  # Hello! 메시지 전송


client.run("Token")
