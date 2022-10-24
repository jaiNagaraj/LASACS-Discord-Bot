# bot.py
import os
import profanity

from discord.ext import commands
from discord import Intents
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = Intents.all()
client = commands.Bot(command_prefix='!',intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    guild = client.get_guild(803712400888299570) #LASA CS ID

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )
    roleChannelExists = False
    for r in guild.text_channels:
        if str(r) == 'get-roles':
            roleChannelExists = True
    if not roleChannelExists:
        roleChannel = await guild.create_text_channel('get-roles',position=2,topic='Get your roles here!')
        await roleChannel.send(
            """**Come get your roles, folks!**\n
            Class Roles:\n
            """
        )
    print(", ".join([str(str(r.name) + ", " + str(r.id)) for r in guild.roles]))

#greet newcomers
#@client.event
#async def on_member_join(member):
#    await member.create_dm()
#    await member.dm_channel.send(
#        f'Hey there {member.name}! Welcome to the LASA CS discord. Don\'t be afraid to say hi in #general, and make sure to get your role in the get-roles channel!'
#        )
#    general = client.get_channel(803712401399873549) #general channel ID
#    await general.send(f'{member.name} just joined the server, make sure to say hi!')
#
##check for naughty words >:(
#@client.event
#async def on_message(message):
#    if message.author == client.user:
#        return
#    if profanity.contains_profanity(message.content):
#        await message.channel.send("WOAH! That's some strong language which does not have a place on this server (in accordance to rule 3). Please rephrase your sentence in a nicer way.")
#        await message.channel.send("I am a bot, and I sometimes make mistakes. If you think that what you said was appropriate and/or have questions, please DM @jaragan.")


client.run(TOKEN)