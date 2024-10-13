import os
import discord
from discord.ext import commands

token = os.getenv("DISCORD_WEATHER_BOT_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot 已登入為 {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if '早安' in message.content:
        await message.channel.send('晚安')
    
    if '晚安' in message.content:
        await message.channel.send('不早安')
    
    if '午安' in message.content:
        await message.channel.send('牛安')

    await bot.process_commands(message)

@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

@bot.command()
async def 你是誰(ctx):
    await ctx.send('Hi! 我是用來查詢天氣的機器人')


bot.run(token)

