import discord
from discord.ext import commands
import time 




bot = commands.Bot("!")

a = 0

palavraos = ["porra","bosta","buceta","caralho","fdp","soca","broxa","fofo",
"sapequinha","bastardo","plebe","putifuro","foda-se","foder","fuder","nem fodendo",
"pau","pica","pqp","punheta","cu","trepar","xoxota",'sacanagem','cacete','arrombado',
"babaca",'bicha','boiola','cracudo','filha da puta','galinha','puta','piranha','vagabundo',
'vagabunda','viado','corno','fudido','escroto','fudido','canalha','paspalho','trouxa','vaca',
'vadia','otario','bostao','mongoloide','penes','poha','sexo','sex','droga','maconha','merda','lolo',
'merdão','esporrada','fodinha','4lan','fodao','xvideos','pornhub','porrão','semen',]

lenght = len(palavraos)
@bot.event
async def on_ready():
    print(f"Estou Pronto! Estou conectado como {bot.user}")


@bot.event
async def on_message(message):
    op = 0
    while op != lenght:
        if message.author == bot.user:
            return
        if palavraos[op] in message.content:
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


bot.run()