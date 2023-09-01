import discord
import responses
import os
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()  # Load environment variables from .env file
TOKEN = os.getenv("DISCORD_TOKEN")  # Token grabber

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)  # Initialize commands.Bot with intents

@bot.command(name='test')
async def test_command(ctx):
    await ctx.send("This is a test")

async def send_message(message, user_message, is_private):
    try:
        response = responses.get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

@bot.event
async def on_ready():
    print(f'{bot.user} is now running!')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    username = str(message.author)
    user_message = str(message.content)
    channel = str(message.channel)

    print(f'{username} said: "{user_message}" in ({channel})')
    if user_message[0] == '?':
        user_message = user_message[1:]
        await send_message(message, user_message, is_private=True)
    else:
        await bot.process_commands(message)  # Handle bot commands

bot.run(TOKEN)
