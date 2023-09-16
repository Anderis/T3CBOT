import discord
import pytz
import responses
import os
import heroes
import base64
import interactions
import asyncio
from discord.ui import Button, View
from dotenv import load_dotenv
from discord.ext import commands
from heroes import get_hero_info, get_hero_cost

load_dotenv()  # Load environment variables from .env file
TOKEN = os.getenv("DISCORD_TOKEN")  # Token grabber

intents = discord.Intents.all()
intents.message_content = True

bot = commands.Bot(command_prefix='!', case_insensitive=True, intents=intents)  # Initialize commands.Bot with intents

@bot.command(name='test')
async def test_command(ctx):
    await ctx.send("This is a test")

class ButtonTest(discord.ui.View):
    def __init__(self, initial_message, initial_embed):
        super().__init__(timeout=None)
        self.initial_message = initial_message
        self.initial_embed = initial_embed

    @discord.ui.button(label="Hero Stats", style=discord.ButtonStyle.blurple)
    async def test_hero_stats(self, interaction: discord.Interaction, button: discord.ui.Button):
        # Modify the existing embed with HeroStats information
        self.initial_embed.title = ""
        self.initial_embed.description = "# HERO DATA\n\n## **Stats(Max)**\nPierce:20\nDamage:20\nAttack-Speed:0.5s"



        # Reply to the interaction with the updated embed (ephemeral=True)
        await interaction.response.send_message(embed=self.initial_embed, ephemeral=True)

    @discord.ui.button(label="Strategy", style=discord.ButtonStyle.blurple)
    async def test_strategy(self, interaction: discord.Interaction, button: discord.ui.Button):
        # Modify the existing embed with Strategy information
        self.initial_embed.title = "Strategy Button Clicked"
        self.initial_embed.description = "This is the Strategy button."
       # Reply to the interaction with the updated embed (ephemeral=True)
        await interaction.response.send_message(embed=self.initial_embed, ephemeral=True)


@bot.command(name="info")
async def buttonmenu(ctx, hero_name: str):
    if hero_name is None:
        await ctx.send("Please provide a hero's name after **buttonmenu**. For example: `!buttonmenu Obyn`")
        return

    hero_info = get_hero_info(hero_name)

    if hero_info:
        # Fetch the cost information for the hero using the get_hero_cost function
        cost_info = get_hero_cost(hero_name)

        description = f"## **{hero_info['title']}**\n\n"

        if cost_info:
            # Include the cost information in the description above the main description
            description += f"🔓 **Unlocked at** Level 28 🔓\n```ansi\n\n[1;2mSPECIALTY[0m\nSupport/Crowd-Control\n\n[1;2mHERO COST[0m\n{cost_info}\n```\n"

        # Append the main description
        description += hero_info['description']

        embed = discord.Embed(
            title='',
            description=description,
            color=hero_info['color']
        )

        # Get the image URL for the hero from hero_data
        image_url = hero_info.get('image_url', '')

        if image_url:
            embed.set_thumbnail(url=image_url)  # Set the image URL as the embed's thumbnail

        # Create an instance of the ButtonTest class
        button_test = ButtonTest(ctx.message, embed)  # Pass the message and embed to the constructor

        # Send the initial embed with the buttons from the ButtonTest instance
        await ctx.send(embed=embed, view=button_test)

async def main():
    async with bot:
        await bot.start("")

async def send_message(message, user_message, is_private):
    try:
        response = responses.get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f'{bot.user} is now running!')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    username = str(message.author)
    user_message = str(message.content)

    if message.guild:  # Check if the message was sent in a server
        channel = f"#{message.channel}"
        location = f"in {channel}"
    else:
        location = "in private DMs"

    # Convert UTC time to EST timezone
    est_timezone = pytz.timezone('US/Eastern')
    utc_time = message.created_at.replace(tzinfo=pytz.UTC)
    est_time = utc_time.astimezone(est_timezone)

    timestamp = est_time.strftime("%Y-%m-%d %H:%M:%S")  # Format the timestamp

    if message.guild:
        print(f'{username} said: "{user_message}" in "{message.guild.name} #{message.channel.name}", at {timestamp}')
    else:
        print(f'{username} said: "{user_message}" in DMs at {timestamp}')

    if user_message.startswith('?'):
        user_message = user_message[1:]
        await send_message(message, user_message, is_private=True)
    else:
        await bot.process_commands(message)  # Handle bot commands

bot.run(TOKEN)
