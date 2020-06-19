import discord
import random
import os
import auxiliary as aux

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send(f"Hello, {message.author.mention}!")

    if message.content.startswith('$roll'):
        words = message.content.split(' ')
        low, high = 0, 100
        if len(words) == 2:
            high = aux.parse_number(words[1], high)
        elif len(words) == 3:
            low = aux.parse_number(words[1], low)
            high = aux.parse_number(words[2], high)
        if low > high:
            low, high = high, low
        roll_result = random.randint(low, high)
        await message.channel.send(f"You rolled({low}:{high}): " + str(roll_result))

    if message.content.startswith('$choice '):
        arguments = message.content[8:]
        words = arguments.split(' или ')
        if len(words) == 1:
            words = arguments.split(' ')
        choice = random.choice(words)
        await message.channel.send(choice)

client.run(os.environ.get('discord_token'))
