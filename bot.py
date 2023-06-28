import discord
import requests
import json

# json 파일에서 config.json 정보 가줘오기
def load_config():
    with open('config.json') as file:
        return json.load(file)
    
config = load_config()
BOT_TOKEN = config['BOT_TOKEN']
    
# discord 라이브러리 세팅 chatgpt 에서 가줘왔음 
intents = discord.Intents.default()  # Create an instance of Intents
intents.typing = False  # Disable typing event (optional)
intents.presences = False  # Disable presence event (optional)
client = discord.Client(intents=intents)  # Pass the intents argument

@client.event
async def on_ready():
    print(f'Logged in as {client.user.name} ({client.user.id})')

client.run(BOT_TOKEN)