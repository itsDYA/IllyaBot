import discord
import random
import os
from discord.ext import commands
from keep_alive import keep_alive

players = {}
client = commands.Bot(command_prefix='&')
basura = ["rezero", "Rezero", "re zero", "Re zero"]
verdad = [
    "es una mierda", "no debería existir", "VIVA K-ON",
    "mejor mira algun cgdct"
]
saludos = ["hey", "hola", "o/", "Hey", "Hola"]

@client.event
async def on_ready():
	await client.change_presence(
	    status=discord.Status.online,
	    activity=discord.Game(
	        'Fate/kaleid liner Prisma☆Illya: Licht - Namae no Nai Shoujo'))
	print('Bot is ready.')


@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
	responses = [
	    'En mi opinión, sí', 'Es cierto', 'Es decididamente así',
	    'Probablemente', 'Buen pronóstico', 'Todo apunta a que sí', 'Sin duda',
	    'Sí', 'Sí - definitivamente', 'Debes confiar en ello',
	    'No cuentes con ello', 'Mi respuesta es no',
	    'Mis fuentes me dicen que no', 'No parece serlo', 'Muy dudoso',
	    'Pregunta de nuevo'
	]
	await ctx.send(
	    f'Pregunta: {question}\nRespuesta: {random.choice(responses)}')


client.counter = 0


@client.event
async def on_message(message):
	if message.author == client.user:
		return

	msg = message.content
	if msg.startswith('&'):
		return await client.process_commands(message)

	if any(word in msg for word in saludos):
		await message.channel.send('Sup nerd')

	if client.user.mentioned_in(message):
		await message.channel.send('No me molestes, estoy preparandome para mi futuro')

	if any(word in msg for word in basura):
		await message.channel.send(random.choice(verdad))	


	await client.process_commands(message)


@client.command()
async def ping(ctx):
	await ctx.send(f'Pong! {round(client.latency * 1000)}ms')


@client.command()
async def home(ctx):
	await ctx.send('https://illyabot.itsdya.repl.co/')


@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=5):
	await ctx.channel.purge(limit=amount + 1)


@client.command()
@commands.is_owner()
async def clean(ctx, amount=10):
	await ctx.channel.purge(limit=amount + 1)


@client.command()
@commands.is_owner()
async def say(ctx, *, palabra):
	await ctx.message.delete()
	await ctx.send(f'{palabra}')




keep_alive()
client.run(os.getenv('TOKEN'))
