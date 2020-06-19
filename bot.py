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

    if message.content.startswith('$pic'):
        words = message.content.split(' ')
        query = ''
        if len(words) > 2:
            max_count = aux.parse_number(words[1], None)
            if max_count == None:
                max_count = 0
                query = ' '.join(words[1:])
            else:
                query = ' '.join(words[2:])
        elif len(words) > 1:
            max_count = 0
            query = ' '.join(words[1:])
        else:
            await message.channel.send('Неверный запрос!')

        if query != '':
            print(query)
            print(max_count)
            total = aux.unsplash_get_count(query)
            if max_count > 0:
                total = max_count if total > max_count else total
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
        words = message.content.split(' ')
        if len(words) > 1:
            max_count = aux.parse_number(words[1], 100)
        else:
            max_count = 0
        query = 'sexy girl'
        total = aux.unsplash_get_count(query)
        if max_count > 0:
            total = max_count if total > max_count else total
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
