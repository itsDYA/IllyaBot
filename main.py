import discord
import os
import requests
import json
import random
from keep_alive import keep_alive


client = discord.Client()
basura = ["rezero"]
verdad = [
    "es una mierda",
    "no debería existir",
    "VIVA K-ON",
]


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " - " + json_data[0]['a']
    return (quote)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content

    if msg.startswith('Hola'):
        await message.channel.send('Sup nerd')

    if msg.startswith('Inspirame'):
        quote = get_quote()
        await message.channel.send(quote)
    if any(word in msg for word in basura):
        await message.channel.send(random.choice(verdad))

keep_alive()
client.run(os.getenv('TOKEN'))
