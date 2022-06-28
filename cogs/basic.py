import discord
from discord.ext import commands
import json
import requests
import connect
import math
import modules.functions as functions
from typing import Union
import asyncio
import datetime
import aiohttp
cont_amount = connect.getData(f"/faction/members.json")
publickey = 'key'
dotkey = 'key'
factionid = '297', '331', '354'
def convertMillis(milli):
    seconds=math.floor((milli/1000)%60)
    minutes=math.floor((milli/(1000*60))%60)
    hours=math.floor((milli/(1000*60*60))%24)
    return (f"{hours}h {minutes}m {seconds}s")

class basic(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def slap(self, ctx, user: discord.Member):
        await ctx.send(f"{ctx.author.mention} delivers an almighty backhand to the face of {user.mention}!")

    @commands.command()
    async def dxp(self, ctx):

        dxpServers = ""
        servers = requests.get("https://cdn.tycoon.community/servers.json", verify=True).json()
        for server in servers['servers']:

            serverID = server['id']
            serverEndpoint = server['backup']
            serverName = server['name']
            serverLink = f"https://cfx.re/join/{serverID}"

            if server['number'] == "L":
                continue
            try:
                players = requests.get(serverEndpoint + "status/widget/players.json")
                players = players.json()
            except:
                players = "N/A"
            if players != "N/A":
                if players["server"]["dxp"][0] == True:
                    dxp = players["server"]["dxp"]
                    timeRemaining = f"{convertMillis(dxp[2])}"
                    if dxp[3] > 0:
                        extraTime = convertMillis(dxp[3])
                        timeRemaining = timeRemaining + f"(+ {extraTime})"
                    dxpServers += f"\nDXP on [{serverName}]({serverLink}) for {timeRemaining}"
                elif players["server"]["dxp"][0] == False:
                    pass
        if dxpServers == "": 
            dxpServers = "No active DXP servers."
        embed = discord.Embed(title = "DXP Check", description = dxpServers, color = 0x23272a)
        await ctx.send(embed = embed)

    @commands.command()
    async def user(self, ctx, discord_id, user: Union[discord.Member, int] = None):
        if user is None:
            user = ctx.author
        elif isinstance(user, int):
            user = await self.bot.fetch_user(user)    

        if discord_id.isnumeric() == False:
            await ctx.send("The discord ID or Transport Tycoon user ID must be numeric")
            return
        if len(discord_id) == 18:
            discordID_data = connect.getData(f"/snowflake2user/{discord_id}")
            if discordID_data == "400":
                await ctx.send("Code 400: No user found with that Discord ID")
            elif discordID_data == "423":
                await ctx.send("Code 423: This users data is locked.")
            elif discordID_data == "412":
                await ctx.send("Code 412: User not found")
            elif discordID_data is None:
                await ctx.send(f"{str(discordID_data)} Unable to connect")
            else:


                user_id = discordID_data.json()
                user_id = str(user_id.get('user_id'))
                wealth = connect.getData(f"/wealth/{user_id}").json()
                userID_data = connect.getData(f"/getuserfaq/{user_id}")
                get_faction = userID_data.json()
                faction_tag = connect.getData(f"/faction/info.json").json()
                faction_id = str(get_faction.get('faction_id'))

                username = None
                for players in connect.getData(f"/widget/players.json").json()['players']:
                        break

                print(players)

                
                await ctx.send(embed=functions.embed_generator(self.bot, f"Username: {players[0]} \nUser ID: {user_id} \nFaction ID: {faction_id} \nFaction Name(broken): {faction_tag['name']} \nWealth: ${wealth['wallet'] + wealth['bank'] - wealth['loan']:,}", colour=0x23272a))


        elif len(discord_id) <= 6:
            userID_data = connect.getData(f"/getuserfaq/{discord_id}")
            if userID_data == "400":
                await ctx.send("Code 400: No user found with that Discord ID")
            elif userID_data == "423":
                await ctx.send("Code 423: This users data is locked.")
            elif userID_data == "412":
                await ctx.send("Code 412: User not found")
            elif userID_data is None:
                await ctx.send(f"{str(userID_data)} Unable to connect")
                
            else:
                get_faction = userID_data.json()
                faction_id = str(get_faction.get('faction_id'))
                await ctx.send(f"User ID: {discord_id} \nFaction ID: {faction_id} \nWealth: {wealth}")
        else:
            await ctx.send("You must enter either a valid discord ID or valid Transport Tycoon user ID") 


    @commands.command()
    @commands.cooldown(1, 60, commands.BucketType.user)
    async def bully(self, ctx, user: discord.Member):
        if user.id == '600339505844584478':
            await ctx.send(f".hardmute {ctx.author.mention} 5s Wow, I can't believe you'd try that.")
        else:
            await ctx.send(f"Hey, {user.mention}, you fucker... {ctx.author.mention} wants to give you this...", delete_after=60)
        await ctx.send(f"{user.mention}", delete_after=60)
        await ctx.send(f"{user.mention}", delete_after=60)
        await ctx.send(f"{user.mention}", delete_after=60)
        await ctx.send(f"{user.mention}", delete_after=60)
        await ctx.send(f"{user.mention}", delete_after=60)
        await ctx.send(f"{user.mention}", delete_after=60)
        await ctx.send(f"{user.mention}", delete_after=60)
        await ctx.send(f"{user.mention}", delete_after=60)
        await ctx.send(f"{user.mention}", delete_after=60)
        await ctx.send(f"{user.mention}", delete_after=60)
        await ctx.send(f"{user.mention}", delete_after=60)
        await ctx.send(f"{user.mention}", delete_after=60)
        await ctx.send(f"{user.mention}", delete_after=60)
        await ctx.send(f"{user.mention}", delete_after=60)
        await ctx.send(f"{user.mention}", delete_after=60)
        await ctx.send(f"{user.mention}", delete_after=60)
        await ctx.send(f"{user.mention}", delete_after=60)
        await ctx.send(f"{user.mention}", delete_after=60)
        await ctx.send(f"{user.mention}", delete_after=60)
        await ctx.send(f"{user.mention}", delete_after=60)
        await ctx.send(f"{user.mention}", delete_after=60)
        await ctx.send(f"{user.mention}", delete_after=60)
        await ctx.send(f"{user.mention}", delete_after=60)
        await ctx.send(f"{user.mention}", delete_after=60)
        await ctx.send(f"{user.mention}", delete_after=60)
        await ctx.send(f"{user.mention}", delete_after=60)
        await ctx.send(f"{user.mention}", delete_after=60)
        await ctx.send(f"{user.mention}", delete_after=60)
        await ctx.send(f"{user.mention}", delete_after=60)
        await ctx.send(f"{user.mention}", delete_after=60)
        await ctx.send(f"{user.mention}", delete_after=60)
        await ctx.send(f"{user.mention}", delete_after=60)
        await ctx.send(f"{user.mention}", delete_after=60)
        await ctx.send(f"{user.mention}", delete_after=60)
        await ctx.send(f"{user.mention}", delete_after=60)
        await ctx.send(f"{user.mention}", delete_after=60)
        await ctx.send(f"{user.mention}", delete_after=60)
        await ctx.send(f"{user.mention}", delete_after=60)
        await ctx.send(f"{user.mention}", delete_after=60)
        await ctx.send(f"{user.mention}", delete_after=60)
        await ctx.send(f"Ha, fuckin' nerd.")
        return

    @commands.command()
    async def infoE(self, ctx):            
        data = connect.getData("/faction/info.json", (publickey))
        factioninfo = data.json()
        name = factioninfo.get('name')
        tag = factioninfo.get('tag')
        faction_id = factioninfo.get('faction_id')
        faction_id = str(faction_id)
        await ctx.send(f"**Faction Information**\n Name: {name}\n Tag: {tag}\n Faction ID: {faction_id} ")  

    @commands.command()
    async def sotd(self, ctx):
        sotd = connect.getData(f"/sotd.json").json()

        await ctx.send(embed=functions.embed_generator(self.bot, f"**The Skill of the Day is:** \n__{sotd['skill']}__ \n**Bonus:** \n__{sotd['bonus']}%__"))
        return


    #Errors


    #@user.error
    #sync def user_error(self, ctx, error):
      #  if isinstance(error, commands.CommandInvokeError):
       #     await ctx.send(embed=functions.embed_generator(self.bot, f"This user is not online, please try again when they are in game.", 0xFF0000))
        ##else:
          #  await ctx.send(embed =functions.embed_generator(self.bot, f"Something went wrong, contact Goobie", 0xFF0000))

                                                       
    @bully.error
    async def bully_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(embed=functions.embed_generator(self.bot, f"Hey, you big fuckin' dummy! Stop spamming this shit, or else! wait 60 seconds before trying again.", 0xFF0000))
            return


def setup(bot):
    bot.add_cog(basic(bot))