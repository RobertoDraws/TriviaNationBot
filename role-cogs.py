#Included: role, delrole

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

class irolesthree_int:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, aliases=['roles', 'addrole', 'addroles', 'arole', 'aroles'])
    async def role(self, ctx, user: discord.Member, *msg):
        role_list = [x.name.lower() for x in ctx.message.author.roles]
        if "support team" or "helper" or "staff" or "junior moderator" or "moderator" or "developer" or "head moderator" or "administrator" in role_list:
                hardcode = {"hq":  "winner (hq trivia)",
                            "hqtrivia":  "winner (hq trivia)",
                             "jr": "winner (joyride)",
                             "joyride": "winner (joyride)",
                             "cs": "winner (cash show)",
                             "cashshow": "winner (cash show)",
                             "ht": "winner (hangtime)",
                             "hangtime": "winner (hangtime)",
                             "hyp": "winner (hypsports)",
                             "hypsports": "winner (hypsports)",
                             "qb": "winner (quiz biz)",
                             "quizbiz": "winner (quiz biz)",
                             "siq": "winner (swag iq)",
                             "htl": "winner (halftime live)",
                             "halftimelive": "winner (halftime live)",
                             "rk": "winner (ripkord)",
                             "ripkord": "winner (ripkord)",
                             "mjr": "winner (majority rules)",
                             "majorityrules": "winner (majority rules)",
                             "swagiq": "winner (swag iq)",
                             "btq": "winner (beat the q)",
                             "beattheq": "winner (beat the q)"}

                if user:
                    for i in msg:
                        await asyncio.sleep(1)
                        role = find(lambda r: r.name.lower() == hardcode[i], user.server.roles)
                        if role:
                            mylist =[hardcode[x] for x in msg]
                            await self.bot.add_roles(user, role)
                if user and role:
                    embed = discord.Embed(title="User Given The Role(s)!", description="**{0}** was given the {1} role(s) by **{2}**!".format(user, ", ".join(mylist),ctx.message.author),color=0xbfea15, timestamp=datetime.utcnow())
                    botmessage = await self.bot.say(embed=embed)

                    embed = discord.Embed(title="Given Role(s)!", description="You were given the {0} role(s) by **{1}**!".format(", ".join(mylist), ctx.message.author), color=0xbfea15, timestamp=datetime.utcnow())
                    await self.bot.send_message(user, embed=embed)
                    print ("| {0} has used the role command in {1}".format(ctx.message.author.name, ctx.message.server.name))
                    print('|-----------------------------------------------------------------------------')
                    embed=discord.Embed(title="", color=0xbfea15, timestamp=datetime.utcnow())
                    embed.set_author(name='Command: +role {}'.format(user), icon_url=spin_logo)
                    embed.add_field(name="Server", value="{}".format(ctx.message.server.name))
                    embed.add_field(name="Channel", value="{}".format(ctx.message.channel.mention))
                    embed.add_field(name="Staff", value="{}".format(ctx.message.author.mention))

                    embed.set_thumbnail(url=ctx.message.author.avatar_url)
                    embed.set_footer(text="ID: {}".format(ctx.message.id))
                    await self.bot.send_message(discord.Object(id='436634502392053761'), embed=embed)
                    await asyncio.sleep(5)
                    await self.bot.delete_message(ctx.message)

        else:
            print ("| {0} has tried to use the role command in {1}".format(ctx.message.author.name, ctx.message.server.name))
            print('|-----------------------------------------------------------------------------')
            embed=discord.Embed(title="Permission Denied.", description="You don't have permission to use this command.", color=0xff2f2f, timestamp=datetime.utcnow())
            botmessage1 = await self.bot.say(embed=embed)
            embed.set_author(name='Command: +role {}'.format(user.mention), icon_url=spin_logo)
            embed.add_field(name="Server", value="{}".format(ctx.message.server.name))
            embed.add_field(name="Channel", value="{}".format(ctx.message.channel.mention))
            embed.add_field(name="Attempted By:", value="{}".format(ctx.message.author.mention))

            embed.set_thumbnail(url=ctx.message.author.avatar_url)
            embed.set_footer(text="ID: {}".format(ctx.message.id))
            await asyncio.sleep(5)
            await self.bot.delete_message(ctx.message)
            await self.bot.delete_message(botmessage1)

    @role.error
    async def role_error(self, error, ctx):
        print ("| {0} has used the role command with an error in {1}".format(ctx.message.author.name, ctx.message.server.name))
        print('|-----------------------------------------------------------------------------')
        user = discord.Member
        embed=discord.Embed(title="", color=0xbfea15, timestamp=datetime.utcnow())
        embed.set_author(name='Invalid syntax: +role', icon_url=spin_logo)
        embed.add_field(name="Server", value="{}".format(ctx.message.server.name))
        embed.add_field(name="Channel", value="{}".format(ctx.message.channel.mention))
        embed.add_field(name="User", value="{}".format(ctx.message.author.mention))
        embed.set_thumbnail(url=ctx.message.author.avatar_url)
        embed.set_footer(text="ID: {}".format(ctx.message.id))
        await self.bot.send_message(discord.Object(id='436634502392053761'), embed=embed)

        embed=discord.Embed(title="", description="Arguments not correct/incomplete!", color=0xbfea15, timestamp=datetime.utcnow())
        embed.set_author(name="Invalid Syntax".format(user.name))
        embed.add_field(name="Usage", value="+role <member> <role(s)>")
        embed.set_footer(text='+role', icon_url=spin_logo)
        botmessage1 = await self.bot.say(embed=embed)
        await asyncio.sleep(5)
        await self.bot.delete_message(ctx.message)
        await self.bot.delete_message(botmessage1)

