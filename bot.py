# bot.py
import os
import profanity

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    guild = client.get_guild(803712400888299570) #LASA CS ID

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

#greet newcomers
@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hey there {member.name}! Welcome to the LASA CS discord. Don\'t be afraid to say hi in #general!'
        )
    general = client.get_channel(803712401399873549) #general channel ID
    await general.send(f'{member.name} just joined the server, make sure to say hi!')

#check for naughty words >:(
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if profanity.contains_profanity(message.content):
        await message.channel.send("WOAH! That's some strong language which does not have a place on this server (in accordance to rule 3). Please rephrase your sentence in a nicer way.")
        await message.channel.send("I am a bot, and I sometimes make mistakes. If you think that what you said was appropriate and/or have questions, please DM @jaragan.")



client.run(TOKEN)