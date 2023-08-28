import discord
from discord.ext import commands
import youtube_dl
import discord
import json

# Load the configuration file as you've done in your example
def load_config():
    with open('config.json') as file:
        return json.load(file)

config = load_config()
BOT_TOKEN = config['BOT_TOKEN']

# Define the bot and the command prefix
bot = commands.Bot(command_prefix='!')

# Command to play the provided YouTube video
@bot.command()
async def play(ctx, url):
    ctx.voice_client.stop()
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    YDL_OPTIONS = {'format':'bestaudio'}
    vc = ctx.voice_client

    with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
        info = ydl.extract_info(url, download=False)
        url2 = info['formats'][0]['url']
        source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)
        vc.play(source)

bot.run(BOT_TOKEN)