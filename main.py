import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def calk(ctx, num1 = 0, sim = 'Введите число, оператор и второе число', num2 = 0):
    if sim == '+':
        await ctx.send(num1 + num2)

    elif sim == '-':
        await ctx.send(num1 - num2)

    elif sim == '/':
        await ctx.send(num1 / num2)

    elif sim == '*':
        await ctx.send(num1 * num2)
        
    else:
        await ctx.send(sim)
        
bot.run("enter your token")
