import discord #<-- Importing discord.
from discord.ext import commands #<-- importing discord.ext for commands.
from discord.commands import slash_command #<-- import slash commands

client = commands.Bot() #<-- Defining 'client' as the bot

@client.event #<-- checks for an event
async def on_ready(): #<-- Checks when the bot is ready
  print("The bot is ready!") #<-- prints "Bot is ready" when the statement falls true.
  
  
client.run('TOKEN') #<-- runs the token
