import discord
from discord.ext import commands, tasks

import logging

from mcstatus import JavaServer

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

# Set up the bot
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

    server = JavaServer.lookup("66.191.193.150:25565")

    try:
        serverStatus = server.status()
    except TimeoutError:
        print("MC Server is Offline")
    
    try:
        status = discord.CustomActivity(name=f"MC Server: Online! {serverStatus.players.online}/{serverStatus.players.max} Players!")
        await client.change_presence(status=discord.Status.online, activity=status)
    except (TimeoutError, NameError):
        status = discord.CustomActivity(name=f"MC Server: Offline :(")
        await client.change_presence(status=discord.Status.online, activity=status)

    if not loop.is_running():
        loop.start()

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.channel.id == 1314065198851686442 or message.channel.id == 1314065184146591744 or message.channel.id == 1314065570517487626 or message.channel.id == 1314447503881539655 or message.channel.id == 1314088983369875488:
        if message.attachments != []:
            await message.add_reaction("⬆️")
            await message.add_reaction("⬇️")

@tasks.loop(seconds=60)
async def loop():
    server = JavaServer.lookup("66.191.193.150:25565")

    try:
        serverStatus = server.status()
    except TimeoutError:
        print("MC Server is Offline")
     
    try:
        status = discord.CustomActivity(name=f"MC Server: Online! {serverStatus.players.online}/{serverStatus.players.max} Players!")
        await client.change_presence(status=discord.Status.online, activity=status)
    except (TimeoutError, NameError):
        status = discord.CustomActivity(name=f"MC Server: Offline :(")
        await client.change_presence(status=discord.Status.online, activity=status)