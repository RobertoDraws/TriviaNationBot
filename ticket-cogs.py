#Included: close, request

import discord
from discord.ext import commands
from discord.ext.commands import Bot
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

class ticketcogs:
    def __init__(self, bot):
        self.bot = bot

#█▀▀ █░░ █▀▀█ █▀▀ █▀▀
#█░░ █░░ █░░█ ▀▀█ █▀▀
#▀▀▀ ▀▀▀ ▀▀▀▀ ▀▀▀ ▀▀▀
    @commands.command(pass_context=True, aliases=['close'])
    async def c(self, ctx):
        role_list = [x.name.lower() for x in ctx.message.author.roles]
        if "support team" in role_list:
            await self.bot.say("-close finished by {}".format(ctx.message.author.mention))
            await self.bot.delete_message(ctx.message)
        else:
            print ("| {0} has tried to use the c command in {1}".format(ctx.message.author.name, ctx.message.server.name))
            print('|-----------------------------------------------------------------------------')
            embed=discord.Embed(title="Permission Denied.", description="You don't have permission to use this command.", color=0xff2f2f, timestamp=datetime.utcnow())
            botmessage1 = await self.bot.say(embed=embed)
            await asyncio.sleep(5)
            await self.bot.delete_message(ctx.message)
            await self.bot.delete_message(botmessage1)

        print ("| {0} has used the c command in {1}".format(ctx.message.author.name, ctx.message.server.name))
        print('|-----------------------------------------------------------------------------')

        embed=discord.Embed(title="", color=0xbfea15, timestamp=datetime.utcnow())
        embed.set_author(name='Command: +c', icon_url=spin_logo)
        embed.add_field(name="Server", value="{}".format(ctx.message.server.name))
        embed.add_field(name="Channel", value="{}".format(ctx.message.channel.mention))
        embed.add_field(name="User", value="{}".format(ctx.message.author.mention))
        embed.set_thumbnail(url=ctx.message.author.avatar_url)
        embed.set_footer(text="ID: {}".format(ctx.message.id))
        await self.bot.send_message(discord.Object(id='436634502392053761'), embed=embed)

#█▀▀█ █▀▀ █▀▀█ █░░█ █▀▀ █▀▀ ▀▀█▀▀
#█▄▄▀ █▀▀ █░░█ █░░█ █▀▀ ▀▀█ ░░█░░
#▀░▀▀ ▀▀▀ ▀▀▀█ ░▀▀▀ ▀▀▀ ▀▀▀ ░░▀░░
    @commands.command(pass_context=True, aliases=['request'])
    async def r(self, ctx, user: discord.Member):
        role_list = [x.name.lower() for x in ctx.message.author.roles]
        if "support team" in role_list:
            await self.bot.say("**{1}**, can you please provide more evidence. This could include a screenshot of your balance at the current time or a screenshot of you on the leaderboards. After you have done so, please ping **{0}** and we will get back to you as soon as possible.".format(ctx.message.author.mention, user.mention))
            await self.bot.delete_message(ctx.message)
            await self.bot.send_message(user, "Hey {0}, you have been asked to submit more proof in **{1}** by **{2}**. Please go ahead and submit more proof so we can give you the role(s) you desire!".format(user.mention, ctx.message.channel.mention, ctx.message.author.mention))

        else:
            print ("| {0} has tried to use the c command in {1}".format(ctx.message.author.name, ctx.message.server.name))
            print('|-----------------------------------------------------------------------------')
            embed=discord.Embed(title="Permission Denied.", description="You don't have permission to use this command.", color=0xff2f2f, timestamp=datetime.utcnow())
            botmessage1 = await self.bot.say(embed=embed)
            await asyncio.sleep(5)
            await self.bot.delete_message(ctx.message)
            await self.bot.delete_message(botmessage1)

        print ("| {0} has used the r command in {1}".format(ctx.message.author.name, ctx.message.server.name))
        print('|-----------------------------------------------------------------------------')

        embed=discord.Embed(title="", color=0xbfea15, timestamp=datetime.utcnow())
        embed.set_author(name='Command: +r {}'.format(user.name), icon_url=spin_logo)
        embed.add_field(name="Server", value="{}".format(ctx.message.server.name))
        embed.add_field(name="Channel", value="{}".format(ctx.message.channel.mention))
        embed.add_field(name="User", value="{}".format(ctx.message.author.mention))
        embed.set_thumbnail(url=ctx.message.author.avatar_url)
        embed.set_footer(text="ID: {}".format(ctx.message.id))
        await self.bot.send_message(discord.Object(id='436634502392053761'), embed=embed)

    @r.error
    async def r_error(self, error, ctx):
        print ("| {0} has used the r command with an error in {1}".format(ctx.message.author.name, ctx.message.server.name))
        print('|-----------------------------------------------------------------------------')

        user = discord.Member
        embed=discord.Embed(title="", color=0xbfea15, timestamp=datetime.utcnow())
        embed.set_author(name='Invalid syntax: +r', icon_url=spin_logo)
        embed.add_field(name="Server", value="{}".format(ctx.message.server.name))
        embed.add_field(name="Channel", value="{}".format(ctx.message.channel.mention))
        embed.add_field(name="User", value="{}".format(ctx.message.author.mention))
        embed.set_thumbnail(url=ctx.message.author.avatar_url)
        embed.set_footer(text="ID: {}".format(ctx.message.id))
        await self.bot.send_message(discord.Object(id='436634502392053761'), embed=embed)

        embed=discord.Embed(title="", description="User not found!", color=0xbfea15, timestamp=datetime.utcnow())
        embed.set_author(name="Invalid Syntax".format(user.name))
        embed.add_field(name="Usage", value="+r <member>")
        embed.set_footer(text='+r', icon_url=spin_logo)
        botmessage1 = await self.bot.say(embed=embed)
        await asyncio.sleep(5)
        await self.bot.delete_message(ctx.message)
        await self.bot.delete_message(botmessage1)

def setup(bot):
    bot.add_cog(ticketcogs(bot))
