import discord
from discord.ext import commands
import json

with open('KerDice\setting.json', mode='r', encoding='UTF-8') as jfile: 
    jdata = json.load(jfile) #jdata等於setting文件

bot = commands.Bot(command_prefix= '[') 

@bot.event
async def on_ready():
    print(">> Bot is online <<")


@bot.event
async def on_member_join(member):
    channel =bot.get_channel(int(jdata['Welcome_channel']))
    await channel.send(f'{member} join!')

@bot.event
async def on_member_remove(menber):
    channel =bot.get_channel(int(jdata['Welcome_channel']))
    await channel.send(f'{member} leave!')

@bot.command()
async def ping(ctx):
    channel =bot.get_channel(int(jdata['Welcome_channel']))
    await channel.send('leave!')
    await ctx.send(f'{round(bot.latency*1000)} ms')

bot.run(jdata['TOKEN'])