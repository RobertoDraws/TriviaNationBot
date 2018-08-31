#Included: help, poll, ping, info, botinfo

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

class maincogs:
    def __init__(self, bot):
        self.bot = bot


#█░░█ █▀▀ █░░ █▀▀█
#█▀▀█ █▀▀ █░░ █░░█
#▀░░▀ ▀▀▀ ▀▀▀ █▀▀▀
    @commands.command(pass_context=True)
    async def help(self, ctx, topic):
        if topic.upper() == "MAIN" or topic.upper() == "M":
            embed=discord.Embed(title="Trivia Nation Commands (Main) DMed! :white_check_mark:", color=0xbfea15, timestamp=datetime.utcnow())
            embed.set_footer(text='+help main')
            await self.bot.say(embed=embed)

            embed=discord.Embed(title="", description="Command Preference is: '+'", color=0xbfea15, timestamp=datetime.utcnow())
            embed.set_author(name='Trivia Nation Commands (Main)', icon_url=spin_logo)
            embed.set_thumbnail(url=spin_logo)
            embed.add_field(name="Main Commands:", value="**+help <topic>** *Displays a help message based on a topic.*\n**+botinfo** *Find out information about the bot and bot dev.* \n**+info <member>** *Find information about a specific member.* \n**+serverinfo** *Find information about the server.* \n**+doge** *See a random picture of a dog.*\n**+warm <member>** *Make a member :fire:.* \n**+cookie <member>** *Gives your favorite person a :cookie:.*\n**+fish** *Attempt to capture the rarest fish in the sea.*\n**+farmy/farm** *Farm to test your luck.*\n**+sport/play** *What will you do?.* \n**+poll/p <topic>** *This allows you to make a poll which anyone can respond to.* \n**+suggest <idea>** *Posts a suggestion which will then be reviewed by staff.*\n**+eightball/8ball <question>** *Ask the 8ball a question.* \n**+coinflip/coin/flip <option 1> | <option 2>** *Flip a coin to see who/that wins.*", inline=False)
            embed.set_footer(text='+help main', icon_url=spin_logo)
            await self.bot.send_message(ctx.message.author, embed=embed)

            print ("| {0} has used the help (main) command in {1}".format(ctx.message.author.name, ctx.message.server.name))
            print('|-----------------------------------------------------------------------------')
            embed=discord.Embed(title="", color=0xbfea15, timestamp=datetime.utcnow())
            embed.set_author(name='Command: +help main', icon_url=spin_logo)
            embed.add_field(name="Server", value="{}".format(ctx.message.server.name))
            embed.add_field(name="Channel", value="{}".format(ctx.message.channel.mention))
            embed.add_field(name="User", value="{}".format(ctx.message.author.mention))
            embed.set_thumbnail(url=ctx.message.author.avatar_url)
            embed.set_footer(text="ID: {}".format(ctx.message.id))
            await self.bot.send_message(discord.Object(id='436634502392053761'), embed=embed)

        if topic.upper() == "STAFF" or topic.upper() == "S":
            embed=discord.Embed(title="Trivia Nation Commands (Staff) DMed! :white_check_mark:", color=0xbfea15, timestamp=datetime.utcnow())
            embed.set_footer(text='+help staff')
            await self.bot.say(embed=embed)

            embed=discord.Embed(title="", description="Command Preference is: '+'", color=0xbfea15, timestamp=datetime.utcnow())
            embed.set_author(name='Trivia Nation Commands (Staff)', icon_url=spin_logo)
            embed.set_thumbnail(url=spin_logo)
            embed.add_field(name="Staff Commands:", value="__NOTE:__ *These commands can only be used by Staff.* \n**+clear <amount>** *Clears set amount of messages.*", inline=False)
            embed.set_footer(text='+help staff', icon_url=spin_logo)
            await self.bot.send_message(ctx.message.author, embed=embed)

            print ("| {0} has used the help (staff) command in {1}".format(ctx.message.author.name, ctx.message.server.name))
            print('|-----------------------------------------------------------------------------')
            embed=discord.Embed(title="", color=0xbfea15, timestamp=datetime.utcnow())
            embed.set_author(name='Command: +help staff', icon_url=spin_logo)
            embed.add_field(name="Server", value="{}".format(ctx.message.server.name))
            embed.add_field(name="Channel", value="{}".format(ctx.message.channel.mention))
            embed.add_field(name="User", value="{}".format(ctx.message.author.mention))
            embed.set_thumbnail(url=ctx.message.author.avatar_url)
            embed.set_footer(text="ID: {}".format(ctx.message.id))
            await self.bot.send_message(discord.Object(id='436634502392053761'), embed=embed)

        if topic.upper() == "ROLES" or topic.upper() == "ROLE" or topic.upper() == "R":
            embed=discord.Embed(title="Trivia Nation Commands (Role) DMed! :white_check_mark:", color=0xbfea15, timestamp=datetime.utcnow())
            embed.set_footer(text='+help role')
            await self.bot.say(embed=embed)

            embed=discord.Embed(title="", description="__NOTE:__ *These commands can only be used by Staff!*\nCommand Preference is: '+'", color=0xbfea15, timestamp=datetime.utcnow())
            embed.set_author(name='Trivia Nation Commands (Roles)', icon_url=spin_logo)
            embed.set_thumbnail(url=spin_logo)
            embed.add_field(name="Multiple Role Commands:", value="**Usage: +roles/role/addroles/addrole/aroles/arole <member> <role(s)>** *Adds role(s) to member specified.* \n**Usage: +delroles/delrole/droles/drole <member> <role(s)>** *Removes role(s) to member specified.* \n__**Possibilities:**__ \n**hqtrivia/hq** - HQ Trivia \n**joyride/jr** - Joyride \n**cashshow/cs** - Cash Show\n**hangtime/ht** - HangTime \n**hypsports/hyp** - HypSports \n**quizbiz/qb**- QuizBiz \n**beattheq/btq** - Beat The Q\n**swagiq/siq** - Swag IQ\n**halftimelive/htl** - Halftime Live\n**ripkord/rk** - Ripkord\n**majorityrules/mjr** - Majority Rules", inline=True)
            embed.add_field(name="Ticket Commands:", value="**+c/close** *Closes the ticket.* \n**+r/request <member>** *Tells the member requesting roles to add additonal proof to their ticket.*", inline=False)
            embed.set_footer(text='+help roles', icon_url=spin_logo)
            await self.bot.send_message(ctx.message.author, embed=embed)

            print ("| {0} has used the help (roles) command in {1}".format(ctx.message.author.name, ctx.message.server.name))
            print('|-----------------------------------------------------------------------------')
            embed=discord.Embed(title="", color=0xbfea15, timestamp=datetime.utcnow())
            embed.set_author(name='Command: +help roles', icon_url=spin_logo)
            embed.add_field(name="Server", value="{}".format(ctx.message.server.name))
            embed.add_field(name="Channel", value="{}".format(ctx.message.channel.mention))
            embed.add_field(name="User", value="{}".format(ctx.message.author.mention))
            embed.set_thumbnail(url=ctx.message.author.avatar_url)
            embed.set_footer(text="ID: {}".format(ctx.message.id))
            await self.bot.send_message(discord.Object(id='436634502392053761'), embed=embed)

    @help.error
    async def help_error(self, error, ctx):
        print ("| {0} has used the help command with an error in {1}".format(ctx.message.author.name, ctx.message.server.name))
        print('|-----------------------------------------------------------------------------')
        embed=discord.Embed(title="", color=0xbfea15, timestamp=datetime.utcnow())
        embed.set_author(name='Invalid syntax: +help', icon_url=spin_logo)
        embed.add_field(name="Server", value="{}".format(ctx.message.server.name))
        embed.add_field(name="Channel", value="{}".format(ctx.message.channel.mention))
        embed.add_field(name="User", value="{}".format(ctx.message.author.mention))
        embed.set_thumbnail(url=ctx.message.author.avatar_url)
        embed.set_footer(text="ID: {}".format(ctx.message.id))
        await self.bot.send_message(discord.Object(id='436634502392053761'), embed=embed)

        user = discord.Member
        embed=discord.Embed(title="", description="You can use: \n**+help main/m** *Displays the main commands.* \n**+help staff/s** *Displays the staff commands.* \n**+help roles/role/s** *Displays the command(s) staff use to apply roles.*", color=0xbfea15, timestamp=datetime.utcnow())
        embed.set_author(name='Trivia Nation Commands (Topics)', icon_url=spin_logo)
        embed.add_field(name="Usage", value="+help <topic>")
        embed.set_thumbnail(url=spin_logo)
        embed.set_footer(text='+help', icon_url=spin_logo)
        botmessage1 = await self.bot.say(embed=embed)
        await asyncio.sleep(15)
        await self.bot.delete_message(ctx.message)
        await self.bot.delete_message(botmessage1)

