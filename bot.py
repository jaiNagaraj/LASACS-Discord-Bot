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
    guild = client.get_guild(int(GUILD)) #LASA CS ID

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )
    roleChannelExists = False
    for r in guild.text_channels:
        global roleChannel
        roleChannel = None
        print(str(r))
        if str(r) == 'get-roles':
            roleChannelExists = True
            roleChannel = r
    if not roleChannelExists:
        global newRoleChannel
        newRoleChannel = await guild.create_text_channel('get-roles',position=2,topic='Get your roles here!')
        rolMsg = await newRoleChannel.send(
            """
            **Come get your roles, folks!**
            Make sure to react accordingly to get roles that fit YOU! Hold down Shift to select multiple reactions.\n
            *Grade Roles*:
            `9th Grade` react with 🤓
            `10th Grade` react with 🤠
            `11th Grade` react with 😎
            `12th Grade` react with 🧐
            `Alumni` react with 🧓
            \n
            *CS Classes*:
            `Intro to CS` react with 👶
            `AP CS` react with 😊
            `Advanced CS` react with 🤑
            `Independent Study` react with 💪
            `Web and Mobile` react with 📱
            `Digital Electronics` react with 💽
            \n
            *Clubs*
            `Hack Club` react with 🔍
            `CS Club` react with 🦸‍♂️
            `Programming in Practice` react with 🤵
            `Cyberpatriot` react with 🛑
            `WiCS+` react with 👩‍💻
            `RaptorWorks Data Science` react with 📜
            \n
            And make sure you get this one!
            `Members` react with ✊
            """
        )
        await rolMsg.add_reaction('🤓')
        await rolMsg.add_reaction('🤠')
        await rolMsg.add_reaction('😎')
        await rolMsg.add_reaction('🧐')
        await rolMsg.add_reaction('🧓')
        await rolMsg.add_reaction('👶')
        await rolMsg.add_reaction('😊')
        await rolMsg.add_reaction('🤑')
        await rolMsg.add_reaction('💪')
        await rolMsg.add_reaction('📱')
        await rolMsg.add_reaction('💽')
        await rolMsg.add_reaction('🔍')
        await rolMsg.add_reaction('🦸‍♂️')
        await rolMsg.add_reaction('🤵')
        await rolMsg.add_reaction('🛑')
        await rolMsg.add_reaction('👩‍💻')
        await rolMsg.add_reaction('📜')
        await rolMsg.add_reaction('✊')

#greet newcomers
@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hey there {member.name}! Welcome to the LASA CS discord. Don\'t be afraid to say hi in #general, and make sure to get your role in the get-roles channel!'
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
        await message.channel.send("I am a bot, and I sometimes make mistakes. If you think that what you said was appropriate and/or have questions, please DM jaragan.")
@client.event
async def on_raw_reaction_add(ctx):
    guild = client.get_guild(int(GUILD))
    myMoji = (ctx.emoji.name)
    msg = await guild.get_channel(ctx.channel_id).fetch_message(ctx.message_id)
    if not (roleChannel is None):
        myRoleChannel = roleChannel
    else:
        myRoleChannel = newRoleChannel
    if ctx.channel_id != myRoleChannel.id or guild.get_member(ctx.user_id).name == 'Jaragan Test Bot': # CORRECT THIS NAME, MIGHT BE DIFFERENT
        return
    if myMoji == '🤓':
        roleToAdd = discord.utils.get(guild.roles,id=947698094877868072)
        currMember = guild.get_member(ctx.user_id)
        await currMember.add_roles(roleToAdd)
    elif myMoji == '🤠':
        roleToAdd = discord.utils.get(guild.roles,id=947697781252952076)
        currMember = guild.get_member(ctx.user_id)
        await currMember.add_roles(roleToAdd)
    elif myMoji == '😎':
        roleToAdd = discord.utils.get(guild.roles,id=947697823950962689)
        currMember = guild.get_member(ctx.user_id)
        await currMember.add_roles(roleToAdd)
    elif myMoji == '🧐':
        roleToAdd = discord.utils.get(guild.roles,id=947697850383478864)
        currMember = guild.get_member(ctx.user_id)
        await currMember.add_roles(roleToAdd)
    elif myMoji == '🧓':
        roleToAdd = discord.utils.get(guild.roles,id=947697898253090856)
        currMember = guild.get_member(ctx.user_id)
        await currMember.add_roles(roleToAdd)
    elif myMoji == '👶':
        roleToAdd = discord.utils.get(guild.roles,id=807088268423856148)
        currMember = guild.get_member(ctx.user_id)
        await currMember.add_roles(roleToAdd)
    elif myMoji == '😊':
        roleToAdd = discord.utils.get(guild.roles,id=807089136635871252)
        currMember = guild.get_member(ctx.user_id)
        await currMember.add_roles(roleToAdd)
    elif myMoji == '🤑':
        roleToAdd = discord.utils.get(guild.roles,id=803712717692207104)
        currMember = guild.get_member(ctx.user_id)
        await currMember.add_roles(roleToAdd)
    elif myMoji == '💪':
        roleToAdd = discord.utils.get(guild.roles,id=807088371729825832)
        currMember = guild.get_member(ctx.user_id)
        await currMember.add_roles(roleToAdd)
    elif myMoji == '📱':
        roleToAdd = discord.utils.get(guild.roles,id=807088201238970388)
        currMember = guild.get_member(ctx.user_id)
        await currMember.add_roles(roleToAdd)
    elif myMoji == '💽':
        roleToAdd = discord.utils.get(guild.roles,id=803721581544865854)
        currMember = guild.get_member(ctx.user_id)
        await currMember.add_roles(roleToAdd)
    elif myMoji == '🔍':
        roleToAdd = discord.utils.get(guild.roles,id=804783485221994527)
        currMember = guild.get_member(ctx.user_id)
        await currMember.add_roles(roleToAdd)
    elif myMoji == '🦸‍♂️':
        roleToAdd = discord.utils.get(guild.roles,id=803713243213594635)
        currMember = guild.get_member(ctx.user_id)
        await currMember.add_roles(roleToAdd)
    elif myMoji == '🤵':
        roleToAdd = discord.utils.get(guild.roles,id=803721615958474752)
        currMember = guild.get_member(ctx.user_id)
        await currMember.add_roles(roleToAdd)
    elif myMoji == '🛑':
        roleToAdd = discord.utils.get(guild.roles,id=803712882071175169)
        currMember = guild.get_member(ctx.user_id)
        await currMember.add_roles(roleToAdd)
    elif myMoji == '👩‍💻':
        roleToAdd = discord.utils.get(guild.roles,id=803712678043975720)
        currMember = guild.get_member(ctx.user_id)
        await currMember.add_roles(roleToAdd)
    elif myMoji == '📜':
        roleToAdd = discord.utils.get(guild.roles,id=1014706106393710633)
        currMember = guild.get_member(ctx.user_id)
        await currMember.add_roles(roleToAdd)
    elif myMoji == '✊':
        roleToAdd = discord.utils.get(guild.roles,id=947652632762282085)
        currMember = guild.get_member(ctx.user_id)
        await currMember.add_roles(roleToAdd)

client.run(TOKEN)
