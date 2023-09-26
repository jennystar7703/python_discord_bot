import discord
from discord.ext import commands
import json

bot = commands.Bot(command_prefix='$', intents=discord.Intents.all())

def load_config():
    with open('config.json') as file:
        return json.load(file)
    
config = load_config()
BOT_TOKEN = config['BOT_TOKEN']    

# Set up the Discord bot client

# Command definition
@bot.command()
async def hello(ctx):
    print("Hello command received") 
    await ctx.send('Hello, I am your friendly Discord bot!')

@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')

@bot.event
async def on_command_error(ctx, error):
    print(f'An error occurred: {error}')


bot.run(BOT_TOKEN)