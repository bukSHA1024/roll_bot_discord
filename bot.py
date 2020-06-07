import discord
import secrets
import string
import os
import xchange

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hi!')

    if message.content.startswith('$exchange'):
        string.strip(message.content, '$exchange ')
        if message.content.startswith('rub'):
            string.strip(message.content, 'rub ')
            await message.channel.send("Uero: " + RUB(int(message.content)).exchange_to_eur() + "\n Dollar: " + RUB(int(message.content)).exchange_to_usd())

client.run(os.environ.get('discord_token'))
