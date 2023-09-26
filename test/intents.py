import discord
from discord.ext import commands #module in Discord.py library

intents = discord.Intents.default()  # Create an instance of Intents
intents.typing = False  # Disable typing event (optional)
intents.presences = False  # Disable presence event (optional)
intents.members = True
intents.guilds = True
intents.messages=True
#client = discord.Client(intents=intents)  # Pass the intents argument

def get_intents():
    return intents