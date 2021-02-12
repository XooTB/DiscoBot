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

    if message.content.startswith('@why events'):
        await message.channel.send(f'Event 1: {event1.name}, Odds(Yes/No): {event1.odd1}/{event1.odd2}')

event1 = cont.Event('Will ves win the design duel?', 1.5, 2.5)

client.run(key)
