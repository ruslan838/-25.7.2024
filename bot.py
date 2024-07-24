import discord
import random
import datetime
from discord.ext import commands

# Переменная intents - хранит привилегии бота
intents = discord.Intents.default()
# Включаем привелегию на чтение сообщений
intents.message_content = True
# Создаем бота в переменной client и передаем все привелегии
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')


@bot.command()
async def bw(ctx, word: str):
    result = ''
    for i in range(len(word)-1, -1, -1):
        result += word[i]
    await ctx.send(result)

@bot.command()
async def time(ctx):
    a = datetime.datetime.now()
    await ctx.send(a.strftime('%H:%M:%S'))

@bot.command()
async def date(ctx):
    a = datetime.datetime.now()
    await ctx.send(a.strftime('%d.%m.%Y'))

bot.run("TOKEN")