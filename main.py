from typing import Final
from dotenv import load_dotenv
import os
import discord
from discord.ui import Button, View
from discord import app_commands, ButtonStyle
from discord.ext import commands
from ilbattle import il_battle
from records import ilrecord
from poopster import poopster
from test import test
from powerranking import powerranking
import Paginator

#Setup Discord Junk
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')
intents: discord.Intents = discord.Intents.all()
intents.message_content = True # NOQA
bot: commands.Bot = commands.Bot(command_prefix="!br", intents=intents)

#Sync commands
@bot.event
async def on_ready():
    print('Hi :3')
    try:
        synced = await bot.tree.sync()
        print(f"{len(synced)} commands synced.")
    except Exception as e:
        print(e)

@bot.event
async def on_message(message: discord.Message):
    if len(message.content) < 1:
        return
    if message.content[0] == '!':
        inputcommand = message.content.removeprefix('!')
        if inputcommand.split(' ')[0] == 'poopster':
            if (inputcommand.replace(' ', '') == 'poopster'):
                response = poopster(None)
            else:
                response = poopster(inputcommand.split(' ', 1)[1])
            await message.channel.send(response)
        if inputcommand.split(' ')[0] == 'test':
            if message.author.id == 258712206298841088:
                await message.channel.send(test())

@bot.tree.command(name='powerrankings', description='Shows the Power Rankings for the provided game!')
@app_commands.describe(game='Which Game?')
@app_commands.choices(game=[
    app_commands.Choice(name = 'Banana Blitz HD', value='bbhd'),
    app_commands.Choice(name = 'Banana Mania', value = 'mania'),
    app_commands.Choice(name = 'Banana Rumble', value = 'rumble')
])
async def powerrankings(interaction: discord.Interaction, game:str):
    pages = powerranking(game)
    await Paginator.Simple().start(interaction, pages)

@bot.tree.command(name='testcommand', description='test')
async def testcommand(interaction: discord.Interaction):
    if (interaction.user.id == 258712206298841088):
        pages = powerranking('mania')
        await Paginator.Simple().start(interaction, pages)

#IL Battle Parameters
@bot.tree.command(name="ilbattle", description="Generates a list of stages for a potential Individual Level battle!")
@app_commands.describe(game = "What game?")
@app_commands.choices(game=[
    app_commands.Choice(name = 'Banana Blitz HD', value='BBHD'),
    app_commands.Choice(name = 'Banana Mania', value = 'Mania'),
    app_commands.Choice(name = 'Banana Rumble', value = 'Rumble')
])
@app_commands.describe(stages = "How many stages would you list in your list?")
@app_commands.describe(category1 = "Would you like to specify a set of stages?")
@app_commands.choices(category1=[
    app_commands.Choice(name='World Tour (Rumble)', value='wt'),
    app_commands.Choice(name="World Tour EX (Rumble)", value="wtex"),
    app_commands.Choice(name="Story Mode (Mania)", value="story"),
    app_commands.Choice(name="SMB1 Challenge (Mania)", value="smb1"),
    app_commands.Choice(name="SMB2 Challenge (Mania)", value="smb2"),
    app_commands.Choice(name="Specials (Mania)", value="specials"),
    app_commands.Choice(name="DX Mode (Mania)", value="dxonly")]
    )
@app_commands.describe(category2 = "Would you like to specify a set of stages?")
@app_commands.choices(category2=[
    app_commands.Choice(name='World Tour (Rumble)', value='wt'),
    app_commands.Choice(name="World Tour EX (Rumble)", value="wtex"),
    app_commands.Choice(name="Story Mode (Mania)", value="story"),
    app_commands.Choice(name="SMB1 Challenge (Mania)", value="smb1"),
    app_commands.Choice(name="SMB2 Challenge (Mania)", value="smb2"),
    app_commands.Choice(name="Specials (Mania)", value="specials"),
    app_commands.Choice(name="DX Mode (Mania)", value="dxonly")]
    )
@app_commands.describe(category3 = "(Optional) Would you like to specify a set of stages?")
@app_commands.choices(category3=[
    app_commands.Choice(name='World Tour (Rumble)', value='wt'),
    app_commands.Choice(name="World Tour EX (Rumble)", value="wtex"),
    app_commands.Choice(name="Story Mode (Mania)", value="story"),
    app_commands.Choice(name="SMB1 Challenge (Mania)", value="smb1"),
    app_commands.Choice(name="SMB2 Challenge (Mania)", value="smb2"),
    app_commands.Choice(name="Specials (Mania)", value="specials"),
    app_commands.Choice(name="DX Mode (Mania)", value="dxonly")]
    )
async def ilbattle(interaction: discord.Interaction, game: str, stages: int, category1: str = None, category2: str = None, category3: str = None):
    categories = f"{category1},{category2},{category3}"
    message = il_battle(game, stages, categories)
    await interaction.response.send_message(message, ephemeral=False)

#Record Command
@bot.tree.command(name="record", description="Provides the current live proof world record of a stage from SMBElite!")
@app_commands.describe(game = "What game?")
@app_commands.choices(game=[
    app_commands.Choice(name = 'Banana Blitz HD', value='bbhd'),
    app_commands.Choice(name = 'Banana Mania', value = 'mania'),
    app_commands.Choice(name = 'Banana Rumble', value = 'rumble')
])
@app_commands.describe(type = "Time or Score? Time is default.")
@app_commands.choices(type=[
    app_commands.Choice(name='Time', value='time'),
    app_commands.Choice(name='Score', value='score')
])
@app_commands.describe(category = "(Optional) If your game has a stage in multiple categories, specify it here. Otherwise the first instance will be pulled")
@app_commands.choices(category=[
    app_commands.Choice(name='Story Mode', value='story'),
    app_commands.Choice(name='SMB1 Challenge', value='smb1'),
    app_commands.Choice(name='SMB2 Challenge', value='smb2'),
    app_commands.Choice(name='Original Stage Mode', value='og'),
    app_commands.Choice(name='Golden Banana Mode', value='gb'),
    app_commands.Choice(name='Dark Banana Mode', value='db'),
    app_commands.Choice(name='Reverse Mode', value='reverse'),
    app_commands.Choice(name='DX Mode', value='dx'),
    app_commands.Choice(name='World Tour', value='wt'),
    app_commands.Choice(name='World Tour EX', value='wtex')
])

@app_commands.describe(jump = "(Optional) If your record is a Mania record, would you like the Jumps WR? Jumpless is default.")
@app_commands.choices(jump=[
    app_commands.Choice(name='Jumpless', value='nojump'),
    app_commands.Choice(name='Jumps', value='jump')
])

@app_commands.describe(color = "What color is the goal? Defaults to nothing.")
@app_commands.choices(color=[
    app_commands.Choice(name="Blue", value="blue"),
    app_commands.Choice(name="Green", value="green"),
    app_commands.Choice(name="Red", value="red")
])
async def record(interaction: discord.Interaction, game: str, level: str, type: str = None, category: str = None, jump:str = None, color:str = None):
    message = ilrecord(game, level, type, category, jump, color)
    await interaction.response.send_message(message, ephemeral=False)

bot.run(TOKEN)
    


