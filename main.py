import discord
import cont
import os

client = discord.Client()

key = ''


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
