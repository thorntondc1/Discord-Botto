# bot.py
import os, time, discord
from datetime import datetime
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

win = 0
loss = 0
timestart = datetime.now()

@bot.command(name='startsession')
async def timerstart(ctx):
    global timestart
    global win
    global loss
    timestart = datetime.now()
    win = 0
    loss = 0
    await ctx.send("Session started")

@bot.command(name='stopsession')
async def timestop(ctx):
    global timestart
    global win
    global loss 
    currenttime = datetime.now()
    response = currenttime-timestart
    await ctx.send(f"Your session lasted {response} with {win} wins and {loss} losses")



@bot.command(name='win')
async def add_win(ctx):
    global win
    win += 1 
    await ctx.send("Added a win, good job!")

@bot.command(name='loss')
async def add_loss(ctx):
    global loss
    loss += 1
    response = loss
    await ctx.send("They're cheaters, you'll get em next time")

bot.run(TOKEN)