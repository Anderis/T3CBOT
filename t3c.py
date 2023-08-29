import discord
import t3cResponse as responses
from discord.ext import commands
import re
import random
from dotenv import load_dotenv

async def send_message(message, user_message, is_private):
    try:
        response = responses.get_response(user_message)

        if response and not is_private:
            await message.channel.send(response)
    except Exception as e:
        print(e)

def run_discord_bot(bot_token):
    intents = discord.Intents.default()
    intents.typing = False
    intents.presences = False
    intents.messages = True
    bot = commands.Bot(command_prefix='!', intents=intents.all(), help_command=None)  # Disable the default help command
    @bot.event
    async def on_ready():
        print(f'{bot.user} is now running')

    @bot.event
    async def on_message(message):
        if message.author == bot.user:
            return
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)
        print(f'{username} said: "{user_message}" ({channel})')

    @bot.command(name='help', aliases=['help'])
    async def mochihelp_command(ctx):
        embed = discord.Embed(title='TO THE RESCUE!', description='List of available commands & phrases:', color=discord.Color.yellow())

        # Commands

        commands_field = "A command can only be run standalone and must begin with a \"!\".\n"
        commands_field += "```"

        commands_field += "```\u200b"

        # Trigger Statements
        statements_field = "Similar to commands, a trigger statement cannot include additional characters. However, it does not need to begin with a \"!\".\n"
        statements_field += "```"
        statements_field += "```"

        # Trigger Words
        words_field = "A trigger word can be used at any point in a sentence without the need for a prefix.\n"
        words_field += "\n"
        words_field += "```\n"

        embed.add_field(name='__**Commands**__', value=commands_field, inline=False)
        embed.add_field(name='__**Trigger Statements**__', value=statements_field, inline=True)
        embed.add_field(name='__**Trigger Words**__', value=words_field, inline=True)

        await ctx.send(embed=embed)

    bot.run(bot_token)