#█▀▀█ █▀▀█ █░░ █░░
#█░░█ █░░█ █░░ █░░
#█▀▀▀ ▀▀▀▀ ▀▀▀ ▀▀▀
    @commands.command(pass_context=True, aliases=['p'])
    async def poll(self, ctx, *, mesg):
        await self.bot.delete_message(ctx.message)
        embed = discord.Embed(title="", description='{}'.format(mesg), color=0xbfea15, timestamp=datetime.utcnow())
        embed.set_author(name='{} has started a poll'.format(ctx.message.author.name), icon_url=spin_logo)
        embed.set_footer(text='+poll', icon_url=spin_logo)
        botmessage = await self.bot.say(embed=embed)
        await self.bot.add_reaction(message=botmessage, emoji='👍')
        await self.bot.add_reaction(message=botmessage, emoji='👎')
        await self.bot.add_reaction(message=botmessage, emoji='🤷')

        print("| {0} has used the poll command in {1}".format(ctx.message.author.name, ctx.message.server.name))
        print('|-----------------------------------------------------------------------------')
        embed = discord.Embed(title="", color=0xbfea15, timestamp=datetime.utcnow())
        embed.set_author(name='Command: +poll {}'.format(mesg), icon_url=spin_logo)
        embed.add_field(name="Server", value="{}".format(ctx.message.server.name))
        embed.add_field(name="Channel", value="{}".format(ctx.message.channel.mention))
        embed.add_field(name="User", value="{}".format(ctx.message.author.mention))
        embed.set_thumbnail(url=ctx.message.author.avatar_url)
        embed.set_footer(text="ID: {}".format(ctx.message.id))
        await self.bot.send_message(discord.Object(id='436634502392053761'), embed=embed)

    @poll.error
    async def poll_error(self, error, ctx):
        print("| {0} has used the poll command with an error in {1}".format(ctx.message.author.name, ctx.message.server.name))
        print('|-----------------------------------------------------------------------------')
        embed = discord.Embed(title="", color=0xbfea15, timestamp=datetime.utcnow())
        embed.set_author(name='Invalid syntax: +poll', icon_url=spin_logo)
        embed.add_field(name="Server", value="{}".format(ctx.message.server.name))
        embed.add_field(name="Channel", value="{}".format(ctx.message.channel.mention))
        embed.add_field(name="User", value="{}".format(ctx.message.author.mention))
        embed.set_thumbnail(url=ctx.message.author.avatar_url)
        embed.set_footer(text="ID: {}".format(ctx.message.id))
        await self.bot.send_message(discord.Object(id='436634502392053761'), embed=embed)

        user = discord.Member
        embed = discord.Embed(title="", description="You must include what you want the poll to be about.", color=0xbfea15, timestamp=datetime.utcnow())
        embed.set_author(name="Invalid Syntax".format(user.name))
        embed.add_field(name="Usage", value="+poll <topic>")
        embed.set_footer(text='+poll', icon_url=spin_logo)
        botmessage1 = await self.bot.say(embed=embed)
        await asyncio.sleep(5)
        await self.bot.delete_message(ctx.message)
        await self.bot.delete_message(botmessage1)

