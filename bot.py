# bot.py
import os
import profanity

from discord.ext import commands
from discord import Intents
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')


intents = Intents.all()
client = commands.Bot(command_prefix='!',intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    guild = client.get_guild(GUILD) #LASA CS ID

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
        rolMsg = await roleChannel.send(
            """
            **Come get your roles, folks!**\n
            Make sure to react accordingly to get roles that fit YOU! Hold down Shift to select multiple reactions.\n\n
            *Grade Roles*:\n
            `9th Grade` react with 🤓\n
            `10th Grade` react with 🤠\n
            `11th Grade` react with 😎\n
            `12th Grade` react with 🧐\n
            \n
            *CS Classes*:\n
            `Intro to CS` react with 👶\n
            `AP CS` react with 😊\n
            `Advanced CS` react with 🤑\n
            `Independent Study` react with 👴\n
            `Web and Mobile` react with 📱\n
            `Digital Electronics` react with 💽\n
            \n
            *Clubs*
            `Hack Club` react with 🔍\n
            `CS Club` react with 🦸‍♂️\n
            `Programming in Practice` react with 🤵\n
            `Cyberpatriot` react with 🛑\n
            `WiCS+` react with 👩‍💻\n
            `Raptor DataWorks` react with 📜\n
            """
        )
        rolMsg.add_reaction('🤓')
        rolMsg.add_reaction('🤠')
        rolMsg.add_reaction('😎')
        rolMsg.add_reaction('🧐')
        rolMsg.add_reaction('👶')
        rolMsg.add_reaction('😊')
        rolMsg.add_reaction('🤑')
        rolMsg.add_reaction('👴')
        rolMsg.add_reaction('📱')
        rolMsg.add_reaction('💽')
        rolMsg.add_reaction('🔍')
        rolMsg.add_reaction('🦸‍♂️')
        rolMsg.add_reaction('🤵')
        rolMsg.add_reaction('🛑')
        rolMsg.add_reaction('👩‍💻')
        rolMsg.add_reaction('📜')
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
#        await message.channel.send("I am a bot, and I sometimes make mistakes. If you think that what you said was appropriate and/or have questions, please DM jaragan.")
@client.event
async def on_raw_reaction_add(ctx):
    guild = client.get_guild(GUILD)
    roleChannel = discord.utils.get(guild.channels, name="get-roles",type="ChannelType.text")
    if ctx.channel_id != roleChannel or ctx.user_id == client.id:
        return
    if ctx.emoji == '🤓':
        roleToAdd = discord.utils.get(guild.roles,id=00000000000)
        currMember = client.get_user(ctx.user_id)
        currMember.add_roles(roleToAdd)
    elif ctx.emoji == '🤠':
        roleToAdd = discord.utils.get(guild.roles,id=00000000000)
        currMember = client.get_user(ctx.user_id)
        currMember.add_roles(roleToAdd)
    elif ctx.emoji == '😎':
        roleToAdd = discord.utils.get(guild.roles,id=00000000000)
        currMember = client.get_user(ctx.user_id)
        currMember.add_roles(roleToAdd)
    elif ctx.emoji == '🧐':
        roleToAdd = discord.utils.get(guild.roles,id=00000000000)
        currMember = client.get_user(ctx.user_id)
        currMember.add_roles(roleToAdd)
    elif ctx.emoji == '👶':
        roleToAdd = discord.utils.get(guild.roles,id=00000000000)
        currMember = client.get_user(ctx.user_id)
        currMember.add_roles(roleToAdd)
    elif ctx.emoji == '😊':
        roleToAdd = discord.utils.get(guild.roles,id=00000000000)
        currMember = client.get_user(ctx.user_id)
        currMember.add_roles(roleToAdd)
    elif ctx.emoji == '🤑':
        roleToAdd = discord.utils.get(guild.roles,id=00000000000)
        currMember = client.get_user(ctx.user_id)
        currMember.add_roles(roleToAdd)
    elif ctx.emoji == '👴':
        roleToAdd = discord.utils.get(guild.roles,id=00000000000)
        currMember = client.get_user(ctx.user_id)
        currMember.add_roles(roleToAdd)
    elif ctx.emoji == '📱':
        roleToAdd = discord.utils.get(guild.roles,id=00000000000)
        currMember = client.get_user(ctx.user_id)
        currMember.add_roles(roleToAdd)
    elif ctx.emoji == '💽':
        roleToAdd = discord.utils.get(guild.roles,id=00000000000)
        currMember = client.get_user(ctx.user_id)
        currMember.add_roles(roleToAdd)
    elif ctx.emoji == '🔍':
        roleToAdd = discord.utils.get(guild.roles,id=00000000000)
        currMember = client.get_user(ctx.user_id)
        currMember.add_roles(roleToAdd)
    elif ctx.emoji == '🦸‍♂️':
        roleToAdd = discord.utils.get(guild.roles,id=00000000000)
        currMember = client.get_user(ctx.user_id)
        currMember.add_roles(roleToAdd)
    elif ctx.emoji == '🤵':
        roleToAdd = discord.utils.get(guild.roles,id=00000000000)
        currMember = client.get_user(ctx.user_id)
        currMember.add_roles(roleToAdd)
    elif ctx.emoji == '🛑':
        roleToAdd = discord.utils.get(guild.roles,id=00000000000)
        currMember = client.get_user(ctx.user_id)
        currMember.add_roles(roleToAdd)
    elif ctx.emoji == '👩‍💻':
        roleToAdd = discord.utils.get(guild.roles,id=00000000000)
        currMember = client.get_user(ctx.user_id)
        currMember.add_roles(roleToAdd)
    elif ctx.emoji == '📜':
        roleToAdd = discord.utils.get(guild.roles,id=00000000000)
        currMember = client.get_user(ctx.user_id)
        currMember.add_roles(roleToAdd)

client.run(TOKEN)
