import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix=".")
token = os.environ['TOKEN']


@client.event
async def on_ready() :
    await client.change_presence(status=discord.Status.idle, activity=discord.Game("Listening to .help"))
    print("I am online")

client.run(token)