#█▀▀█ ░▀░ █▀▀▄ █▀▀▀
#█░░█ ▀█▀ █░░█ █░▀█
#█▀▀▀ ▀▀▀ ▀░░▀ ▀▀▀▀
    @commands.command(pass_context=True)
    async def ping(self, ctx):
        channel = ctx.message.channel
        t1 = time.perf_counter()
        await self.bot.send_typing(channel)
        t2 = time.perf_counter()
        embed=discord.Embed(title=':ping_pong: Pong! {}ms'.format(round((t2-t1)*1000)), color=0xbfea15, timestamp=datetime.utcnow())
        embed.set_footer(text='+pong', icon_url=spin_logo)
        await self.bot.say(embed=embed)

        print ("| {0} has used the ping command in {1}".format(ctx.message.author.name, ctx.message.server.name))
        print('|-----------------------------------------------------------------------------')
        embed=discord.Embed(title="", color=0xbfea15, timestamp=datetime.utcnow())
        embed.set_author(name='Command: +ping', icon_url=spin_logo)
        embed.add_field(name="Server", value="{}".format(ctx.message.server.name))
        embed.add_field(name="Channel", value="{}".format(ctx.message.channel.mention))
        embed.add_field(name="User", value="{}".format(ctx.message.author.mention))
        embed.set_thumbnail(url=ctx.message.author.avatar_url)
        embed.set_footer(text="ID: {}".format(ctx.message.id))
        await self.bot.send_message(discord.Object(id='436634502392053761'), embed=embed)

