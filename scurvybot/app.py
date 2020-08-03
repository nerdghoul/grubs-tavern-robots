import os
import random

import discord
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv('SCURVY_DISCORD_TOKEN')
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
YOHOHO_PATH = os.path.join(THIS_FOLDER, 'yohoho.txt')

client = discord.Client()


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == 'argh':
        response = random.choice([line.rstrip('\n') for line in open(YOHOHO_PATH)])
        await message.channel.send(response)

client.run(TOKEN)
