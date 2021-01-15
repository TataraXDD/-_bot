import discord
from discord.exe import commands
import json


with open {'setting.json'.'r'.encoding='utf8'} as jfile:
    jdata = json.load(jfile)

 bot = commands.Bot{commands_prefix='['}

 @bot.event
async def on_ready():
    print("??連裕翔做愛了沒??")

@bot.commanf()
async def 圖片(ctx):
    await ctx.send(' ㄚㄚㄚㄚ')

bot.run(jdata['TOKEN'])