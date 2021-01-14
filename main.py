import discord

client = discord.Client()


@client.event
async def on_ready():
    print('Successfully started!')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run('NzgxODk0MzcxNzk2MzIwMjU3.X8ER4Q.TnHShENO5glK-T5FjwHIfWKC0DA')
