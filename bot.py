import discord
import requests
from config import BOT_TOKEN, API__KEY, HEADERS, intents

client = discord.Client(intents=intents)  # Pass the intents argument

@client.event
async def on_ready():
    print(f'Logged in as {client.user.name} ({client.user.id})')

client.run(BOT_TOKEN)