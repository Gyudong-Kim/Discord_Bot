import discord
from discord.ext import commands
from youtube_dl import YoutubeDL
from .module.youtube import get_url


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
    async def play_music(self, ctx, *keywords):
        keyword = " ".join(keywords)
        url = get_url(keyword)
        print(f"Keyword : {keyword}")

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
            print("End music that was playing")

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
            "before_options": "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5",
        }

        player = discord.FFmpegPCMAudio(link, **ffmpeg_options)
        ctx.voice_client.play(player)

        embed = discord.Embed(
            title="음악 재생",
            description=f"{title} 재생을 시작합니다.",
            color=discord.Color.blue(),
        )
        await ctx.send(embed=embed)
        print(f"Play music : {title}")

    @commands.command(name="음악종료")
    async def quit_music(self, ctx):
        voice = ctx.voice_client
        if voice.is_connected():  # 음성 채널에 연결 중이면
            await voice.disconnect()  # 음성 채널 연결을 끊음
            embed = discord.Embed(
                title="", description="음악 재생을 종료합니다.", color=discord.Color.blue()
            )
            await ctx.send(embed=embed)
            print("End of music")

    @commands.command(name="일시정지")
    async def pause_music(self, ctx):
        voice = ctx.voice_client
        if voice.is_playing():  # 음악을 재생 중이면
            voice.pause()  # 음악 일시정지
            embed = discord.Embed(
                title="", description="음악 재생을 일시정지합니다.", color=discord.Color.blue()
            )
            await ctx.send(embed=embed)
            print("Pause the music")

    @commands.command(name="다시시작")
    async def resume_music(self, ctx):
        voice = ctx.voice_client
        if voice.is_paused():  # 음악이 일시정지되어 있으면
            voice.resume()  # 음악을 이어서 재생
            embed = discord.Embed(
                title="", description="일시정지된 음악을 이어서 재생합니다.", color=discord.Color.blue()
            )
            await ctx.send(embed=embed)
            print("Pause the music")


async def setup(client):
    await client.add_cog(Music(client))
