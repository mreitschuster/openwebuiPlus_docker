import discord
from discord.ext import commands
import requests

# Get bot token from environment variable
TOKEN = os.environ['DISCORD_BOT_TOKEN']

# Create a new instance of the bot class
bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.event
async def on_message(message):
    # You can add logic here to process incoming messages, e.g., send them to Open-WebUI for processing

    if message.author == bot.user:
        return  # Ignore messages from your own bot

    await bot.process_commands(message)

# Start the bot's event loop
bot.run(TOKEN)