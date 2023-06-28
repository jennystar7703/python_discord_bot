import discord
from discord.ext import commands
import json

intents = discord.Intents.default()  # Create an instance of Intents
intents.typing = False  # Disable typing event (optional)
intents.presences = False  # Disable presence event (optional)

bot = commands.Bot(command_prefix='!', intents=intents)

def load_config():
    with open('config.json') as file:
        return json.load(file)
    
config = load_config()
BOT_TOKEN = config['BOT_TOKEN']    

# Set up the Discord bot client

# Command definition
@bot.command()
async def hello(ctx):
    await ctx.send('Hello, I am your friendly Discord bot!')

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')

bot.run(BOT_TOKEN)