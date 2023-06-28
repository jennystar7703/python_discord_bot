# config.py

import discord 

API__KEY = ''

HEADERS = {
    'Authorization': f'Bearer {API__KEY}',
    'Content-Type': 'application/json'
}

BOT_TOKEN='MTEyMzEzNDEwNDQ1NjY1OTAwNQ.GmWDvE.avQNZGNf4QosVDJiugQDccOpEHUp0QPFgIM_S0'

intents = discord.Intents.default()  # Create an instance of Intents
intents.typing = False  # Disable typing event (optional)
intents.presences = False  # Disable presence event (optional)