import discord

import logging

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

# Set up the bot
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.attachments != []:
        await message.add_reaction("⬆️")
        await message.add_reaction("⬇️")
