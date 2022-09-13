import discord
from discord.ext import commands
import time 

bot = discord.ext.commands.Bot(command_prefix = ".")



a = 0

palavraos_file = open("palavras.txt", "r")
file_content = palavraos_file.read()

palavraos_list = file_content.split("""
""")
palavraos_file.close()

lenght = len(palavraos_list)

@bot.event
async def on_ready():
    print(f"Estou Pronto! Estou conectado como {bot.user}")


@bot.event
async def on_message(message):
    op = 0
    while op != lenght:
        if message.author == bot.user:
            return
        if palavraos_list[op] in message.content:
            await message.channel.send(
                f"Sem palavras de baixo calão por aqui {message.author.name}"
            )

            await message.object()
        op += 1

@bot.command(name="olá")
async def send_hello(ctx):
    name = ctx.author.name

    response = f"Olá, {name}, como vai a sua mãe?"

    await ctx.send(response)

token = 'MTAxMDE0OTY4MDYzNTcxMTU1OA.GU1tJ7.S6aPkMXJfyo7BmRXjpTxf_XiBBm94MW0Z3leUE'

intents = discord.all()
intents.members = True

bot = commands.Bot(command_prefix=".", intents=intents)