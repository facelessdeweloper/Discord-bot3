import discord, requests
from function import *
from discord.ext import commands
from key_ds import *
from os import listdir
from random import choice

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)


@bot.command()
async def decomposition(ctx):
    await ctx.send(decomposition1())

@bot.command()
async def recycling(ctx):
    await ctx.send(recycling1())

@bot.command()
async def bot_info(ctx):
    await ctx.send(infobot())

@bot.command()
async def sorting(ctx):
    await ctx.send(sorting1())
bot.run(token_ds())
