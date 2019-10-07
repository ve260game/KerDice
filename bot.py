import discord
from discord.ext import commands

bot = commands.Bot(command_prefix= '[')

@bot.event
async def on_ready():
    print(">> Bot is online <<")


@bot.event
async def on_member_join(member):
    channel =bot.get_channel(630749684775780352)
    await channel.send(f'{member} join!')

@bot.event
async def on_member_remove(menber):
    channel =bot.get_channel(630749684775780352)
    await channel.send(f'{member} leave!')

@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency*1000)} (ms)')

bot.run('NjMwNDM0OTM1MDg1MzM0NTI4.XZoXdA.TvVZ8EEqQrA9XJ3I4G7ywOxJ71I')

