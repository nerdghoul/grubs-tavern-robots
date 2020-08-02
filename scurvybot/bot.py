import os
import random

import discord
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv('SCURVY_DISCORD_TOKEN')

client = discord.Client()


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == 'argh':
        response = random.choice([line.rstrip('\n') for line in open('yohoho.txt')])
        await message.channel.send(response)

client.run(TOKEN)
