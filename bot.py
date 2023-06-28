import discord
from discord.ext import commands #module in Discord.py library
import requests
import json
from intents import intents

bot = commands.Bot(command_prefix='!', intents=intents)  # Pass the intents argument

# json 파일에서 config.json 정보 가줘오기
def load_config():
    with open('config.json') as file:
        return json.load(file)
    
config = load_config()
BOT_TOKEN = config['BOT_TOKEN']

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')

bot.run(BOT_TOKEN)