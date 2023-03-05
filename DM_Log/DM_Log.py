
import discord
from discord.ext import commands

intents = discord.Intents.all()
client = discord.Client(token='TOKEN', intents=intents)

def log_dm(message, file_name):
    if isinstance(message.channel, discord.DMChannel):
        with open(file_name, 'a') as file:
            file.write(f'{message.author.name}: {message.content}\n')

@client.event
async def on_message(message):
    #requires dir path to be run as .py
    log_dm(message, 'logs.txt')
    
client.run('TOKEN')