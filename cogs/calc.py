import discord
from discord.ext import commands
from io import BytesIO
import requests
from datetime import datetime
import json
import math
import textwrap


class calc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ["conc"])
    @commands.cooldown(3, 10, commands.BucketType.user)
    async def concrete(self, ctx, amount: int):
        if amount > 100000000:
            await ctx.reply(embed = discord.Embed(title ="Amount Exceeded",description="The amount must not exceed `100,000,000`",color=0xFFA500))
            return
        cementmix = amount * 5
        sand = cementmix * 5
        gravel = math.ceil(sand/0.6)
        rubble = math.ceil(gravel/12)
        sawdust = cementmix * 2
        logs = sawdust/10
        embed = discord.Embed(title = "Concrete Calculator", description = f"**Cementmix Required:** {cementmix}", color = 0xFE6000)
        embed.add_field(name = f"Sand Requirements", value = f"**Sand:** {sand}\n**Quarry Rubble:** {rubble}\n**Gravel:** {gravel}", inline = False)
        embed.add_field(name = f"\u200b\nSawdust Requirements", value = f"**Sawdust:** {sawdust}\n**Logs:** {int(logs)}", inline = False)
        embed.add_field(name = f"\u200b\nWater Requirements", value = f"**Water:** {amount}\n**Untreated Water:** {amount}\n**Acid:** {amount}\n**Toxic Waste:** {math.ceil(amount/4)}", inline = False)
        await ctx.send(f"{ctx.author.mention}, here are your results.")
        try:
            await ctx.send(embed = embed)
        except discord.errors.Forbidden:
            await ctx.send(f"{ctx.author.mention} Please allow direct messages to use this command")

    @commands.command(aliases = ['cementmix'])
    @commands.cooldown(3, 10, commands.BucketType.user)
    async def cement(self, ctx, amount: int):
        if amount > 100000000:
            await ctx.reply(embed = discord.Embed(title="Amount Exceeded", description="The amount must not exceed `100,000,000`", color=0xFFA500))
            return
        cementmix = amount * 5
        sand = cementmix * 5
        gravel = math.ceil(sand/0.6)
        rubble = math.ceil(gravel/12)
        sawdust = cementmix * 2
        logs = sawdust/10
        embed = discord.Embed(title ="Cement Mix Calculator", description = f":)", color=0xFE6000)
        embed.add_field(name = f"Sand Requirements", value = f"**Sand:** {sand}\n**Quarry Rubble:** {rubble}\n**Gravel:** {gravel}", inline = False)
        embed.add_field(name = f"\u200b\nSawdust Requirements", value = f"**Sawdust:** {sawdust}\n**Logs:** {int(logs)}", inline = False)
        await ctx.send(f"{ctx.author.mention}, here are your results.")
        try:
            await ctx.send(embed=embed)
        except discord.errors.Forbidden:
            await ctx.send(f"{ctx.author.mention} Please allow direct messages to use this command")


    @concrete.error
    async def concrete_error(self, ctx, error):           
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("You are missing a required argument. The correct usage is `>concrete [amount]`")
            return

def setup(bot):
    bot.add_cog(calc(bot))