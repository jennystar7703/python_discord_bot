import discord
from discord.ext import commands #module in Discord.py library
import requests
import json

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='.', intents=discord.Intents.all())  # Pass the intents argument

# json 파일에서 config.json 정보 가줘오기
def load_config():
    with open('config.json') as file:
        return json.load(file)
    
config = load_config()
BOT_TOKEN = config['BOT_TOKEN']

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')

@bot.command()
async def join(ctx):
    if ctx.author.voice is None or ctx.author.voice.channel is None:
        await ctx.send("You are not connected to a voice channel.")
        return
    
    voice_channel = ctx.author.voice.channel
    if ctx.voice_client is None:
        await voice_channel.connect()
    else:
        await ctx.voice_client.move_to(voice_channel)

@bot.command 
async def leave(ctx):
    if ctx.voice_client is not None:
        await ctx.voice_client.disconnect()
    else:
        await ctx.send("I'm not in a voice channel!")

# Command definition
@bot.command()
async def hello(ctx):
    print("Hello command received")  # Debugging line
    await ctx.send('Hello, I am your friendly Discord bot!')

@bot.command()
async def play(ctx, url):
    ctx.voice_client.stop()
    
bot.run(BOT_TOKEN) 