#Included: clear

import discord
from discord.ext import commands
from discord.ext.commands import bot
from discord.utils import find
import asyncio
import logging
import os
import time
import requests
import random
from time import localtime, strftime
from datetime import datetime
import subprocess
import colorama
from itertools import cycle
from discord.utils import find

spin_logo = "https://cdn.discordapp.com/attachments/411306798042054657/471067301408538635/Trivia_Nation_Logo_HQ.jpg"
red = "0xff2f2f"
green = "0xbfea15"

class staffcogs:
    def __init__(self, bot):
        self.bot = bot


#█▀▀ █░░ █▀▀ █▀▀█ █▀▀█
#█░░ █░░ █▀▀ █▄▄█ █▄▄▀
#▀▀▀ ▀▀▀ ▀▀▀ ▀░░▀ ▀░▀▀
    @commands.command(pass_context = True)
    async def clear(self, ctx, number: int):

        embed=discord.Embed(title="", color=0xbfea15, timestamp=datetime.utcnow())
        embed.set_author(name='Command: +clear {}'.format(number), icon_url=spin_logo)
        embed.add_field(name="Server", value="{}".format(ctx.message.server.name))
        embed.add_field(name="Channel", value="{}".format(ctx.message.channel.mention))
        embed.add_field(name="Staff", value="{}".format(ctx.message.author.mention))
        embed.set_thumbnail(url=ctx.message.author.avatar_url)
        embed.set_footer(text="ID: {}".format(ctx.message.id))
        await self.bot.send_message(discord.Object(id='436634502392053761'), embed=embed)

        role_list = [x.name.lower() for x in ctx.message.author.roles]
        if "junior moderator" or "moderator" or "developer" or "head moderator" or "administrator" in role_list:
            print ("| {0} has used the clear command in {1}".format(ctx.message.author.name, ctx.message.server.name))
            print('|-----------------------------------------------------------------------------')
            mgs = []
            async for x in self.bot.logs_from(ctx.message.channel, limit = number):
                mgs.append(x)
            await self.bot.delete_messages(mgs)
            embed=discord.Embed(title="Messages Cleared! :white_check_mark:", color=0xbfea15, timestamp=datetime.utcnow())
            botmessage = await self.bot.say(embed=embed)
            await asyncio.sleep(5)
            await self.bot.delete_message(botmessage)
        else:
            print ("| {0} has tried to use the clear command in {1}".format(ctx.message.author.name, ctx.message.server.name))
            print('|-----------------------------------------------------------------------------')
            embed=discord.Embed(title="Permission Denied.", description="You don't have permission to use this command.", color=0xff2f2f, timestamp=datetime.utcnow())
            botmessage1 = await self.bot.say(embed=embed)
            await asyncio.sleep(5)
            await self.bot.delete_message(ctx.message)
            await self.bot.delete_message(botmessage1)

    @clear.error
    async def clear_error(self, error, ctx):
        print ("| {0} has used the clear command with an error in {1}".format(ctx.message.author.name, ctx.message.server.name))
        print('|-----------------------------------------------------------------------------')

        user = discord.Member
        embed=discord.Embed(title="", color=0xbfea15, timestamp=datetime.utcnow())
        embed.set_author(name='Invalid syntax: +clear', icon_url=spin_logo)
        embed.add_field(name="Server", value="{}".format(ctx.message.server.name))
        embed.add_field(name="Channel", value="{}".format(ctx.message.channel.mention))
        embed.add_field(name="User", value="{}".format(ctx.message.author.mention))
        embed.set_thumbnail(url=ctx.message.author.avatar_url)
        embed.set_footer(text="ID: {}".format(ctx.message.id))
        await self.bot.send_message(discord.Object(id='436634502392053761'), embed=embed)

        embed=discord.Embed(title="", description="Make sure that the amount is between 2 and 100!", color=0xbfea15, timestamp=datetime.utcnow())
        embed.set_author(name="Invalid Syntax".format(user.name))
        embed.add_field(name="Usage", value="+clear <amount>")
        embed.set_footer(text='+clear', icon_url=spin_logo)
        botmessage1 = await self.bot.say(embed=embed)
        await asyncio.sleep(5)
        await self.bot.delete_message(ctx.message)
        await self.bot.delete_message(botmessage1)

def setup(bot):
    bot.add_cog(staffcogs(bot))