#░▀░ █▀▀▄ █▀▀ █▀▀█
#▀█▀ █░░█ █▀▀ █░░█
#▀▀▀ ▀░░▀ ▀░░ ▀▀▀▀
    @commands.command(pass_context=True)
    async def info(self, ctx, user: discord.Member):
        embed=discord.Embed(title="", description="Here's what I could find.", color=0xbfea15, timestamp=datetime.utcnow())
        embed.set_author(name="{}'s info".format(user.name), icon_url=user.avatar_url)
        embed.add_field(name="Name", value=user.name, inline=True)
        embed.add_field(name="ID", value=user.id, inline=True)
        embed.add_field(name="Status", value=user.status, inline=True)
        embed.add_field(name="Highest role", value=user.top_role)
        embed.add_field(name="Joined", value=user.joined_at)
        embed.set_thumbnail(url=user.avatar_url)
        embed.set_footer(text='+info {}'.format(user.name), icon_url=spin_logo)
        await self.bot.say(embed=embed)

        print ("| {0} has used the info command in {1}".format(ctx.message.author.name, ctx.message.server.name))
        print('|-----------------------------------------------------------------------------')
        embed=discord.Embed(title="", color=0xbfea15, timestamp=datetime.utcnow())
        embed.set_author(name='Command: +info {}'.format(user.name), icon_url=spin_logo)
        embed.add_field(name="Server", value="{}".format(ctx.message.server.name))
        embed.add_field(name="Channel", value="{}".format(ctx.message.channel.mention))
        embed.add_field(name="User", value="{}".format(ctx.message.author.mention))
        embed.set_thumbnail(url=ctx.message.author.avatar_url)
        embed.set_footer(text="ID: {}".format(ctx.message.id))
        await self.bot.send_message(discord.Object(id='436634502392053761'), embed=embed)

    @info.error
    async def info_error(self, error, ctx):
        print ("| {0} has used the info command with an error in {1}".format(ctx.message.author.name, ctx.message.server.name))
        print('|-----------------------------------------------------------------------------')
        embed=discord.Embed(title="", color=0xbfea15, timestamp=datetime.utcnow())
        embed.set_author(name='Invalid syntax: +info', icon_url=spin_logo)
        embed.add_field(name="Server", value="{}".format(ctx.message.server.name))
        embed.add_field(name="Channel", value="{}".format(ctx.message.channel.mention))
        embed.add_field(name="User", value="{}".format(ctx.message.author.mention))
        embed.set_thumbnail(url=ctx.message.author.avatar_url)
        embed.set_footer(text="ID: {}".format(ctx.message.id))
        await self.bot.send_message(discord.Object(id='436634502392053761'), embed=embed)

        user = discord.Member
        embed=discord.Embed(title="", description="This command finds information about a specific member.", color=0xbfea15, timestamp=datetime.utcnow())
        embed.set_author(name="Invalid Syntax".format(user.name))
        embed.add_field(name="Usage", value="+info <member>")
        embed.set_footer(text='+info', icon_url=spin_logo)
        botmessage1 = await self.bot.say(embed=embed)
        await asyncio.sleep(5)
        await self.bot.delete_message(ctx.message)
        await self.bot.delete_message(botmessage1)

