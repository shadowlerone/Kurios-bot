import discord
from discord.ext import commands
import random

description = '''An example bot to showcase the discord.ext.commands extension
module.
There are a number of utility commands being showcased here.'''
bot = commands.Bot(command_prefix='>', description=description)

@bot.event
async def on_ready():
	print('Logged in as')
	print(bot.user.name)
	print(bot.user.id)
	print('------')



@bot.command()
async def attendance(ctx):
	with open("attendees.txt", "w") as fp:
		fp.write("\n".join(map(str, ctx.guild.get_channel(692133317948211282).members)))
	await ctx.send(file=discord.File("attendees.txt"))




bot.run('token')