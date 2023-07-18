import discord
from discord.ext import commands #module in Discord.py library
import requests
import json
from intents import get_intents

bot = commands.Bot(command_prefix='!', intents=get_intents())  # Pass the intents argument

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
    if ctx.voice_client is None:

bot.run(BOT_TOKEN)