#█▀▀▄ █▀▀█ ▀▀█▀▀ ░▀░ █▀▀▄ █▀▀ █▀▀█
#█▀▀▄ █░░█ ░░█░░ ▀█▀ █░░█ █▀▀ █░░█
#▀▀▀░ ▀▀▀▀ ░░▀░░ ▀▀▀ ▀░░▀ ▀░░ ▀▀▀▀
    @commands.command(pass_context=True)
    async def botinfo(self, ctx):
        embed=discord.Embed(title="", color=0xbfea15, timestamp=datetime.utcnow())
        embed.set_author(name="Trivia Nation", icon_url=spin_logo)
        embed.add_field(name="Version", value="3.3.8", inline=True)
        embed.add_field(name="Library", value="discord.py", inline=True)
        embed.add_field(name="Developer", value="dark#9999", inline=True)
        embed.add_field(name="Dev Wesbite", value="http://darktv.xyz/")
        embed.add_field(name="Contributors", value="surister#0570, Ottomated#9999, panda#0003, and RobertoDraws#1234")
        embed.set_thumbnail(url="https://darktv.xyz/wp-content/uploads/2018/05/May.gif")
        embed.set_footer(text="+botinfo", icon_url=spin_logo)
        await self.bot.say(embed=embed)

        print ("| {0} has used the botinfo command in {1}".format(ctx.message.author.name, ctx.message.server.name))
        print('|-----------------------------------------------------------------------------')
        embed=discord.Embed(title="", color=0xbfea15, timestamp=datetime.utcnow())
        embed.set_author(name='Command: +botinfo', icon_url=spin_logo)
        embed.add_field(name="Server", value="{}".format(ctx.message.server.name))
        embed.add_field(name="Channel", value="{}".format(ctx.message.channel.mention))
        embed.add_field(name="User", value="{}".format(ctx.message.author.mention))
        embed.set_thumbnail(url=ctx.message.author.avatar_url)
        embed.set_footer(text="ID: {}".format(ctx.message.id))
        await self.bot.send_message(discord.Object(id='436634502392053761'), embed=embed)

    @commands.command(pass_context=True)
    async def serverinfo(self, ctx):
        embed=discord.Embed(title="", description="Here's what I could find.", color=0xbfea15, timestamp=datetime.utcnow())
        embed.set_author(name="Server Info", icon_url=ctx.message.server.icon_url)
        embed.add_field(name="Name", value=ctx.message.server.name, inline=True)
        embed.add_field(name="ID", value=ctx.message.server.id, inline=True)
        embed.add_field(name="Roles", value=len(ctx.message.server.roles), inline=True)
        embed.add_field(name="Members", value=len(ctx.message.server.members))
        embed.set_thumbnail(url=ctx.message.server.icon_url)
        embed.set_footer(text='+serverinfo', icon_url=spin_logo)
        await self.bot.say(embed=embed)

        print ("| {0} has used the serverinfo command in {1}".format(ctx.message.author.name, ctx.message.server.name))
        print('|-----------------------------------------------------------------------------')
        embed=discord.Embed(title="", color=0xbfea15, timestamp=datetime.utcnow())
        embed.set_author(name='Command: +serverinfo', icon_url=spin_logo)
        embed.add_field(name="Server", value="{}".format(ctx.message.server.name))
        embed.add_field(name="Channel", value="{}".format(ctx.message.channel.mention))
        embed.add_field(name="User", value="{}".format(ctx.message.author.mention))
        embed.set_thumbnail(url=ctx.message.author.avatar_url)
        embed.set_footer(text="ID: {}".format(ctx.message.id))
        await self.bot.send_message(discord.Object(id='436634502392053761'), embed=embed)

