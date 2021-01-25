import discord
import os
import requests
import json

client = discord.Client()

def get_quote():
  response = request.get (https://myanimelist.net)

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
      return
  if message.content.startswith('Hola'):
    await message.channel.send('Sup nerd')


client.run(os.getenv('TOKEN'))