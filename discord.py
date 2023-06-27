import discord
import requests
from config import BOT_TOKEN

client = discord.Client()
prefix = '!'

@client.event
async def on_ready():
    print(f'Logged in as {client.user.name} ({client.user.id})')

client.run('')