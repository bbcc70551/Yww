from multiprocessing.connection import wait
import discord
from discord.commands import Option
from discord.ext import commands
import json
import random


with open('setting.json', mode='r',encoding='utf8') as jfile:
    jdata = json.load(jfile)


intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!', intents = intents)

bot = discord.Bot(
    intents=intents,
    debug_guilds=[890071213857198129] #頻道ID
)

#機器人上線
@bot.event
async def on_ready():
    print(f"{bot.user} ist online")


#成員加入 #頻道ID


#獲取身分組




#移除身分組


#機器人指令
@bot.slash_command(description="Grüße einen User")
async def greet(ctx, user: Option(discord.User, "Der User, den du grüßen möchtest")):
    await ctx.respond(f"Hallo {user.mention}")

#/say機器人打字說話
@bot.slash_command(description="Lass den Bot eine Nachricht senden")
async def say(
        ctx,
        text: Option(str, "Der Text, den du senden möchtest"),
        channel: Option(discord.TextChannel, "Der Channel, in den du die Nachricht senden möchtest")
):
    await channel.send(text)
    await ctx.respond("Nachricht gesendet", ephemeral=True)

#傳圖片
@bot.command()
async def 在嗎(ctx):
    pic = discord.File(jdata['pic'])
    await ctx.send(file= pic)

@bot.command()
async def 給你一朵小紅花(ctx):
    pic4 = discord.File(jdata['pic4'])
    await ctx.send("**送你一朵小紅花**",file= pic4) #文字+圖片
    

#傳隨機圖片
@bot.command()
async def 我要看魚丸丸(ctx):
    random_pic2 = random.choice(jdata['pic2'])
    pic2 = discord.File(random_pic2)
    await ctx.send(file= pic2)

@bot.command()
async def 于文文表演(ctx):
    random_pic3 = random.choice(jdata['pic3'])
    pic3 = discord.File(random_pic3)
    await ctx.send(file= pic3)



bot.run(jdata['TOKEN'])
