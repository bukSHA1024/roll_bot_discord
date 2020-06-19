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
        await message.channel.send('Hi!')

    if message.content.startswith('$roll'):
        roll_result = random.randint(1, 100)
        await message.channel.send('You rolled: ' + roll_result)

    if message.content.startswith('$pic '):
        query = ' '.join(message.content.split(' ')[1:])
        total = aux.unsplash_get_count(query)
        #total = 100 if total > 100 else total
        if total > 0:
            pic_num = random.randint(1, total)
            pic_url = aux.unsplash_get_pic_url(query, pic_num)
            if pic_url == None:
                await message.channel.send('Ошибка при загрузке :(')
            else:
                await message.channel.send(f"Хоба!({pic_num}/{total})",
                    embed=discord.Embed().set_image(url=pic_url))
        else:
            await message.channel.send('Ничего не найдено :(')

    if message.content.startswith('$girls'):
        query = 'sexy girl'
        total = aux.unsplash_get_count(query)
        #total = 100 if total > 100 else total
        if total > 0:
            pic_num = random.randint(1, total)
            pic_url = aux.unsplash_get_pic_url(query, pic_num)
            if pic_url == None:
                await message.channel.send('Ошибка при загрузке :(')
            else:
                await message.channel.send(f"Руки на стол!({pic_num}/{total})",
                    embed=discord.Embed().set_image(url=pic_url))
        else:
            await message.channel.send('Ничего не найдено :(')

client.run(os.environ.get('discord_token'))
