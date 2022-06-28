import discord
import json
import requests
from discord.ext import commands
import os
import math

with open('db/config.json') as fp:
    config = json.load(fp)

def convertMillis(milli):
    seconds=math.floor((milli/1000)%60)
    minutes=math.floor((milli/(1000*60))%60)
    hours=math.floor((milli/(1000*60*60))%24)
    return (f"{hours}h {minutes}m {seconds}s")

token = 'tokengohere'
api_key = 'apikeyhere'
client = discord.Client()
client = commands.Bot(command_prefix=config["bot_prefix"], help_command=None)



@client.event
async def on_ready():
    await client.change_presence(status = discord.Status.online, activity = discord.Activity(type=discord.ActivityType.watching, name = "For Dannies!"))
    print("Bot is online")

@client.command()
@commands.cooldown(3, 10, commands.BucketType.user)
async def ping(ctx):
    embed = discord.Embed(title = "Pong! :grinning:", description =f"`Ping is : {round(client.latency*1000)}ms`", colour= 0xFE6000)
    msg=await ctx.channel.send(embed=embed)
    await msg.add_reaction("🏓")

@client.event
async def on_message_delete(message):
    async for entry in message.guild.audit_logs(limit=1, action=discord.AuditLogAction.message_delete):
        if entry.user.bot:
            return
        if message.user.bot:
            return
        delete_message_embed = discord.Embed(title='{} has deleted a message'.format(message.author), description=f"`{message.content}`")
        delete_message_embed.add_field(name='Channel', value=f'#{message.channel.name}')
        channel = client.get_channel(824766159554478160)
        await channel.send(embed=delete_message_embed)

class MessageEdit:
    def __init__(self, bot):
        self.bot = bot

@client.event
async def on_message_edit(message_before, message_after):
    if message_before.author.bot:
        return
    if message_after.author.bot:
        return
    else:
        embed=discord.Embed(title="{} edited a message".format(message_before.author), description="")
    embed.add_field(name= message_before.content ,value="Before", inline=False)
    embed.add_field(name= message_after.content ,value="After", inline=False)
    channel=client.get_channel(824766159554478160)
    await channel.send(embed=embed)

for filename in os.listdir("./cogs"):
	if filename.endswith(".py"):
		client.load_extension(f"cogs.{filename[:-3]}")
        
print("All Cogs loaded successfully")
                
client.run(token)