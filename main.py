import discord
import cont

client = discord.Client()

key = 'NzgxODk0MzcxNzk2MzIwMjU3.X8ER4Q.Xj2Spc0qanFD71KjetYRTxUeCK0'


@client.event
async def on_ready():
    print('Successfully started!')


@client.event
async def on_message(message):

    if message.author == client.user:
        return
    msg = message.content

    if message.content.startswith('@why bet'):

        amount = float(msg.split(" ")[2])
        on = msg.split(" ")[4]
        cont.place_bet(message.author, amount, 1.5, on)


client.run(key)