#poll

    @commands.command(pass_context=True, aliases=['suggestion'])
    async def suggest(self, ctx, *, mesg):
        embed = discord.Embed(title="", description='{}'.format(mesg), color=0xbfea15, timestamp=datetime.utcnow())
        embed.set_author(name='New suggestion from: {}'.format(ctx.message.author.name))
        embed.set_footer(text='+suggest', icon_url=spin_logo)
        botmessage = await self.bot.send_message(discord.Object(id='436305516633915393'), embed=embed)

        embed=discord.Embed(title="Suggestion Sent! :white_check_mark:", color=0xbfea15, timestamp=datetime.utcnow())
        embed.set_footer(text='+suggest')
        await self.bot.say(embed=embed)

        await self.bot.add_reaction(message=botmessage, emoji='👍')
        await self.bot.add_reaction(message=botmessage, emoji='👎')
        await self.bot.add_reaction(message=botmessage, emoji='🤷')

        print("| {0} has used the suggest command in {1}".format(ctx.message.author.name, ctx.message.server.name))
        print('|-----------------------------------------------------------------------------')
        embed = discord.Embed(title="", color=0xbfea15, timestamp=datetime.utcnow())
        embed.set_author(name='Command: +suggest {}'.format(mesg), icon_url=spin_logo)
        embed.add_field(name="Server", value="{}".format(ctx.message.server.name))
        embed.add_field(name="Channel", value="{}".format(ctx.message.channel.mention))
        embed.add_field(name="User", value="{}".format(ctx.message.author.mention))
        embed.set_thumbnail(url=ctx.message.author.avatar_url)
        embed.set_footer(text="ID: {}".format(ctx.message.id))
        await self.bot.send_message(discord.Object(id='436634502392053761'), embed=embed)

    @suggest.error
    async def suggest_error(self, error, ctx):
        print("| {0} has used the suggest command with an error in {1}".format(ctx.message.author.name, ctx.message.server.name))
        print('|-----------------------------------------------------------------------------')
        embed = discord.Embed(title="", color=0xbfea15, timestamp=datetime.utcnow())
        embed.set_author(name='Invalid syntax: +suggest', icon_url=spin_logo)
        embed.add_field(name="Server", value="{}".format(ctx.message.server.name))
        embed.add_field(name="Channel", value="{}".format(ctx.message.channel.mention))
        embed.add_field(name="User", value="{}".format(ctx.message.author.mention))
        embed.set_thumbnail(url=ctx.message.author.avatar_url)
        embed.set_footer(text="ID: {}".format(ctx.message.id))
        await self.bot.send_message(discord.Object(id='436634502392053761'), embed=embed)

        user = discord.Member
        embed = discord.Embed(title="", description="You must include what you want the suggestion to be about.", color=0xbfea15, timestamp=datetime.utcnow())
        embed.set_author(name="Invalid Syntax".format(user.name))
        embed.add_field(name="Usage", value="+suggest <idea>")
        embed.set_footer(text='+suggest', icon_url=spin_logo)
        botmessage1 = await self.bot.say(embed=embed)
        await asyncio.sleep(5)
        await self.bot.delete_message(ctx.message)
        await self.bot.delete_message(botmessage1)

def setup(bot):
    bot.add_cog(maincogs(bot))
