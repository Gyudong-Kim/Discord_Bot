import discord
from discord.ext import commands
from youtube_dl import YoutubeDL


class Music(commands.Cog):
    def __init__(self, client):
        options = {
            "format": "bestaudio/best",  # 고음질
            "noplaylist": True,  # 플레이리스트 없음
        }
        self.client = client
        self.DL = YoutubeDL(options)

    @commands.Cog.listener()
    async def on_ready(self):
        print("Music Cog is Ready")

    @commands.command(name="음악재생")
    async def play_music(self, ctx, url):
        # 봇이 음성 채널에 연결되어 있지 않으면
        if ctx.voice_client is None:
            # 명령어(ctx) 작성자(author)의 음성 채널에 연결 상태 확인
            if ctx.author.voice:
                await ctx.author.voice.channel.connect()
            else:
                embed = discord.Embed(
                    title="오류 발생",
                    description="음성 채널에 들어간 후 명령어를 사용해 주세요.",
                    color=discord.Color.red(),
                )
                await ctx.send(embed=embed)
                raise commands.CommandError("Author not connected to a voice channel.")
        # 봇이 음성 채널에 연결되어 있고, 재생 중이면
        elif ctx.voice_client.is_playing():
            # 현재 재생 중인 음악 종료
            ctx.voice_client.stop()

        await ctx.send(url)
        embed = discord.Embed(
            title="음악 재생",
            description="음악 재생을 준비하고 있어요. 잠시 기다려주세요.",
            color=discord.Color.red(),
        )
        await ctx.send(embed=embed)

        data = self.DL.extract_info(url, download=False)  # 음악 데이터 추출
        link = data["url"]
        title = data["title"]

        ffmpeg_options = {
            # 비디오를 사용하지 않음
            "options": "-vn",
            # ffmpeg에서 연결이 끊기는 경우, 재연결 시도
            # "before_options": "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5",
        }

        player = discord.FFmpegPCMAudio(
            link,
            **ffmpeg_options,
        )
        ctx.voice_client.play(player)

        embed = discord.Embed(
            title="음악 재생",
            description=f"{title} 재생을 시작합니다.",
            color=discord.Color.blue(),
        )
        await ctx.send(embed=embed)


async def setup(client):
    await client.add_cog(Music(client))
