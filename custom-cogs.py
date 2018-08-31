#Included: dark, panda, alex, dsay

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

class customcogs:
    def __init__(self, bot):
        self.bot = bot

#█▀▀▄ █▀▀█ █▀▀█ █░█
#█░░█ █▄▄█ █▄▄▀ █▀▄
#▀▀▀░ ▀░░▀ ▀░▀▀ ▀░▀
    @commands.command(pass_context=True)
    async def dark(self, ctx, member: discord.Member):
        if ctx.message.author.id == '261310324429422592':
            await self.bot.delete_message(ctx.message)
            print ("| {0} has used the dark command in {1}".format(ctx.message.author.name, ctx.message.server.name))
            print('|-----------------------------------------------------------------------------')
            embed=discord.Embed(title="", description="get rekt bud.", color=0xbfea15, timestamp=datetime.utcnow())
            embed.set_author(name="you've been dark'd", icon_url="https://darktv.xyz/wp-content/uploads/2018/05/Untitled-3-4inverted-1.gif")
            embed.set_image(url="https://darktv.xyz/wp-content/uploads/2018/05/May.gif")
            embed.set_footer(text="+dark", icon_url=spin_logo)
            await self.bot.send_message(member, embed=embed)

            embed=discord.Embed(title="", color=0xbfea15, timestamp=datetime.utcnow())
            embed.set_author(name='Command: +dark {}'.format(member.name), icon_url='https://darktv.xyz/wp-content/uploads/2018/05/May.gif')
            embed.add_field(name="Server", value="{}".format(ctx.message.server.name))
            embed.add_field(name="Channel", value="{}".format(ctx.message.channel.mention))
            embed.add_field(name="User", value="{}".format(ctx.message.author.mention))
            embed.set_thumbnail(url=ctx.message.author.avatar_url)
            embed.set_footer(text="ID: {}".format(ctx.message.id))
            await self.bot.send_message(discord.Object(id='436634502392053761'), embed=embed)
        else:
            await self.bot.say("lol nice try xd")

#█▀▀█ █▀▀█ █▀▀▄ █▀▀▄ █▀▀█
#█░░█ █▄▄█ █░░█ █░░█ █▄▄█
#█▀▀▀ ▀░░▀ ▀░░▀ ▀▀▀░ ▀░░▀
    @commands.command(pass_context=True)
    async def panda(self, ctx, member: discord.Member):
        if ctx.message.author.id == '156879556278616064':
            await self.bot.delete_message(ctx.message)
            print ("| {0} has used the panda command in {1}".format(ctx.message.author.name, ctx.message.server.name))
            print('|-----------------------------------------------------------------------------')
            embed=discord.Embed(title="", description="*usually known as the pfp machine* :panda_face:", color=0xbfea15, timestamp=datetime.utcnow())
            embed.set_author(name="you've been panda'd", icon_url="https://cdn.discordapp.com/attachments/444983335551500288/456589865677750292/image.jpg")
            embed.set_image(url="https://cdn.discordapp.com/attachments/444983335551500288/456589865677750292/image.jpg")
            embed.set_footer(text="+panda", icon_url=spin_logo)
            await self.bot.send_message(member, embed=embed)

            embed=discord.Embed(title="", color=0xbfea15, timestamp=datetime.utcnow())
            embed.set_author(name='Command: +panda {}'.format(member.name), icon_url=spin_logo)
            embed.add_field(name="Server", value="{}".format(ctx.message.server.name))
            embed.add_field(name="Channel", value="{}".format(ctx.message.channel.mention))
            embed.add_field(name="User", value="{}".format(ctx.message.author.mention))
            embed.set_thumbnail(url=ctx.message.author.avatar_url)
            embed.set_footer(text="ID: {}".format(ctx.message.id))
            await self.bot.send_message(discord.Object(id='436634502392053761'), embed=embed)
        else:
            await self.bot.say("ｓ𝔞ｄｎ𝔢ｓｓ")

#█▀▀█ █░░ █▀▀ █░█
#█▄▄█ █░░ █▀▀ ▄▀▄
#▀░░▀ ▀▀▀ ▀▀▀ ▀░▀
    @commands.command(pass_context=True)
    async def alex(self, ctx, member: discord.Member):
        if ctx.message.author.id == '224684569230573578' or ctx.message.author.id == '306226529699102720':
            await self.bot.delete_message(ctx.message)
            print ("| {0} has used the panda command in {1}".format(ctx.message.author.name, ctx.message.server.name))
            print('|-----------------------------------------------------------------------------')
            embed=discord.Embed(title="", description="*too bad your not one of them :upside_down:", color=0xbfea15, timestamp=datetime.utcnow())
            embed.set_author(name="you've been alex'd", icon_url="https://media.giphy.com/media/6WvNT8KOUeB8s0tnQI/giphy.gif")
            embed.set_image(url="https://media.giphy.com/media/6WvNT8KOUeB8s0tnQI/giphy.gif")
            embed.set_footer(text="+alex", icon_url=spin_logo)
            await self.bot.send_message(member, embed=embed)

            embed=discord.Embed(title="", color=0xbfea15, timestamp=datetime.utcnow())
            embed.set_author(name='Command: +alex {}'.format(member.name), icon_url=spin_logo)
            embed.add_field(name="Server", value="{}".format(ctx.message.server.name))
            embed.add_field(name="Channel", value="{}".format(ctx.message.channel.mention))
            embed.add_field(name="User", value="{}".format(ctx.message.author.mention))
            embed.set_thumbnail(url=ctx.message.author.avatar_url)
            embed.set_footer(text="ID: {}".format(ctx.message.id))
            await self.bot.send_message(discord.Object(id='436634502392053761'), embed=embed)
        else:
            await self.bot.say("you're not 'alex' enough.")

#█▀▀▄ █▀▀ █▀▀█ █░░█
#█░░█ ▀▀█ █▄▄█ █▄▄█
#▀▀▀░ ▀▀▀ ▀░░▀ ▄▄▄█
    @commands.command(pass_context=True)
    async def dsay(self, ctx, channel, *, mesg):
        if ctx.message.author.id == '261310324429422592':
            print ("| {0} has used the dsay command in {1}".format(ctx.message.author.name, ctx.message.server.name))
            print('|-----------------------------------------------------------------------------')
            await self.bot.delete_message(ctx.message)
            await self.bot.send_message(discord.Object(id=channel), "{}".format(mesg))
        else:
            await self.bot.say("no u")

def setup(bot):
    bot.add_cog(customcogs(bot))
