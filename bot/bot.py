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
        await message.channel.send(f"Hello, {message.author.mention}!")

    if message.content.startswith('$roll'):
        words = message.content.split(' ')
        if len(words) == 3 and words[1].isdigit() and words[2].isdigit():
            low = int(words[1])
            high = int(words[2])
            if low > high:
                low, high = high, low
        else:
            low, high = 1, 100
        roll_result = random.randint(low, high)
        await message.channel.send('You rolled: ' + str(roll_result))

client.run(os.environ.get('discord_token'))