#█▀▀▄ █▀▀ █░░ █▀▀█ █▀▀█ █░░ █▀▀
#█░░█ █▀▀ █░░ █▄▄▀ █░░█ █░░ █▀▀
#▀▀▀░ ▀▀▀ ▀▀▀ ▀░▀▀ ▀▀▀▀ ▀▀▀ ▀▀▀
    @commands.command(pass_context=True, aliases=['delroles', 'drole', 'droles'])
    async def delrole(self, ctx, user: discord.Member, *msg):
        role_list = [x.name.lower() for x in ctx.message.author.roles]
        if "support team" in role_list:
                hardcode1 = {"hq":  "winner (hq trivia)",
                             "hqtrivia":  "winner (hq trivia)",
                              "jr": "winner (joyride)",
                              "joyride": "winner (joyride)",
                              "cs": "winner (cash show)",
                              "cashshow": "winner (cash show)",
                              "ht": "winner (hangtime)",
                              "hangtime": "winner (hangtime)",
                              "hyp": "winner (hypsports)",
                              "hypsports": "winner (hypsports)",
                              "qb": "winner (quiz biz)",
                              "quizbiz": "winner (quiz biz)",
                              "siq": "winner (swag iq)",
                              "htl": "winner (halftime live)",
                              "halftimelive": "winner (halftime live)",
                              "rk": "winner (ripkord)",
                              "ripkord": "winner (ripkord)",
                              "mjr": "winner (majority rules)",
                              "majorityrules": "winner (majority rules)",
                              "swagiq": "winner (swag iq)",
                              "btq": "winner (beat the q)",
                              "beattheq": "winner (beat the q)"}

                if user:
                    for i in msg:
                        await asyncio.sleep(1)
                        role = find(lambda r: r.name.lower() == hardcode1[i], user.server.roles)
                        if role:
                            mylist =[hardcode1[x] for x in msg]
                            await self.bot.remove_roles(user, role)
                if user and role:
                    embed = discord.Embed(title="User Removed From Role(s)!", description="**{0}** was removed from the {1} role(s) by **{2}**!".format(user, ", ".join(mylist),ctx.message.author),color=0xbfea15, timestamp=datetime.utcnow())
                    botmessage = await self.bot.say(embed=embed)

                    embed = discord.Embed(title="Removed From Role(s)!", description="You were removed from the {0} role(s) by **{1}**!".format(", ".join(mylist), ctx.message.author), color=0xbfea15, timestamp=datetime.utcnow())
                    await self.bot.send_message(user, embed=embed)
                    print ("| {0} has used the delrole command in {1}".format(ctx.message.author.name, ctx.message.server.name))
                    print('|-----------------------------------------------------------------------------')
                    embed=discord.Embed(title="", color=0xbfea15, timestamp=datetime.utcnow())
                    embed.set_author(name='Command: +delrole {}'.format(user), icon_url=spin_logo)
                    embed.add_field(name="Server", value="{}".format(ctx.message.server.name))
                    embed.add_field(name="Channel", value="{}".format(ctx.message.channel.mention))
                    embed.add_field(name="Staff", value="{}".format(ctx.message.author.mention))
                    embed.set_thumbnail(url=ctx.message.author.avatar_url)
                    embed.set_footer(text="ID: {}".format(ctx.message.id))
                    await self.bot.send_message(discord.Object(id='436634502392053761'), embed=embed)
                    await asyncio.sleep(5)
                    await self.bot.delete_message(ctx.message)

        else:
            print ("| {0} has tried to use the delrole command in {1}".format(ctx.message.author.name, ctx.message.server.name))
            print('|-----------------------------------------------------------------------------')
            embed=discord.Embed(title="Permission Denied.", description="You don't have permission to use this command.", color=0xff2f2f, timestamp=datetime.utcnow())
            botmessage1 = await self.bot.say(embed=embed)
            embed.set_author(name='Command: +delrole {}'.format(user.mention), icon_url=spin_logo)
            embed.add_field(name="Server", value="{}".format(ctx.message.server.name))
            embed.add_field(name="Channel", value="{}".format(ctx.message.channel.mention))
            embed.add_field(name="Attempted By:", value="{}".format(ctx.message.author.mention))
            embed.set_thumbnail(url=ctx.message.author.avatar_url)
            embed.set_footer(text="ID: {}".format(ctx.message.id))
            await asyncio.sleep(5)
            await self.bot.delete_message(ctx.message)
            await self.bot.delete_message(botmessage1)

    @delrole.error
    async def delrole_error(self, error, ctx):
        print ("| {0} has used the delrole command with an error in {1}".format(ctx.message.author.name, ctx.message.server.name))
        print('|-----------------------------------------------------------------------------')
        user = discord.Member
        embed=discord.Embed(title="", color=0xbfea15, timestamp=datetime.utcnow())
        embed.set_author(name='Invalid syntax: +delrole', icon_url=spin_logo)
        embed.add_field(name="Server", value="{}".format(ctx.message.server.name))
        embed.add_field(name="Channel", value="{}".format(ctx.message.channel.mention))
        embed.add_field(name="User", value="{}".format(ctx.message.author.mention))
        embed.set_thumbnail(url=ctx.message.author.avatar_url)
        embed.set_footer(text="ID: {}".format(ctx.message.id))
        await self.bot.send_message(discord.Object(id='436634502392053761'), embed=embed)

        embed=discord.Embed(title="", description="Arguments not correct/incomplete!", color=0xbfea15, timestamp=datetime.utcnow())
        embed.set_author(name="Invalid Syntax".format(user.name))
        embed.add_field(name="Usage", value="+delrole <member> <role(s)>")
        embed.set_footer(text='+delrole', icon_url=spin_logo)
        botmessage1 = await self.bot.say(embed=embed)
        await asyncio.sleep(5)
        await self.bot.delete_message(ctx.message)
        await self.bot.delete_message(botmessage1)


def setup(bot):
    bot.add_cog(irolesthree_int(bot))
