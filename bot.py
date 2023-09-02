import discord
import responses
import os
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()  # Load environment variables from .env file
TOKEN = os.getenv("DISCORD_TOKEN")  # Token grabber

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', case_insensitive=True, intents=intents)  # Initialize commands.Bot with intents

@bot.command(name='test')
async def test_command(ctx):
    await ctx.send("This is a test")

@bot.command(name='info')
async def info_command(ctx, hero_name: str = None):
    if hero_name:
        hero_name = hero_name.lower()  # Convert input to lowercase

        # Define hero aliases
        hero_aliases = {
            'quincy': ['quinc', 'quin', 'q'],
            'obyn': ['oby', 'o'],
            'gwen': ['g', 'gwendolyn'],
            'pat': ['fusty', 'pat fusty', 'p', 'pf'],
            'ben': ['benjamin', 'benjy', 'benj', 'be', 'benny'],
            'sauda': ['s'],
            'brickell': ['brick', 'admiral', 'admiral brickell', 'ab', 'adm'],
            'adora': ['dora', 'ado'],
            'churchill': ['captain', 'captain churchill', 'c'],
            'ezili': ['ez'],
            'ettiene': ['etn', 'et'],
            'jones': ['striker', 'striker jones', 'sj', 'st', 'j']
        }

        # Check for heroes and aliases
        for hero, aliases in hero_aliases.items():
            if hero_name == hero or hero_name in aliases:
                # Add specific information for each hero/alias
                if hero == 'quincy':
                    await ctx.send("This is information about Quincy.")
                elif hero == 'obyn':
                    await ctx.send("This is information about Obyn.")
                elif hero == 'gwen':
                    await ctx.send("This is information about Gwen.")
                elif hero == 'pat':
                    await ctx.send("This is information about Pat.")
                elif hero == 'ben':
                    await ctx.send("This is information about Ben.")
                elif hero == 'sauda':
                    await ctx.send("This is information about Sauda.")
                elif hero == 'brickell':
                    await ctx.send("This is information about Brickell.")
                elif hero == 'adora':
                    await ctx.send("This is information about Adora.")
                elif hero == 'churchill':
                    await ctx.send("This is information about Churchill.")
                elif hero == 'ezili':
                    await ctx.send("This is information about Ezili.")
                elif hero == 'ettiene':
                    await ctx.send("This is information about Ettiene.")
                elif hero == 'jones':
                    await ctx.send("This is information about Jones.")
                return  # Exit the loop if a match is found

        # If no match found
        await ctx.send("I don't have information about that hero.")
    else:
        await ctx.send("Please type in a hero's name after **info**. For example: `!info Obyn`")




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
