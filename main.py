import discord

client = discord.Client()

key = ''
@client.event
async def on_ready():
    print('Successfully started!')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run(key)
