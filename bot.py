import discord
import random
import os

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
    
    if message.content.startswith('$roll'):
        roll_result = random.randint(1, 100)
        await message.channel.send('You rolled: ' + roll_result)

client.run(os.environ.get('discord_token'))
