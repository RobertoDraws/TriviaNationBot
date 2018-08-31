#Included: doge, warm, cookie, eightball, coinflip, farm, sport/play

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
from urllib.parse import quote
from itertools import cycle
from discord.utils import find

spin_logo = "https://cdn.discordapp.com/attachments/411306798042054657/471067301408538635/Trivia_Nation_Logo_HQ.jpg"
red = "0xff2f2f"
green = "0xbfea15"

class misccogs:
    def __init__(self, bot):
        self.bot = bot

#█▀▀▄ █▀▀█ █▀▀▀ █▀▀
#█░░█ █░░█ █░▀█ █▀▀
#▀▀▀░ ▀▀▀▀ ▀▀▀▀ ▀▀▀
    @commands.command(pass_context = True)
    async def doge(self, ctx):

        url = 'https://dog.ceo/api/breeds/image/random'
        r = requests.get(url)
        data = r.json()
        embed = discord.Embed(title=":dog: Woof!", color=0xbfea15, timestamp=datetime.utcnow())
        embed.set_image(url=data["message"])
        embed.set_footer(text='+doge', icon_url=spin_logo)
        await self.bot.say(embed=embed)

        print ("| {0} has used the doge command in {1}".format(ctx.message.author.name, ctx.message.server.name))
        print('|-----------------------------------------------------------------------------')
        embed=discord.Embed(title="", color=0xbfea15, timestamp=datetime.utcnow())
        embed.set_author(name='Command: +doge', icon_url=spin_logo)
        embed.add_field(name="Server", value="{}".format(ctx.message.server.name))
        embed.add_field(name="Channel", value="{}".format(ctx.message.channel.mention))
        embed.add_field(name="User", value="{}".format(ctx.message.author.mention))
        embed.set_thumbnail(url=data["message"])
        embed.set_footer(text="ID: {}".format(ctx.message.id))
        await self.bot.send_message(discord.Object(id='436634502392053761'), embed=embed)

#█░░░█ █▀▀█ █▀▀█ █▀▄▀█
#█▄█▄█ █▄▄█ █▄▄▀ █░▀░█
#░▀░▀░ ▀░░▀ ▀░▀▀ ▀░░░▀
    @commands.command(pass_context=True)
    async def warm(self, ctx, user: discord.Member):

        embed=discord.Embed(title=":sun_with_face: **{0}** has been warmed by **{1}** :heart:.".format(user.name, ctx.message.author.name), color=0xeca762, timestamp=datetime.utcnow())
        embed.set_footer(text='+warm', icon_url=spin_logo)
        await self.bot.say(embed=embed)

        print ("| {0} has used the warm command in {1}".format(ctx.message.author.name, ctx.message.server.name))
        print('|-----------------------------------------------------------------------------')

        embed=discord.Embed(title="", color=0xbfea15, timestamp=datetime.utcnow())
        embed.set_author(name='Command: +warm {}'.format(user.name), icon_url=spin_logo)
        embed.add_field(name="Server", value="{}".format(ctx.message.server.name))
        embed.add_field(name="Channel", value="{}".format(ctx.message.channel.mention))
        embed.add_field(name="User", value="{}".format(ctx.message.author.mention))
        embed.set_thumbnail(url=ctx.message.author.avatar_url)
        embed.set_footer(text="ID: {}".format(ctx.message.id))
        await self.bot.send_message(discord.Object(id='436634502392053761'), embed=embed)

    @warm.error
    async def warm_error(self, error, ctx):
        print ("| {0} has used the warn command with an error in {1}".format(ctx.message.author.name, ctx.message.server.name))
        print('|-----------------------------------------------------------------------------')

        user = discord.Member
        embed=discord.Embed(title="", color=0xbfea15, timestamp=datetime.utcnow())
        embed.set_author(name='Invalid syntax: +warm', icon_url=spin_logo)
        embed.add_field(name="Server", value="{}".format(ctx.message.server.name))
        embed.add_field(name="Channel", value="{}".format(ctx.message.channel.mention))
        embed.add_field(name="User", value="{}".format(ctx.message.author.mention))
        embed.set_thumbnail(url=ctx.message.author.avatar_url)
        embed.set_footer(text="ID: {}".format(ctx.message.id))
        await self.bot.send_message(discord.Object(id='436634502392053761'), embed=embed)

        embed=discord.Embed(title="", description="This command makes a member warm :wink:", color=0xbfea15, timestamp=datetime.utcnow())
        embed.set_author(name="Invalid Syntax".format(user.name))
        embed.add_field(name="Usage", value="+warm <member>")
        embed.set_footer(text='+warm', icon_url=spin_logo)
        botmessage1 = await self.bot.say(embed=embed)
        await asyncio.sleep(5)
        await self.bot.delete_message(ctx.message)
        await self.bot.delete_message(botmessage1)

#█▀▀ █▀▀█ █▀▀█ █░█ ░▀░ █▀▀
#█░░ █░░█ █░░█ █▀▄ ▀█▀ █▀▀
#▀▀▀ ▀▀▀▀ ▀▀▀▀ ▀░▀ ▀▀▀ ▀▀▀
    @commands.command(pass_context=True)
    async def cookie(self, ctx, user: discord.Member):

        embed=discord.Embed(title="**{0}** has given a :cookie: with :heart: to **{1}**.".format(ctx.message.author.name, user.name), color=0xeca762, timestamp=datetime.utcnow())
        embed.set_footer(text='+cookie', icon_url=spin_logo)
        await self.bot.say(embed=embed)

        print ("| {0} has used the cookie command in {1}".format(ctx.message.author.name, ctx.message.server.name))
        print('|-----------------------------------------------------------------------------')

        embed=discord.Embed(title="", color=0xbfea15, timestamp=datetime.utcnow())
        embed.set_author(name='Command: +cookie {}'.format(user.name), icon_url=spin_logo)
        embed.add_field(name="Server", value="{}".format(ctx.message.server.name))
        embed.add_field(name="Channel", value="{}".format(ctx.message.channel.mention))
        embed.add_field(name="User", value="{}".format(ctx.message.author.mention))
        embed.set_thumbnail(url=ctx.message.author.avatar_url)
        embed.set_footer(text="ID: {}".format(ctx.message.id))
        await self.bot.send_message(discord.Object(id='436634502392053761'), embed=embed)

    @cookie.error
    async def cookie_error(self, error, ctIx):
        print ("| {0} has used the cookie command with an error in {1}".format(ctx.message.author.name, ctx.message.server.name))
        print('|-----------------------------------------------------------------------------')

        user = discord.Member
        embed=discord.Embed(title="", color=0xbfea15, timestamp=datetime.utcnow())
        embed.set_author(name='Invalid syntax: +cookie', icon_url=spin_logo)
        embed.add_field(name="Server", value="{}".format(ctx.message.server.name))
        embed.add_field(name="Channel", value="{}".format(ctx.message.channel.mention))
        embed.add_field(name="User", value="{}".format(ctx.message.author.mention))
        embed.set_thumbnail(url=ctx.message.author.avatar_url)
        embed.set_footer(text="ID: {}".format(ctx.message.id))
        await self.bot.send_message(discord.Object(id='436634502392053761'), embed=embed)

        embed=discord.Embed(title="", description="This command gives a member a :cookie:.", color=0xbfea15, timestamp=datetime.utcnow())
        embed.set_author(name="Invalid Syntax".format(user.name))
        embed.add_field(name="Usage", value="+cookie <member>")
        embed.set_footer(text='+cookie', icon_url=spin_logo)
        botmessage1 = await self.bot.say(embed=embed)
        await asyncio.sleep(5)
        await self.bot.delete_message(ctx.message)
        await self.bot.delete_message(botmessage1)


#█▀▀ ░▀░ █▀▀▀ █░░█ ▀▀█▀▀ █▀▀▄ █▀▀█ █░░ █░░
#█▀▀ ▀█▀ █░▀█ █▀▀█ ░░█░░ █▀▀▄ █▄▄█ █░░ █░░
#▀▀▀ ▀▀▀ ▀▀▀▀ ▀░░▀ ░░▀░░ ▀▀▀░ ▀░░▀ ▀▀▀ ▀▀▀
    @commands.command(pass_context=True, aliases=['8ball'])
    @commands.cooldown(1, 20, commands.BucketType.user)
    async def eightball(self, ctx, *, mesg):
        print ("| {0} has used the eightball command in {1}".format(ctx.message.author.name, ctx.message.server.name))
        print('|-----------------------------------------------------------------------------')

        user = discord.Member
        embed=discord.Embed(title="", color=0xbfea15, timestamp=datetime.utcnow())
        embed.set_author(name='Command: +eightball', icon_url=spin_logo)
        embed.add_field(name="Server", value="{}".format(ctx.message.server.name))
        embed.add_field(name="Channel", value="{}".format(ctx.message.channel.mention))
        embed.add_field(name="User", value="{}".format(ctx.message.author.mention))
        embed.set_thumbnail(url='https://thumbs.gfycat.com/KeenVerifiableCavy-max-1mb.gif')
        embed.set_footer(text="ID: {}".format(ctx.message.id))
        await self.bot.send_message(discord.Object(id='436634502392053761'), embed=embed)

        embed=discord.Embed(title="Randomly selecting answer, give me a few seconds...", color=0xffffff)
        embed.set_author(name="Magic 8 Ball", icon_url="https://thumbs.gfycat.com/KeenVerifiableCavy-max-1mb.gif")
        botmessage = await self.bot.say(embed=embed)
        await asyncio.sleep(5)
        await self.bot.delete_message(botmessage)

        possible_responses = [
            ':white_check_mark: It is certain.',
            ':white_check_mark: It is decidedly so.',
            ':white_check_mark: Without a doubt.',
            ':white_check_mark: Yes - definitely.',
            ':white_check_mark: You may rely on it.',
            ':white_check_mark: As I see it, yes.',
            ':white_check_mark: Most likely.',
            ':white_check_mark: Outlook good.',
            ':white_check_mark: Yes.',
            ':white_check_mark: Signs point to yes.',
            ':warning: Reply hazy, try again',
            ':warning: Ask again later.',
            ':warning: Better not tell you now.',
            ':warning: Cannot predict now.',
            ':warning: Concentrate and ask again.',
            ":x: Don't count on it.",
            ':x: My reply is no.',
            ':x: My sources say no.',
            ':x: Outlook not so good.',
            ':x: Very doubtful.',
        ]
        answer = (random.choice(possible_responses))
        embed=discord.Embed(title="And the answer is...", color=0xffffff, timestamp=datetime.utcnow())
        embed.set_author(name="Magic 8 Ball", icon_url="https://thumbs.gfycat.com/KeenVerifiableCavy-max-1mb.gif")
        embed.add_field(name="Question", value='{}'.format(mesg), inline=False)
        embed.add_field(name="Answer", value='{}'.format(answer), inline=False)
        embed.set_footer(text='+eightball', icon_url=spin_logo)
        await self.bot.say(embed=embed)

    @eightball.error
    async def eightball_error(self, error, ctx):
        print ("| {0} has used the eightball command on cooldown in {1}".format(ctx.message.author.name, ctx.message.server.name))
        print('|-----------------------------------------------------------------------------')

        user = discord.Member
        embed=discord.Embed(title="", color=0xbfea15, timestamp=datetime.utcnow())
        embed.set_author(name='Cooldown: +eightball', icon_url=spin_logo)
        embed.add_field(name="Server", value="{}".format(ctx.message.server.name))
        embed.add_field(name="Channel", value="{}".format(ctx.message.channel.mention))
        embed.add_field(name="User", value="{}".format(ctx.message.author.mention))
        embed.set_thumbnail(url='https://thumbs.gfycat.com/KeenVerifiableCavy-max-1mb.gif')
        embed.set_footer(text="ID: {}".format(ctx.message.id))
        await self.bot.send_message(discord.Object(id='436634502392053761'), embed=embed)

        embed=discord.Embed(title="", description=f'**You are on cooldown or you have not asked a question :alarm_clock:.** Try again in {str(round(error.retry_after, 2))} seconds!\n*This message will be deleted once you can use the* `+eightball` *command again.*', color=0xbfea15, timestamp=datetime.utcnow())
        embed.set_author(name="8Ball Cooldown".format(user.name))
        embed.set_thumbnail(url="https://i.imgur.com/zEbHiZs.gif")
        embed.set_footer(text='+eightball', icon_url=spin_logo)
        botmessage1 = await self.bot.say(embed=embed)
        await asyncio.sleep(error.retry_after)
        await self.bot.delete_message(botmessage1)

#█▀▀ █▀▀█ ░▀░ █▀▀▄ █▀▀ █░░ ░▀░ █▀▀█
#█░░ █░░█ ▀█▀ █░░█ █▀▀ █░░ ▀█▀ █░░█
#▀▀▀ ▀▀▀▀ ▀▀▀ ▀░░▀ ▀░░ ▀▀▀ ▀▀▀ █▀▀▀
    @commands.command(pass_context=True, aliases=['coin', 'flip'])
    @commands.cooldown(1, 20, commands.BucketType.user)
    async def coinflip(self, ctx, *, choices):
        print ("| {0} has used the coinflip command in {1}".format(ctx.message.author.name, ctx.message.server.name))
        print('|-----------------------------------------------------------------------------')

        user = discord.Member
        embed=discord.Embed(title="", color=0xbfea15, timestamp=datetime.utcnow())
        embed.set_author(name='Command: +coinflip', icon_url=spin_logo)
        embed.add_field(name="Server", value="{}".format(ctx.message.server.name))
        embed.add_field(name="Channel", value="{}".format(ctx.message.channel.mention))
        embed.add_field(name="User", value="{}".format(ctx.message.author.mention))
        embed.set_thumbnail(url='https://i.imgur.com/GsrBafV.gif')
        embed.set_footer(text="ID: {}".format(ctx.message.id))
        await self.bot.send_message(discord.Object(id='436634502392053761'), embed=embed)

        embed=discord.Embed(title="Flipping, give me a few seconds...", color=0xffffff)
        embed.set_author(name="Coin Flip", icon_url="https://i.imgur.com/GsrBafV.gif")
        botmessage = await self.bot.say(embed=embed)
        await asyncio.sleep(5)
        await self.bot.delete_message(botmessage)

        answer = random.choice(list(map(str.strip, choices.split('|'))))
        embed=discord.Embed(title="And the answer is...", color=0xffffff, timestamp=datetime.utcnow())
        embed.set_author(name="Coin Flip", icon_url="https://i.imgur.com/GsrBafV.gif")
        embed.add_field(name="Options", value='{}'.format(choices), inline=False)
        embed.add_field(name="Answer", value='{}'.format(answer), inline=False)
        embed.set_footer(text='+coinflip', icon_url=spin_logo)
        await self.bot.say(embed=embed)

    @coinflip.error
    async def coinflip_error(self, error, ctx):
        print ("| {0} has used the coinflip command on cooldown in {1}".format(ctx.message.author.name, ctx.message.server.name))
        print('|-----------------------------------------------------------------------------')

        user = discord.Member
        embed=discord.Embed(title="", color=0xbfea15, timestamp=datetime.utcnow())
        embed.set_author(name='Cooldown: +coinflip', icon_url=spin_logo)
        embed.add_field(name="Server", value="{}".format(ctx.message.server.name))
        embed.add_field(name="Channel", value="{}".format(ctx.message.channel.mention))
        embed.add_field(name="User", value="{}".format(ctx.message.author.mention))
        embed.set_thumbnail(url='https://i.imgur.com/GsrBafV.gif')
        embed.set_footer(text="ID: {}".format(ctx.message.id))
        await self.bot.send_message(discord.Object(id='436634502392053761'), embed=embed)

        embed=discord.Embed(title="", description=f'**You are on cooldown or you have not put in two arguments :alarm_clock:.**Try again in {str(round(error.retry_after, 2))} seconds!\n*This message will be deleted once you can use the* `+coinflip` *command again.*', color=0xbfea15, timestamp=datetime.utcnow())
        embed.set_author(name="Coin Flip Cooldown".format(user.name))
        embed.set_thumbnail(url="https://i.imgur.com/zEbHiZs.gif")
        embed.set_footer(text='+coinflip', icon_url=spin_logo)
        botmessage1 = await self.bot.say(embed=embed)
        await asyncio.sleep(error.retry_after)
        await self.bot.delete_message(botmessage1)

#█▀▀ █▀▀█ █▀▀█ █▀▄▀█
#█▀▀ █▄▄█ █▄▄▀ █░▀░█
#▀░░ ▀░░▀ ▀░▀▀ ▀░░░▀
    @commands.command(pass_context=True, aliases=['farmy'])
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def farm(self, ctx):
        print ("| {0} has used the farm command in {1}".format(ctx.message.author.name, ctx.message.server.name))
        print('|-----------------------------------------------------------------------------')

        user = discord.Member
        embed=discord.Embed(title="", color=0xbfea15, timestamp=datetime.utcnow())
        embed.set_author(name='Command: +farm', icon_url=spin_logo)
        embed.add_field(name="Server", value="{}".format(ctx.message.server.name))
        embed.add_field(name="Channel", value="{}".format(ctx.message.channel.mention))
        embed.add_field(name="User", value="{}".format(ctx.message.author.mention))
        embed.set_thumbnail(url='https://i.imgur.com/g12DuwU.png')
        embed.set_footer(text="ID: {}".format(ctx.message.id))
        await self.bot.send_message(discord.Object(id='436634502392053761'), embed=embed)

        embed=discord.Embed(title="Farming, give me a few seconds...", color=0xffffff)
        embed.set_author(name="Farmy", icon_url="https://media0.giphy.com/media/l378lr9mW23l1Tw4g/giphy.gif")
        botmessage = await self.bot.say(embed=embed)
        await asyncio.sleep(3)
        await self.bot.delete_message(botmessage)

        possible_responses = [
        ':green_apple:',
        ':apple:',
        ':pear:',
        ':tangerine:',
        ':lemon:',
        ':banana:',
        ':watermelon:',
        ':grapes:',
        ':strawberry:',
        ':melon:',
        ':cherries:',
        ':peach:',
        ':pineapple:',
        ':tomato:',
        ':eggplant:',
        ':hot_pepper:',
        ':corn:',
        ':sweet_potato:',
        ':honey_pot:',
        ':bread:',
        ':cheese:',
        ':bacon:',
        ':potato:',
        ':carrot:',
        ':french_bread:',
        ':kiwi:',
        ':peanuts:',
        ':milk:',
        ':chocolate_bar:',
        ':burrito:',
        ':chicken:',
        ':poultry_leg:',
        ':meat_on_bone:',
        ':fried_shrimp:',
        ':cooking:',
        ':hamburger:',
        ':fries:',
        ':hotdog:',
        ':pizza:',
        ':spaghetti:',
        ':taco:',
        ':ramen:',
        ':stew:',
        ':fish_cake:',
        ':sushi:',
        ':bento:',
        ':curry:',
        ':rice_ball:',
        ':rice:',
        ':rice_cracker:',
        ':oden:',
        ':dango:',
        ':shaved_ice:',
        ':ice_cream:',
        ':icecream:',
        ':cake:',
        ':birthday:',
        ':custard:',
        ':candy:',
        ':lollipop:',
        ':popcorn:',
        ':doughnut:',
        ':cookie:',
        ':beer:',
        ':beers:',
        ':wine_glass:',
        ':cocktail:',
        ':tropical_drink:',
        ':salad:',
        ':shallow_pan_of_food:',
        ':stuffed_flatbread:',
        ':champagne_glass:',
        ':tumbler_glass:',
        ':spoon:',
        ':egg:',
        ':pancakes:',
        ':poop:',
        ]
        item = (random.choice(possible_responses))
        embed=discord.Embed(title=":tractor: | {0}, you farmed: {1}!".format(ctx.message.author.name, item), color=0xffffff, timestamp=datetime.utcnow())
        embed.set_author(name="Farmy", icon_url="https://media0.giphy.com/media/l378lr9mW23l1Tw4g/giphy.gif")
        embed.set_thumbnail(url='https://i.imgur.com/g12DuwU.png')
        embed.set_footer(text='+farm (Idea by DevelUpGames#1185)', icon_url=spin_logo)
        await self.bot.say(embed=embed)

    @farm.error
    async def farm_error(self, error, ctx):
        print ("| {0} has used the farm command on cooldown in {1}".format(ctx.message.author.name, ctx.message.server.name))
        print('|-----------------------------------------------------------------------------')

        user = discord.Member
        embed=discord.Embed(title="", color=0xbfea15, timestamp=datetime.utcnow())
        embed.set_author(name='Cooldown: +farm', icon_url=spin_logo)
        embed.add_field(name="Server", value="{}".format(ctx.message.server.name))
        embed.add_field(name="Channel", value="{}".format(ctx.message.channel.mention))
        embed.add_field(name="User", value="{}".format(ctx.message.author.mention))
        embed.set_thumbnail(url='https://i.imgur.com/GsrBafV.gif')
        embed.set_footer(text="ID: {}".format(ctx.message.id))
        await self.bot.send_message(discord.Object(id='436634502392053761'), embed=embed)

        embed=discord.Embed(title="", description=f'**You are on cooldown! :alarm_clock:.**Try again in {str(round(error.retry_after, 2))} seconds!\n*This message will be deleted once you can use the* `+farm` *command again.*', color=0xbfea15, timestamp=datetime.utcnow())
        embed.set_author(name="Farmy Cooldown".format(user.name))
        embed.set_thumbnail(url="https://i.imgur.com/zEbHiZs.gif")
        embed.set_footer(text='+farm', icon_url=spin_logo)
        botmessage1 = await self.bot.say(embed=embed)
        await asyncio.sleep(error.retry_after)
        await self.bot.delete_message(botmessage1)

#█▀▀ █▀▀█ █▀▀█ █▀▀█ ▀▀█▀▀
#▀▀█ █░░█ █░░█ █▄▄▀ ░░█░░
#▀▀▀ █▀▀▀ ▀▀▀▀ ▀░▀▀ ░░▀░░
    @commands.command(pass_context=True, aliases=['play'])
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def sport(self, ctx):
        print ("| {0} has used the sport command in {1}".format(ctx.message.author.name, ctx.message.server.name))
        print('|-----------------------------------------------------------------------------')

        user = discord.Member
        embed=discord.Embed(title="", color=0xbfea15, timestamp=datetime.utcnow())
        embed.set_author(name='Command: +sport', icon_url=spin_logo)
        embed.add_field(name="Server", value="{}".format(ctx.message.server.name))
        embed.add_field(name="Channel", value="{}".format(ctx.message.channel.mention))
        embed.add_field(name="User", value="{}".format(ctx.message.author.mention))
        embed.set_thumbnail(url='https://cdn.dribbble.com/users/68398/screenshots/3333492/cyclist.gif')
        embed.set_footer(text="ID: {}".format(ctx.message.id))
        await self.bot.send_message(discord.Object(id='436634502392053761'), embed=embed)

        embed=discord.Embed(title="Thinking, give me a few seconds...", color=0xffffff)
        embed.set_author(name="Sport", icon_url="https://i.imgur.com/Yb9gtzH.jpg")
        botmessage = await self.bot.say(embed=embed)
        await asyncio.sleep(3)
        await self.bot.delete_message(botmessage)

        possible_responses = [
        ':soccer:',
        ':basketball:',
        ':football:',
        ':baseball:',
        ':tennis:',
        ':volleyball:',
        ':rugby_football:',
        ':8ball:',
        ':ping_pong:',
        ':badminton:',
        ':goal:',
        ':hockey:',
        ':field_hockey:',
        ':cricket:',
        ':golf:',
        ':bow_and_arrow:',
        ':fishing_pole_and_fish:',
        ':boxing_glove:',
        ':martial_arts_uniform:',
        ':running_shirt_with_sash:',
        ':ice_skate:',
        ':ski:',
        ':skier:',
        ':snowboarder:',
        ':lifter:',
        ':wrestlers:',
        ':cartwheel:',
        ':person_doing_cartwheel:',
        ':basketball_player:',
        ':person_with_ball:',
        ':basketball_player::',
        ':person_with_ball:',
        ':fencer:',
        ':handball:',
        ':golfer:',
        ':horse_racing:',
        ':surfer:',
        ':swimmer:',
        ':water_polo:',
        ':rowboat:',
        ':mountain_bicyclist:',
        ':bicyclist:',
        ':circus_tent:',
        ':juggling:',
        ':juggler:‍',
        ':performing_arts:',
        ':art:',
        ':clapper:',
        ':microphone:',
        ':headphones:',
        ':musical_score:',
        ':musical_keyboard:',
        ':drum:',
        ':saxophone:',
        ':trumpet:',
        ':guitar:',
        ':violin:',
        ':game_die:',
        ':dart:',
        ':bowling:',
        ':video_game:',
        ':slot_machine:',
        ]
        sport = (random.choice(possible_responses))
        embed=discord.Embed(title=":trophy: | {0}, you will play/do: {1}!".format(ctx.message.author.name, sport), color=0xffffff, timestamp=datetime.utcnow())
        embed.set_author(name="Sports", icon_url="https://i.imgur.com/Yb9gtzH.jpg")
        embed.set_thumbnail(url='https://cdn.dribbble.com/users/68398/screenshots/3333492/cyclist.gif')
        embed.set_footer(text='+sport', icon_url=spin_logo)
        await self.bot.say(embed=embed)

    @sport.error
    async def sport_error(self, error, ctx):
        print ("| {0} has used the sport command on cooldown in {1}".format(ctx.message.author.name, ctx.message.server.name))
        print('|-----------------------------------------------------------------------------')

        user = discord.Member
        embed=discord.Embed(title="", color=0xbfea15, timestamp=datetime.utcnow())
        embed.set_author(name='Cooldown: +sport', icon_url=spin_logo)
        embed.add_field(name="Server", value="{}".format(ctx.message.server.name))
        embed.add_field(name="Channel", value="{}".format(ctx.message.channel.mention))
        embed.add_field(name="User", value="{}".format(ctx.message.author.mention))
        embed.set_thumbnail(url='https://i.imgur.com/GsrBafV.gif')
        embed.set_footer(text="ID: {}".format(ctx.message.id))
        await self.bot.send_message(discord.Object(id='436634502392053761'), embed=embed)

        embed=discord.Embed(title="", description=f'**You are on cooldown! :alarm_clock:.**Try again in {str(round(error.retry_after, 2))} seconds!\n*This message will be deleted once you can use the* `+sport` *command again.*', color=0xbfea15, timestamp=datetime.utcnow())
        embed.set_author(name="Sport Cooldown".format(user.name))
        embed.set_thumbnail(url="https://i.imgur.com/zEbHiZs.gif")
        embed.set_footer(text='+sport', icon_url=spin_logo)
        botmessage1 = await self.bot.say(embed=embed)
        await asyncio.sleep(error.retry_after)
        await self.bot.delete_message(botmessage1)

    @commands.command(pass_context=True)
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def fish(self, ctx):
        print ("| {0} has used the fish command in {1}".format(ctx.message.author.name, ctx.message.server.name))
        print('|-----------------------------------------------------------------------------')

        user = discord.Member
        embed=discord.Embed(title="", color=0xbfea15, timestamp=datetime.utcnow())
        embed.set_author(name='Command: +fish', icon_url=spin_logo)
        embed.add_field(name="Server", value="{}".format(ctx.message.server.name))
        embed.add_field(name="Channel", value="{}".format(ctx.message.channel.mention))
        embed.add_field(name="User", value="{}".format(ctx.message.author.mention))
        embed.set_thumbnail(url='https://media.giphy.com/media/Y4sT5ESJWdPGtTKqNd/giphy.gif')
        embed.set_footer(text="ID: {}".format(ctx.message.id))
        await self.bot.send_message(discord.Object(id='436634502392053761'), embed=embed)

        embed=discord.Embed(title="Fishing, give me a few seconds...", color=0xffffff)
        embed.set_author(name="Fishy", icon_url="https://media.giphy.com/media/Y4sT5ESJWdPGtTKqNd/giphy.gif")
        botmessage = await self.bot.say(embed=embed)
        await asyncio.sleep(3)
        await self.bot.delete_message(botmessage)

        possible_responses = [
            ':fishing_pole_and_fish:  |  **{}, you caught: :shopping_cart:!**'.format(ctx.message.author.name), #Shopping Cart
            ':fishing_pole_and_fish:  |  **{}, you caught: :shopping_cart:!**'.format(ctx.message.author.name), #Shopping Cart
            ':fishing_pole_and_fish:  |  **{}, you caught: :shopping_cart:!**'.format(ctx.message.author.name), #Shopping Cart
            ':fishing_pole_and_fish:  |  **{}, you caught: :shopping_cart:!**'.format(ctx.message.author.name), #Shopping Cart
            ':fishing_pole_and_fish:  |  **{}, you caught: :shopping_cart:!**'.format(ctx.message.author.name), #Shopping Cart
            ':fishing_pole_and_fish:  |  **{}, you caught: :shopping_cart:!**'.format(ctx.message.author.name), #Shopping Cart
            ':fishing_pole_and_fish:  |  **{}, you caught: :shopping_cart:!**'.format(ctx.message.author.name), #Shopping Cart
            ':fishing_pole_and_fish:  |  **{}, you caught: :shopping_cart:!**'.format(ctx.message.author.name), #Shopping Cart
            ':fishing_pole_and_fish:  |  **{}, you caught: :shopping_cart:!**'.format(ctx.message.author.name), #Shopping Cart
            ':fishing_pole_and_fish:  |  **{}, you caught: :shopping_cart:!**'.format(ctx.message.author.name), #Shopping Cart
            ':fishing_pole_and_fish:  |  **{}, you caught: :shopping_cart:!**'.format(ctx.message.author.name), #Shopping Cart
            ':fishing_pole_and_fish:  |  **{}, you caught: :shopping_cart:!**'.format(ctx.message.author.name), #Shopping Cart
            ':fishing_pole_and_fish:  |  **{}, you caught: :shopping_cart:!**'.format(ctx.message.author.name), #Shopping Cart
            ':fishing_pole_and_fish:  |  **{}, you caught: :shopping_cart:!**'.format(ctx.message.author.name), #Shopping Cart
            ':fishing_pole_and_fish:  |  **{}, you caught: :shopping_cart:!**'.format(ctx.message.author.name), #Shopping Cart
            ':fishing_pole_and_fish:  |  **{}, you caught: :shopping_cart:!**'.format(ctx.message.author.name), #Shopping Cart
            ':fishing_pole_and_fish:  |  **{}, you caught: :shopping_cart:!**'.format(ctx.message.author.name), #Shopping Cart
            ':fishing_pole_and_fish:  |  **{}, you caught: :shopping_cart:!**'.format(ctx.message.author.name), #Shopping Cart
            ':fishing_pole_and_fish:  |  **{}, you caught: :shopping_cart:!**'.format(ctx.message.author.name), #Shopping Cart
            ':fishing_pole_and_fish:  |  **{}, you caught: :shopping_cart:!**'.format(ctx.message.author.name), #Shopping Cart
            ':fishing_pole_and_fish:  |  **{}, you caught: :shopping_cart:!**'.format(ctx.message.author.name), #Shopping Cart
            ':fishing_pole_and_fish:  |  **{}, you caught: :shopping_cart:!**'.format(ctx.message.author.name), #Shopping Cart
            ':fishing_pole_and_fish:  |  **{}, you caught: :shopping_cart:!**'.format(ctx.message.author.name), #Shopping Cart
            ':fishing_pole_and_fish:  |  **{}, you caught: :shopping_cart:!**'.format(ctx.message.author.name), #Shopping Cart
            ':fishing_pole_and_fish:  |  **{}, you caught: :shopping_cart:!**'.format(ctx.message.author.name), #Shopping Cart
            ':fishing_pole_and_fish:  |  **{}, you caught: :shopping_cart:!**'.format(ctx.message.author.name), #Shopping Cart
            ':fishing_pole_and_fish:  |  **{}, you caught: :shopping_cart:!**'.format(ctx.message.author.name), #Shopping Cart
            ':fishing_pole_and_fish:  |  **{}, you caught: :shopping_cart:!**'.format(ctx.message.author.name), #Shopping Cart
            ':fishing_pole_and_fish:  |  **{}, you caught: :shopping_cart:!**'.format(ctx.message.author.name), #Shopping Cart
            ':fishing_pole_and_fish:  |  **{}, you caught: :shopping_cart:!**'.format(ctx.message.author.name), #Shopping Cart
            ':fishing_pole_and_fish:  |  **{}, you caught: :shopping_cart:!**'.format(ctx.message.author.name), #Shopping Cart
            ':fishing_pole_and_fish:  |  **{}, you caught: :shopping_cart:!**'.format(ctx.message.author.name), #Shopping Cart
            ':fishing_pole_and_fish:  |  **{}, you caught: :shopping_cart:!**'.format(ctx.message.author.name), #Shopping Cart
            ':fishing_pole_and_fish:  |  **{}, you caught: :shopping_cart:!**'.format(ctx.message.author.name), #Shopping Cart
            ':fishing_pole_and_fish:  |  **{}, you caught: :shopping_cart:!**'.format(ctx.message.author.name), #Shopping Cart
            ':fishing_pole_and_fish:  |  **{}, you caught: :shopping_cart:!**'.format(ctx.message.author.name), #Shopping Cart
            ':fishing_pole_and_fish:  |  **{}, you caught: :shopping_cart:!**'.format(ctx.message.author.name), #Shopping Cart
            ':fishing_pole_and_fish:  |  **{}, you caught: :shopping_cart:!**'.format(ctx.message.author.name), #Shopping Cart
            ':fishing_pole_and_fish:  |  **{}, you caught: :shopping_cart:!**'.format(ctx.message.author.name), #Shopping Cart
            ':fishing_pole_and_fish:  |  **{}, you caught: :shopping_cart:!**'.format(ctx.message.author.name), #Shopping Cart
            ':fishing_pole_and_fish:  |  **{}, you caught: :shopping_cart:!**'.format(ctx.message.author.name), #Shopping Cart
            ':fishing_pole_and_fish:  |  **{}, you caught: :shopping_cart:!**'.format(ctx.message.author.name), #Shopping Cart
            ':fishing_pole_and_fish:  |  **{}, you caught: :shopping_cart:!**'.format(ctx.message.author.name), #Shopping Cart
            ':fishing_pole_and_fish:  |  **{}, you caught: :shopping_cart:!**'.format(ctx.message.author.name), #Shopping Cart
            ':fishing_pole_and_fish:  |  **{}, you caught: :shopping_cart:!**'.format(ctx.message.author.name), #Shopping Cart
            ':fishing_pole_and_fish:  |  **{}, you caught: :shopping_cart:!**'.format(ctx.message.author.name), #Shopping Cart
            ':fishing_pole_and_fish:  |  **{}, you caught: :shopping_cart:!**'.format(ctx.message.author.name), #Shopping Cart
            ':fishing_pole_and_fish:  |  **{}, you caught: :shopping_cart:!**'.format(ctx.message.author.name), #Shopping Cart
            ':fishing_pole_and_fish:  |  **{}, you caught: :shopping_cart:!**'.format(ctx.message.author.name), #Shopping Cart
            ':fishing_pole_and_fish:  |  **{}, you caught: :shopping_cart:!**'.format(ctx.message.author.name), #Shopping Cart
            ':fishing_pole_and_fish:  |  **{}, you caught: :shopping_cart:!**'.format(ctx.message.author.name), #Shopping Cart
            ':fishing_pole_and_fish:  |  **{}, you caught: :shopping_cart:!**'.format(ctx.message.author.name), #Shopping Cart
            ':fishing_pole_and_fish:  |  **{}, you caught: :shopping_cart:!**'.format(ctx.message.author.name), #Shopping Cart
            ':fishing_pole_and_fish:  |  **{}, you caught: :shopping_cart:!**'.format(ctx.message.author.name), #Shopping Cart
            ':fishing_pole_and_fish:  |  **{}, you caught: :shopping_cart:!**'.format(ctx.message.author.name), #Shopping Cart
            ':fishing_pole_and_fish:  |  **{}, you caught: :shopping_cart:!**'.format(ctx.message.author.name), #Shopping Cart
            ':fishing_pole_and_fish:  |  **{}, you caught: :shopping_cart:!**'.format(ctx.message.author.name), #Shopping Cart
            ':fishing_pole_and_fish:  |  **{}, you caught: :shopping_cart:!**'.format(ctx.message.author.name), #Shopping Cart
            ':fishing_pole_and_fish:  |  **{}, you caught: :shopping_cart:!**'.format(ctx.message.author.name), #Shopping Cart
            ':fishing_pole_and_fish:  |  **{}, you caught: :shopping_cart:!**'.format(ctx.message.author.name), #Shopping Cart
            ':fishing_pole_and_fish:  |  **{}, you caught: :shopping_cart:!**'.format(ctx.message.author.name), #Shopping Cart
            ':fishing_pole_and_fish:  |  **{}, you caught: :shopping_cart:!**'.format(ctx.message.author.name), #Shopping Cart
            ':fishing_pole_and_fish:  |  **{}, you caught: :shopping_cart:!**'.format(ctx.message.author.name), #Shopping Cart
            ':fishing_pole_and_fish:  |  **{}, you caught: :shopping_cart:!**'.format(ctx.message.author.name), #Shopping Cart
            ':fishing_pole_and_fish:  |  **{}, you caught: :shopping_cart:!**'.format(ctx.message.author.name), #Shopping Cart
            ':fishing_pole_and_fish:  |  **{}, you caught: :shopping_cart:!**'.format(ctx.message.author.name), #Shopping Cart
            ':fishing_pole_and_fish:  |  **{}, you caught: :shopping_cart:!**'.format(ctx.message.author.name), #Shopping Cart
            ':fishing_pole_and_fish:  |  **{}, you caught: :shopping_cart:!**'.format(ctx.message.author.name), #Shopping Cart
            ':fishing_pole_and_fish:  |  **{}, you caught: :shopping_cart:!**'.format(ctx.message.author.name), #Shopping Cart
            ':fishing_pole_and_fish:  |  **{}, you caught: :shopping_cart:!**'.format(ctx.message.author.name), #Shopping Cart
            ':fishing_pole_and_fish:  |  **{}, you caught: :shopping_cart:!**'.format(ctx.message.author.name), #Shopping Cart
            ':fishing_pole_and_fish:  |  **{}, you caught: :shopping_cart:!**'.format(ctx.message.author.name), #Shopping Cart
            ':fishing_pole_and_fish:  |  **{}, you caught: :shopping_cart:!**'.format(ctx.message.author.name), #Shopping Cart
            ':fishing_pole_and_fish:  |  **{}, you caught: :shopping_cart:!**'.format(ctx.message.author.name), #Shopping Cart
            ':fishing_pole_and_fish:  |  **{}, you caught: :shopping_cart:!**'.format(ctx.message.author.name), #Shopping Cart
            ':fishing_pole_and_fish:  |  **{}, you caught: :shopping_cart:!**'.format(ctx.message.author.name), #Shopping Cart
            ':fishing_pole_and_fish:  |  **{}, you caught: :shopping_cart:!**'.format(ctx.message.author.name), #Shopping Cart
            ':fishing_pole_and_fish:  |  **{}, you caught: :shopping_cart:!**'.format(ctx.message.author.name), #Shopping Cart
            ':fishing_pole_and_fish:  |  **{}, you caught: :shopping_cart:!**'.format(ctx.message.author.name), #Shopping Cart
            ':fishing_pole_and_fish:  |  **{}, you caught: :shopping_cart:!**'.format(ctx.message.author.name), #Shopping Cart
            ':fishing_pole_and_fish:  |  **{}, you caught: :shopping_cart:!**'.format(ctx.message.author.name), #Shopping Cart
            ':fishing_pole_and_fish:  |  **{}, you caught: :shopping_cart:!**'.format(ctx.message.author.name), #Shopping Cart
            ':fishing_pole_and_fish:  |  **{}, you caught: :shopping_cart:!**'.format(ctx.message.author.name), #Shopping Cart
            ':fishing_pole_and_fish:  |  **{}, you caught: :shopping_cart:!**'.format(ctx.message.author.name), #Shopping Cart
            ':fishing_pole_and_fish:  |  **{}, you caught: :shopping_cart:!**'.format(ctx.message.author.name), #Shopping Cart
            ':fishing_pole_and_fish:  |  **{}, you caught: :shopping_cart:!**'.format(ctx.message.author.name), #Shopping Cart
            ':fishing_pole_and_fish:  |  **{}, you caught: :shopping_cart:!**'.format(ctx.message.author.name), #Shopping Cart
            ':fishing_pole_and_fish:  |  **{}, you caught: :shopping_cart:!**'.format(ctx.message.author.name), #Shopping Cart
            ':fishing_pole_and_fish:  |  **{}, you caught: :shopping_cart:!**'.format(ctx.message.author.name), #Shopping Cart
            ':fishing_pole_and_fish:  |  **{}, you caught: :shopping_cart:!**'.format(ctx.message.author.name), #Shopping Cart
            ':fishing_pole_and_fish:  |  **{}, you caught: :shopping_cart:!**'.format(ctx.message.author.name), #Shopping Cart
            ':fishing_pole_and_fish:  |  **{}, you caught: :shopping_cart:!**'.format(ctx.message.author.name), #Shopping Cart
            ':fishing_pole_and_fish:  |  **{}, you caught: :shopping_cart:!**'.format(ctx.message.author.name), #Shopping Cart
            ':fishing_pole_and_fish:  |  **{}, you caught: :paperclip:!**'.format(ctx.message.author.name), #Paper Clip
            ':fishing_pole_and_fish:  |  **{}, you caught: :paperclip:!**'.format(ctx.message.author.name), #Paper Clip
            ':fishing_pole_and_fish:  |  **{}, you caught: :paperclip:!**'.format(ctx.message.author.name), #Paper Clip
            ':fishing_pole_and_fish:  |  **{}, you caught: :paperclip:!**'.format(ctx.message.author.name), #Paper Clip
            ':fishing_pole_and_fish:  |  **{}, you caught: :paperclip:!**'.format(ctx.message.author.name), #Paper Clip
            ':fishing_pole_and_fish:  |  **{}, you caught: :paperclip:!**'.format(ctx.message.author.name), #Paper Clip
            ':fishing_pole_and_fish:  |  **{}, you caught: :paperclip:!**'.format(ctx.message.author.name), #Paper Clip
            ':fishing_pole_and_fish:  |  **{}, you caught: :paperclip:!**'.format(ctx.message.author.name), #Paper Clip
            ':fishing_pole_and_fish:  |  **{}, you caught: :paperclip:!**'.format(ctx.message.author.name), #Paper Clip
            ':fishing_pole_and_fish:  |  **{}, you caught: :paperclip:!**'.format(ctx.message.author.name), #Paper Clip
            ':fishing_pole_and_fish:  |  **{}, you caught: :paperclip:!**'.format(ctx.message.author.name), #Paper Clip
            ':fishing_pole_and_fish:  |  **{}, you caught: :paperclip:!**'.format(ctx.message.author.name), #Paper Clip
            ':fishing_pole_and_fish:  |  **{}, you caught: :paperclip:!**'.format(ctx.message.author.name), #Paper Clip
            ':fishing_pole_and_fish:  |  **{}, you caught: :paperclip:!**'.format(ctx.message.author.name), #Paper Clip
            ':fishing_pole_and_fish:  |  **{}, you caught: :paperclip:!**'.format(ctx.message.author.name), #Paper Clip
            ':fishing_pole_and_fish:  |  **{}, you caught: :paperclip:!**'.format(ctx.message.author.name), #Paper Clip
            ':fishing_pole_and_fish:  |  **{}, you caught: :paperclip:!**'.format(ctx.message.author.name), #Paper Clip
            ':fishing_pole_and_fish:  |  **{}, you caught: :paperclip:!**'.format(ctx.message.author.name), #Paper Clip
            ':fishing_pole_and_fish:  |  **{}, you caught: :paperclip:!**'.format(ctx.message.author.name), #Paper Clip
            ':fishing_pole_and_fish:  |  **{}, you caught: :paperclip:!**'.format(ctx.message.author.name), #Paper Clip
            ':fishing_pole_and_fish:  |  **{}, you caught: :paperclip:!**'.format(ctx.message.author.name), #Paper Clip
            ':fishing_pole_and_fish:  |  **{}, you caught: :paperclip:!**'.format(ctx.message.author.name), #Paper Clip
            ':fishing_pole_and_fish:  |  **{}, you caught: :paperclip:!**'.format(ctx.message.author.name), #Paper Clip
            ':fishing_pole_and_fish:  |  **{}, you caught: :paperclip:!**'.format(ctx.message.author.name), #Paper Clip
            ':fishing_pole_and_fish:  |  **{}, you caught: :paperclip:!**'.format(ctx.message.author.name), #Paper Clip
            ':fishing_pole_and_fish:  |  **{}, you caught: :paperclip:!**'.format(ctx.message.author.name), #Paper Clip
            ':fishing_pole_and_fish:  |  **{}, you caught: :paperclip:!**'.format(ctx.message.author.name), #Paper Clip
            ':fishing_pole_and_fish:  |  **{}, you caught: :paperclip:!**'.format(ctx.message.author.name), #Paper Clip
            ':fishing_pole_and_fish:  |  **{}, you caught: :paperclip:!**'.format(ctx.message.author.name), #Paper Clip
            ':fishing_pole_and_fish:  |  **{}, you caught: :paperclip:!**'.format(ctx.message.author.name), #Paper Clip
            ':fishing_pole_and_fish:  |  **{}, you caught: :paperclip:!**'.format(ctx.message.author.name), #Paper Clip
            ':fishing_pole_and_fish:  |  **{}, you caught: :paperclip:!**'.format(ctx.message.author.name), #Paper Clip
            ':fishing_pole_and_fish:  |  **{}, you caught: :paperclip:!**'.format(ctx.message.author.name), #Paper Clip
            ':fishing_pole_and_fish:  |  **{}, you caught: :paperclip:!**'.format(ctx.message.author.name), #Paper Clip
            ':fishing_pole_and_fish:  |  **{}, you caught: :paperclip:!**'.format(ctx.message.author.name), #Paper Clip
            ':fishing_pole_and_fish:  |  **{}, you caught: :paperclip:!**'.format(ctx.message.author.name), #Paper Clip
            ':fishing_pole_and_fish:  |  **{}, you caught: :paperclip:!**'.format(ctx.message.author.name), #Paper Clip
            ':fishing_pole_and_fish:  |  **{}, you caught: :paperclip:!**'.format(ctx.message.author.name), #Paper Clip
            ':fishing_pole_and_fish:  |  **{}, you caught: :paperclip:!**'.format(ctx.message.author.name), #Paper Clip
            ':fishing_pole_and_fish:  |  **{}, you caught: :paperclip:!**'.format(ctx.message.author.name), #Paper Clip
            ':fishing_pole_and_fish:  |  **{}, you caught: :paperclip:!**'.format(ctx.message.author.name), #Paper Clip
            ':fishing_pole_and_fish:  |  **{}, you caught: :paperclip:!**'.format(ctx.message.author.name), #Paper Clip
            ':fishing_pole_and_fish:  |  **{}, you caught: :paperclip:!**'.format(ctx.message.author.name), #Paper Clip
            ':fishing_pole_and_fish:  |  **{}, you caught: :paperclip:!**'.format(ctx.message.author.name), #Paper Clip
            ':fishing_pole_and_fish:  |  **{}, you caught: :paperclip:!**'.format(ctx.message.author.name), #Paper Clip
            ':fishing_pole_and_fish:  |  **{}, you caught: :paperclip:!**'.format(ctx.message.author.name), #Paper Clip
            ':fishing_pole_and_fish:  |  **{}, you caught: :paperclip:!**'.format(ctx.message.author.name), #Paper Clip
            ':fishing_pole_and_fish:  |  **{}, you caught: :paperclip:!**'.format(ctx.message.author.name), #Paper Clip
            ':fishing_pole_and_fish:  |  **{}, you caught: :paperclip:!**'.format(ctx.message.author.name), #Paper Clip
            ':fishing_pole_and_fish:  |  **{}, you caught: :paperclip:!**'.format(ctx.message.author.name), #Paper Clip
            ':fishing_pole_and_fish:  |  **{}, you caught: :paperclip:!**'.format(ctx.message.author.name), #Paper Clip
            ':fishing_pole_and_fish:  |  **{}, you caught: :paperclip:!**'.format(ctx.message.author.name), #Paper Clip
            ':fishing_pole_and_fish:  |  **{}, you caught: :paperclip:!**'.format(ctx.message.author.name), #Paper Clip
            ':fishing_pole_and_fish:  |  **{}, you caught: :paperclip:!**'.format(ctx.message.author.name), #Paper Clip
            ':fishing_pole_and_fish:  |  **{}, you caught: :paperclip:!**'.format(ctx.message.author.name), #Paper Clip
            ':fishing_pole_and_fish:  |  **{}, you caught: :paperclip:!**'.format(ctx.message.author.name), #Paper Clip
            ':fishing_pole_and_fish:  |  **{}, you caught: :paperclip:!**'.format(ctx.message.author.name), #Paper Clip
            ':fishing_pole_and_fish:  |  **{}, you caught: :paperclip:!**'.format(ctx.message.author.name), #Paper Clip
            ':fishing_pole_and_fish:  |  **{}, you caught: :paperclip:!**'.format(ctx.message.author.name), #Paper Clip
            ':fishing_pole_and_fish:  |  **{}, you caught: :paperclip:!**'.format(ctx.message.author.name), #Paper Clip
            ':fishing_pole_and_fish:  |  **{}, you caught: :paperclip:!**'.format(ctx.message.author.name), #Paper Clip
            ':fishing_pole_and_fish:  |  **{}, you caught: :paperclip:!**'.format(ctx.message.author.name), #Paper Clip
            ':fishing_pole_and_fish:  |  **{}, you caught: :paperclip:!**'.format(ctx.message.author.name), #Paper Clip
            ':fishing_pole_and_fish:  |  **{}, you caught: :paperclip:!**'.format(ctx.message.author.name), #Paper Clip
            ':fishing_pole_and_fish:  |  **{}, you caught: :paperclip:!**'.format(ctx.message.author.name), #Paper Clip
            ':fishing_pole_and_fish:  |  **{}, you caught: :paperclip:!**'.format(ctx.message.author.name), #Paper Clip
            ':fishing_pole_and_fish:  |  **{}, you caught: :paperclip:!**'.format(ctx.message.author.name), #Paper Clip
            ':fishing_pole_and_fish:  |  **{}, you caught: :paperclip:!**'.format(ctx.message.author.name), #Paper Clip
            ':fishing_pole_and_fish:  |  **{}, you caught: :paperclip:!**'.format(ctx.message.author.name), #Paper Clip
            ':fishing_pole_and_fish:  |  **{}, you caught: :paperclip:!**'.format(ctx.message.author.name), #Paper Clip
            ':fishing_pole_and_fish:  |  **{}, you caught: :paperclip:!**'.format(ctx.message.author.name), #Paper Clip
            ':fishing_pole_and_fish:  |  **{}, you caught: :paperclip:!**'.format(ctx.message.author.name), #Paper Clip
            ':fishing_pole_and_fish:  |  **{}, you caught: :paperclip:!**'.format(ctx.message.author.name), #Paper Clip
            ':fishing_pole_and_fish:  |  **{}, you caught: :paperclip:!**'.format(ctx.message.author.name), #Paper Clip
            ':fishing_pole_and_fish:  |  **{}, you caught: :paperclip:!**'.format(ctx.message.author.name), #Paper Clip
            ':fishing_pole_and_fish:  |  **{}, you caught: :paperclip:!**'.format(ctx.message.author.name), #Paper Clip
            ':fishing_pole_and_fish:  |  **{}, you caught: :paperclip:!**'.format(ctx.message.author.name), #Paper Clip
            ':fishing_pole_and_fish:  |  **{}, you caught: :paperclip:!**'.format(ctx.message.author.name), #Paper Clip
            ':fishing_pole_and_fish:  |  **{}, you caught: :paperclip:!**'.format(ctx.message.author.name), #Paper Clip
            ':fishing_pole_and_fish:  |  **{}, you caught: :paperclip:!**'.format(ctx.message.author.name), #Paper Clip
            ':fishing_pole_and_fish:  |  **{}, you caught: :paperclip:!**'.format(ctx.message.author.name), #Paper Clip
            ':fishing_pole_and_fish:  |  **{}, you caught: :paperclip:!**'.format(ctx.message.author.name), #Paper Clip
            ':fishing_pole_and_fish:  |  **{}, you caught: :paperclip:!**'.format(ctx.message.author.name), #Paper Clip
            ':fishing_pole_and_fish:  |  **{}, you caught: :paperclip:!**'.format(ctx.message.author.name), #Paper Clip
            ':fishing_pole_and_fish:  |  **{}, you caught: :paperclip:!**'.format(ctx.message.author.name), #Paper Clip
            ':fishing_pole_and_fish:  |  **{}, you caught: :paperclip:!**'.format(ctx.message.author.name), #Paper Clip
            ':fishing_pole_and_fish:  |  **{}, you caught: :paperclip:!**'.format(ctx.message.author.name), #Paper Clip
            ':fishing_pole_and_fish:  |  **{}, you caught: :paperclip:!**'.format(ctx.message.author.name), #Paper Clip
            ':fishing_pole_and_fish:  |  **{}, you caught: :paperclip:!**'.format(ctx.message.author.name), #Paper Clip
            ':fishing_pole_and_fish:  |  **{}, you caught: :paperclip:!**'.format(ctx.message.author.name), #Paper Clip
            ':fishing_pole_and_fish:  |  **{}, you caught: :paperclip:!**'.format(ctx.message.author.name), #Paper Clip
            ':fishing_pole_and_fish:  |  **{}, you caught: :paperclip:!**'.format(ctx.message.author.name), #Paper Clip
            ':fishing_pole_and_fish:  |  **{}, you caught: :paperclip:!**'.format(ctx.message.author.name), #Paper Clip
            ':fishing_pole_and_fish:  |  **{}, you caught: :paperclip:!**'.format(ctx.message.author.name), #Paper Clip
            ':fishing_pole_and_fish:  |  **{}, you caught: :paperclip:!**'.format(ctx.message.author.name), #Paper Clip
            ':fishing_pole_and_fish:  |  **{}, you caught: :paperclip:!**'.format(ctx.message.author.name), #Paper Clip
            ':fishing_pole_and_fish:  |  **{}, you caught: :paperclip:!**'.format(ctx.message.author.name), #Paper Clip
            ':fishing_pole_and_fish:  |  **{}, you caught: :paperclip:!**'.format(ctx.message.author.name), #Paper Clip
            ':fishing_pole_and_fish:  |  **{}, you caught: :paperclip:!**'.format(ctx.message.author.name), #Paper Clip
            ':fishing_pole_and_fish:  |  **{}, you caught: :paperclip:!**'.format(ctx.message.author.name), #Paper Clip
            ':fishing_pole_and_fish:  |  **{}, you caught: :paperclip:!**'.format(ctx.message.author.name), #Paper Clip
            ':fishing_pole_and_fish:  |  **{}, you caught: :paperclip:!**'.format(ctx.message.author.name), #Paper Clip
            ':fishing_pole_and_fish:  |  **{}, you caught: :paperclip:!**'.format(ctx.message.author.name), #Paper Clip
            ':fishing_pole_and_fish:  |  **{}, you caught: :paperclip:!**'.format(ctx.message.author.name), #Paper Clip
            ':fishing_pole_and_fish:  |  **{}, you caught: :paperclip:!**'.format(ctx.message.author.name), #Paper Clip
            ':fishing_pole_and_fish:  |  **{}, you caught: :wrench:!**'.format(ctx.message.author.name), #Wrench
            ':fishing_pole_and_fish:  |  **{}, you caught: :wrench:!**'.format(ctx.message.author.name), #Wrench
            ':fishing_pole_and_fish:  |  **{}, you caught: :wrench:!**'.format(ctx.message.author.name), #Wrench
            ':fishing_pole_and_fish:  |  **{}, you caught: :wrench:!**'.format(ctx.message.author.name), #Wrench
            ':fishing_pole_and_fish:  |  **{}, you caught: :wrench:!**'.format(ctx.message.author.name), #Wrench
            ':fishing_pole_and_fish:  |  **{}, you caught: :wrench:!**'.format(ctx.message.author.name), #Wrench
            ':fishing_pole_and_fish:  |  **{}, you caught: :wrench:!**'.format(ctx.message.author.name), #Wrench
            ':fishing_pole_and_fish:  |  **{}, you caught: :wrench:!**'.format(ctx.message.author.name), #Wrench
            ':fishing_pole_and_fish:  |  **{}, you caught: :wrench:!**'.format(ctx.message.author.name), #Wrench
            ':fishing_pole_and_fish:  |  **{}, you caught: :wrench:!**'.format(ctx.message.author.name), #Wrench
            ':fishing_pole_and_fish:  |  **{}, you caught: :wrench:!**'.format(ctx.message.author.name), #Wrench
            ':fishing_pole_and_fish:  |  **{}, you caught: :wrench:!**'.format(ctx.message.author.name), #Wrench
            ':fishing_pole_and_fish:  |  **{}, you caught: :wrench:!**'.format(ctx.message.author.name), #Wrench
            ':fishing_pole_and_fish:  |  **{}, you caught: :wrench:!**'.format(ctx.message.author.name), #Wrench
            ':fishing_pole_and_fish:  |  **{}, you caught: :wrench:!**'.format(ctx.message.author.name), #Wrench
            ':fishing_pole_and_fish:  |  **{}, you caught: :wrench:!**'.format(ctx.message.author.name), #Wrench
            ':fishing_pole_and_fish:  |  **{}, you caught: :wrench:!**'.format(ctx.message.author.name), #Wrench
            ':fishing_pole_and_fish:  |  **{}, you caught: :wrench:!**'.format(ctx.message.author.name), #Wrench
            ':fishing_pole_and_fish:  |  **{}, you caught: :wrench:!**'.format(ctx.message.author.name), #Wrench
            ':fishing_pole_and_fish:  |  **{}, you caught: :wrench:!**'.format(ctx.message.author.name), #Wrench
            ':fishing_pole_and_fish:  |  **{}, you caught: :wrench:!**'.format(ctx.message.author.name), #Wrench
            ':fishing_pole_and_fish:  |  **{}, you caught: :wrench:!**'.format(ctx.message.author.name), #Wrench
            ':fishing_pole_and_fish:  |  **{}, you caught: :wrench:!**'.format(ctx.message.author.name), #Wrench
            ':fishing_pole_and_fish:  |  **{}, you caught: :wrench:!**'.format(ctx.message.author.name), #Wrench
            ':fishing_pole_and_fish:  |  **{}, you caught: :wrench:!**'.format(ctx.message.author.name), #Wrench
            ':fishing_pole_and_fish:  |  **{}, you caught: :wrench:!**'.format(ctx.message.author.name), #Wrench
            ':fishing_pole_and_fish:  |  **{}, you caught: :wrench:!**'.format(ctx.message.author.name), #Wrench
            ':fishing_pole_and_fish:  |  **{}, you caught: :wrench:!**'.format(ctx.message.author.name), #Wrench
            ':fishing_pole_and_fish:  |  **{}, you caught: :wrench:!**'.format(ctx.message.author.name), #Wrench
            ':fishing_pole_and_fish:  |  **{}, you caught: :wrench:!**'.format(ctx.message.author.name), #Wrench
            ':fishing_pole_and_fish:  |  **{}, you caught: :wrench:!**'.format(ctx.message.author.name), #Wrench
            ':fishing_pole_and_fish:  |  **{}, you caught: :wrench:!**'.format(ctx.message.author.name), #Wrench
            ':fishing_pole_and_fish:  |  **{}, you caught: :wrench:!**'.format(ctx.message.author.name), #Wrench
            ':fishing_pole_and_fish:  |  **{}, you caught: :wrench:!**'.format(ctx.message.author.name), #Wrench
            ':fishing_pole_and_fish:  |  **{}, you caught: :wrench:!**'.format(ctx.message.author.name), #Wrench
            ':fishing_pole_and_fish:  |  **{}, you caught: :wrench:!**'.format(ctx.message.author.name), #Wrench
            ':fishing_pole_and_fish:  |  **{}, you caught: :wrench:!**'.format(ctx.message.author.name), #Wrench
            ':fishing_pole_and_fish:  |  **{}, you caught: :wrench:!**'.format(ctx.message.author.name), #Wrench
            ':fishing_pole_and_fish:  |  **{}, you caught: :wrench:!**'.format(ctx.message.author.name), #Wrench
            ':fishing_pole_and_fish:  |  **{}, you caught: :wrench:!**'.format(ctx.message.author.name), #Wrench
            ':fishing_pole_and_fish:  |  **{}, you caught: :wrench:!**'.format(ctx.message.author.name), #Wrench
            ':fishing_pole_and_fish:  |  **{}, you caught: :wrench:!**'.format(ctx.message.author.name), #Wrench
            ':fishing_pole_and_fish:  |  **{}, you caught: :wrench:!**'.format(ctx.message.author.name), #Wrench
            ':fishing_pole_and_fish:  |  **{}, you caught: :wrench:!**'.format(ctx.message.author.name), #Wrench
            ':fishing_pole_and_fish:  |  **{}, you caught: :wrench:!**'.format(ctx.message.author.name), #Wrench
            ':fishing_pole_and_fish:  |  **{}, you caught: :wrench:!**'.format(ctx.message.author.name), #Wrench
            ':fishing_pole_and_fish:  |  **{}, you caught: :wrench:!**'.format(ctx.message.author.name), #Wrench
            ':fishing_pole_and_fish:  |  **{}, you caught: :wrench:!**'.format(ctx.message.author.name), #Wrench
            ':fishing_pole_and_fish:  |  **{}, you caught: :wrench:!**'.format(ctx.message.author.name), #Wrench
            ':fishing_pole_and_fish:  |  **{}, you caught: :wrench:!**'.format(ctx.message.author.name), #Wrench
            ':fishing_pole_and_fish:  |  **{}, you caught: :wrench:!**'.format(ctx.message.author.name), #Wrench
            ':fishing_pole_and_fish:  |  **{}, you caught: :wrench:!**'.format(ctx.message.author.name), #Wrench
            ':fishing_pole_and_fish:  |  **{}, you caught: :wrench:!**'.format(ctx.message.author.name), #Wrench
            ':fishing_pole_and_fish:  |  **{}, you caught: :wrench:!**'.format(ctx.message.author.name), #Wrench
            ':fishing_pole_and_fish:  |  **{}, you caught: :wrench:!**'.format(ctx.message.author.name), #Wrench
            ':fishing_pole_and_fish:  |  **{}, you caught: :wrench:!**'.format(ctx.message.author.name), #Wrench
            ':fishing_pole_and_fish:  |  **{}, you caught: :wrench:!**'.format(ctx.message.author.name), #Wrench
            ':fishing_pole_and_fish:  |  **{}, you caught: :wrench:!**'.format(ctx.message.author.name), #Wrench
            ':fishing_pole_and_fish:  |  **{}, you caught: :wrench:!**'.format(ctx.message.author.name), #Wrench
            ':fishing_pole_and_fish:  |  **{}, you caught: :wrench:!**'.format(ctx.message.author.name), #Wrench
            ':fishing_pole_and_fish:  |  **{}, you caught: :wrench:!**'.format(ctx.message.author.name), #Wrench
            ':fishing_pole_and_fish:  |  **{}, you caught: :wrench:!**'.format(ctx.message.author.name), #Wrench
            ':fishing_pole_and_fish:  |  **{}, you caught: :wrench:!**'.format(ctx.message.author.name), #Wrench
            ':fishing_pole_and_fish:  |  **{}, you caught: :wrench:!**'.format(ctx.message.author.name), #Wrench
            ':fishing_pole_and_fish:  |  **{}, you caught: :wrench:!**'.format(ctx.message.author.name), #Wrench
            ':fishing_pole_and_fish:  |  **{}, you caught: :wrench:!**'.format(ctx.message.author.name), #Wrench
            ':fishing_pole_and_fish:  |  **{}, you caught: :wrench:!**'.format(ctx.message.author.name), #Wrench
            ':fishing_pole_and_fish:  |  **{}, you caught: :wrench:!**'.format(ctx.message.author.name), #Wrench
            ':fishing_pole_and_fish:  |  **{}, you caught: :wrench:!**'.format(ctx.message.author.name), #Wrench
            ':fishing_pole_and_fish:  |  **{}, you caught: :wrench:!**'.format(ctx.message.author.name), #Wrench
            ':fishing_pole_and_fish:  |  **{}, you caught: :wrench:!**'.format(ctx.message.author.name), #Wrench
            ':fishing_pole_and_fish:  |  **{}, you caught: :wrench:!**'.format(ctx.message.author.name), #Wrench
            ':fishing_pole_and_fish:  |  **{}, you caught: :wrench:!**'.format(ctx.message.author.name), #Wrench
            ':fishing_pole_and_fish:  |  **{}, you caught: :wrench:!**'.format(ctx.message.author.name), #Wrench
            ':fishing_pole_and_fish:  |  **{}, you caught: :wrench:!**'.format(ctx.message.author.name), #Wrench
            ':fishing_pole_and_fish:  |  **{}, you caught: :wrench:!**'.format(ctx.message.author.name), #Wrench
            ':fishing_pole_and_fish:  |  **{}, you caught: :wrench:!**'.format(ctx.message.author.name), #Wrench
            ':fishing_pole_and_fish:  |  **{}, you caught: :wrench:!**'.format(ctx.message.author.name), #Wrench
            ':fishing_pole_and_fish:  |  **{}, you caught: :wrench:!**'.format(ctx.message.author.name), #Wrench
            ':fishing_pole_and_fish:  |  **{}, you caught: :wrench:!**'.format(ctx.message.author.name), #Wrench
            ':fishing_pole_and_fish:  |  **{}, you caught: :wrench:!**'.format(ctx.message.author.name), #Wrench
            ':fishing_pole_and_fish:  |  **{}, you caught: :mans_shoe:!**'.format(ctx.message.author.name), #Shoes
            ':fishing_pole_and_fish:  |  **{}, you caught: :mans_shoe:!**'.format(ctx.message.author.name), #Shoes
            ':fishing_pole_and_fish:  |  **{}, you caught: :mans_shoe:!**'.format(ctx.message.author.name), #Shoes
            ':fishing_pole_and_fish:  |  **{}, you caught: :mans_shoe:!**'.format(ctx.message.author.name), #Shoes
            ':fishing_pole_and_fish:  |  **{}, you caught: :mans_shoe:!**'.format(ctx.message.author.name), #Shoes
            ':fishing_pole_and_fish:  |  **{}, you caught: :mans_shoe:!**'.format(ctx.message.author.name), #Shoes
            ':fishing_pole_and_fish:  |  **{}, you caught: :mans_shoe:!**'.format(ctx.message.author.name), #Shoes
            ':fishing_pole_and_fish:  |  **{}, you caught: :mans_shoe:!**'.format(ctx.message.author.name), #Shoes
            ':fishing_pole_and_fish:  |  **{}, you caught: :mans_shoe:!**'.format(ctx.message.author.name), #Shoes
            ':fishing_pole_and_fish:  |  **{}, you caught: :mans_shoe:!**'.format(ctx.message.author.name), #Shoes
            ':fishing_pole_and_fish:  |  **{}, you caught: :mans_shoe:!**'.format(ctx.message.author.name), #Shoes
            ':fishing_pole_and_fish:  |  **{}, you caught: :mans_shoe:!**'.format(ctx.message.author.name), #Shoes
            ':fishing_pole_and_fish:  |  **{}, you caught: :mans_shoe:!**'.format(ctx.message.author.name), #Shoes
            ':fishing_pole_and_fish:  |  **{}, you caught: :mans_shoe:!**'.format(ctx.message.author.name), #Shoes
            ':fishing_pole_and_fish:  |  **{}, you caught: :mans_shoe:!**'.format(ctx.message.author.name), #Shoes
            ':fishing_pole_and_fish:  |  **{}, you caught: :mans_shoe:!**'.format(ctx.message.author.name), #Shoes
            ':fishing_pole_and_fish:  |  **{}, you caught: :mans_shoe:!**'.format(ctx.message.author.name), #Shoes
            ':fishing_pole_and_fish:  |  **{}, you caught: :mans_shoe:!**'.format(ctx.message.author.name), #Shoes
            ':fishing_pole_and_fish:  |  **{}, you caught: :mans_shoe:!**'.format(ctx.message.author.name), #Shoes
            ':fishing_pole_and_fish:  |  **{}, you caught: :mans_shoe:!**'.format(ctx.message.author.name), #Shoes
            ':fishing_pole_and_fish:  |  **{}, you caught: :mans_shoe:!**'.format(ctx.message.author.name), #Shoes
            ':fishing_pole_and_fish:  |  **{}, you caught: :mans_shoe:!**'.format(ctx.message.author.name), #Shoes
            ':fishing_pole_and_fish:  |  **{}, you caught: :mans_shoe:!**'.format(ctx.message.author.name), #Shoes
            ':fishing_pole_and_fish:  |  **{}, you caught: :mans_shoe:!**'.format(ctx.message.author.name), #Shoes
            ':fishing_pole_and_fish:  |  **{}, you caught: :mans_shoe:!**'.format(ctx.message.author.name), #Shoes
            ':fishing_pole_and_fish:  |  **{}, you caught: :mans_shoe:!**'.format(ctx.message.author.name), #Shoes
            ':fishing_pole_and_fish:  |  **{}, you caught: :mans_shoe:!**'.format(ctx.message.author.name), #Shoes
            ':fishing_pole_and_fish:  |  **{}, you caught: :mans_shoe:!**'.format(ctx.message.author.name), #Shoes
            ':fishing_pole_and_fish:  |  **{}, you caught: :mans_shoe:!**'.format(ctx.message.author.name), #Shoes
            ':fishing_pole_and_fish:  |  **{}, you caught: :mans_shoe:!**'.format(ctx.message.author.name), #Shoes
            ':fishing_pole_and_fish:  |  **{}, you caught: :mans_shoe:!**'.format(ctx.message.author.name), #Shoes
            ':fishing_pole_and_fish:  |  **{}, you caught: :mans_shoe:!**'.format(ctx.message.author.name), #Shoes
            ':fishing_pole_and_fish:  |  **{}, you caught: :mans_shoe:!**'.format(ctx.message.author.name), #Shoes
            ':fishing_pole_and_fish:  |  **{}, you caught: :mans_shoe:!**'.format(ctx.message.author.name), #Shoes
            ':fishing_pole_and_fish:  |  **{}, you caught: :mans_shoe:!**'.format(ctx.message.author.name), #Shoes
            ':fishing_pole_and_fish:  |  **{}, you caught: :mans_shoe:!**'.format(ctx.message.author.name), #Shoes
            ':fishing_pole_and_fish:  |  **{}, you caught: :mans_shoe:!**'.format(ctx.message.author.name), #Shoes
            ':fishing_pole_and_fish:  |  **{}, you caught: :mans_shoe:!**'.format(ctx.message.author.name), #Shoes
            ':fishing_pole_and_fish:  |  **{}, you caught: :mans_shoe:!**'.format(ctx.message.author.name), #Shoes
            ':fishing_pole_and_fish:  |  **{}, you caught: :mans_shoe:!**'.format(ctx.message.author.name), #Shoes
            ':fishing_pole_and_fish:  |  **{}, you caught: :mans_shoe:!**'.format(ctx.message.author.name), #Shoes
            ':fishing_pole_and_fish:  |  **{}, you caught: :mans_shoe:!**'.format(ctx.message.author.name), #Shoes
            ':fishing_pole_and_fish:  |  **{}, you caught: :mans_shoe:!**'.format(ctx.message.author.name), #Shoes
            ':fishing_pole_and_fish:  |  **{}, you caught: :mans_shoe:!**'.format(ctx.message.author.name), #Shoes
            ':fishing_pole_and_fish:  |  **{}, you caught: :mans_shoe:!**'.format(ctx.message.author.name), #Shoes
            ':fishing_pole_and_fish:  |  **{}, you caught: :mans_shoe:!**'.format(ctx.message.author.name), #Shoes
            ':fishing_pole_and_fish:  |  **{}, you caught: :mans_shoe:!**'.format(ctx.message.author.name), #Shoes
            ':fishing_pole_and_fish:  |  **{}, you caught: :mans_shoe:!**'.format(ctx.message.author.name), #Shoes
            ':fishing_pole_and_fish:  |  **{}, you caught: :mans_shoe:!**'.format(ctx.message.author.name), #Shoes
            ':fishing_pole_and_fish:  |  **{}, you caught: :mans_shoe:!**'.format(ctx.message.author.name), #Shoes
            ':fishing_pole_and_fish:  |  **{}, you caught: :mans_shoe:!**'.format(ctx.message.author.name), #Shoes
            ':fishing_pole_and_fish:  |  **{}, you caught: :mans_shoe:!**'.format(ctx.message.author.name), #Shoes
            ':fishing_pole_and_fish:  |  **{}, you caught: :mans_shoe:!**'.format(ctx.message.author.name), #Shoes
            ':fishing_pole_and_fish:  |  **{}, you caught: :mans_shoe:!**'.format(ctx.message.author.name), #Shoes
            ':fishing_pole_and_fish:  |  **{}, you caught: :mans_shoe:!**'.format(ctx.message.author.name), #Shoes
            ':fishing_pole_and_fish:  |  **{}, you caught: :mans_shoe:!**'.format(ctx.message.author.name), #Shoes
            ':fishing_pole_and_fish:  |  **{}, you caught: :mans_shoe:!**'.format(ctx.message.author.name), #Shoes
            ':fishing_pole_and_fish:  |  **{}, you caught: :mans_shoe:!**'.format(ctx.message.author.name), #Shoes
            ':fishing_pole_and_fish:  |  **{}, you caught: :mans_shoe:!**'.format(ctx.message.author.name), #Shoes
            ':fishing_pole_and_fish:  |  **{}, you caught: :mans_shoe:!**'.format(ctx.message.author.name), #Shoes
            ':fishing_pole_and_fish:  |  **{}, you caught: :mans_shoe:!**'.format(ctx.message.author.name), #Shoes
            ':fishing_pole_and_fish:  |  **{}, you caught: :mans_shoe:!**'.format(ctx.message.author.name), #Shoes
            ':fishing_pole_and_fish:  |  **{}, you caught: :mans_shoe:!**'.format(ctx.message.author.name), #Shoes
            ':fishing_pole_and_fish:  |  **{}, you caught: :mans_shoe:!**'.format(ctx.message.author.name), #Shoes
            ':fishing_pole_and_fish:  |  **{}, you caught: :mans_shoe:!**'.format(ctx.message.author.name), #Shoes
            ':fishing_pole_and_fish:  |  **{}, you caught: :mans_shoe:!**'.format(ctx.message.author.name), #Shoes
            ':fishing_pole_and_fish:  |  **{}, you caught: :mans_shoe:!**'.format(ctx.message.author.name), #Shoes
            ':fishing_pole_and_fish:  |  **{}, you caught: :mans_shoe:!**'.format(ctx.message.author.name), #Shoes
            ':fishing_pole_and_fish:  |  **{}, you caught: :mans_shoe:!**'.format(ctx.message.author.name), #Shoes
            ':fishing_pole_and_fish:  |  **{}, you caught: :mans_shoe:!**'.format(ctx.message.author.name), #Shoes
            ':fishing_pole_and_fish:  |  **{}, you caught: :mans_shoe:!**'.format(ctx.message.author.name), #Shoes
            ':fishing_pole_and_fish:  |  **{}, you caught: :mans_shoe:!**'.format(ctx.message.author.name), #Shoes
            ':fishing_pole_and_fish:  |  **{}, you caught: :mans_shoe:!**'.format(ctx.message.author.name), #Shoes
            ':fishing_pole_and_fish:  |  **{}, you caught: :mans_shoe:!**'.format(ctx.message.author.name), #Shoes
            ':fishing_pole_and_fish:  |  **{}, you caught: :mans_shoe:!**'.format(ctx.message.author.name), #Shoes
            ':fishing_pole_and_fish:  |  **{}, you caught: :mans_shoe:!**'.format(ctx.message.author.name), #Shoes
            ':fishing_pole_and_fish:  |  **{}, you caught: :mans_shoe:!**'.format(ctx.message.author.name), #Shoes
            ':fishing_pole_and_fish:  |  **{}, you caught: :mans_shoe:!**'.format(ctx.message.author.name), #Shoes
            ':fishing_pole_and_fish:  |  **{}, you caught: :battery:!**'.format(ctx.message.author.name), #Battery
            ':fishing_pole_and_fish:  |  **{}, you caught: :battery:!**'.format(ctx.message.author.name), #Battery
            ':fishing_pole_and_fish:  |  **{}, you caught: :battery:!**'.format(ctx.message.author.name), #Battery
            ':fishing_pole_and_fish:  |  **{}, you caught: :battery:!**'.format(ctx.message.author.name), #Battery
            ':fishing_pole_and_fish:  |  **{}, you caught: :battery:!**'.format(ctx.message.author.name), #Battery
            ':fishing_pole_and_fish:  |  **{}, you caught: :battery:!**'.format(ctx.message.author.name), #Battery
            ':fishing_pole_and_fish:  |  **{}, you caught: :battery:!**'.format(ctx.message.author.name), #Battery
            ':fishing_pole_and_fish:  |  **{}, you caught: :battery:!**'.format(ctx.message.author.name), #Battery
            ':fishing_pole_and_fish:  |  **{}, you caught: :battery:!**'.format(ctx.message.author.name), #Battery
            ':fishing_pole_and_fish:  |  **{}, you caught: :battery:!**'.format(ctx.message.author.name), #Battery
            ':fishing_pole_and_fish:  |  **{}, you caught: :battery:!**'.format(ctx.message.author.name), #Battery
            ':fishing_pole_and_fish:  |  **{}, you caught: :battery:!**'.format(ctx.message.author.name), #Battery
            ':fishing_pole_and_fish:  |  **{}, you caught: :battery:!**'.format(ctx.message.author.name), #Battery
            ':fishing_pole_and_fish:  |  **{}, you caught: :battery:!**'.format(ctx.message.author.name), #Battery
            ':fishing_pole_and_fish:  |  **{}, you caught: :battery:!**'.format(ctx.message.author.name), #Battery
            ':fishing_pole_and_fish:  |  **{}, you caught: :battery:!**'.format(ctx.message.author.name), #Battery
            ':fishing_pole_and_fish:  |  **{}, you caught: :battery:!**'.format(ctx.message.author.name), #Battery
            ':fishing_pole_and_fish:  |  **{}, you caught: :battery:!**'.format(ctx.message.author.name), #Battery
            ':fishing_pole_and_fish:  |  **{}, you caught: :battery:!**'.format(ctx.message.author.name), #Battery
            ':fishing_pole_and_fish:  |  **{}, you caught: :battery:!**'.format(ctx.message.author.name), #Battery
            ':fishing_pole_and_fish:  |  **{}, you caught: :battery:!**'.format(ctx.message.author.name), #Battery
            ':fishing_pole_and_fish:  |  **{}, you caught: :battery:!**'.format(ctx.message.author.name), #Battery
            ':fishing_pole_and_fish:  |  **{}, you caught: :battery:!**'.format(ctx.message.author.name), #Battery
            ':fishing_pole_and_fish:  |  **{}, you caught: :battery:!**'.format(ctx.message.author.name), #Battery
            ':fishing_pole_and_fish:  |  **{}, you caught: :battery:!**'.format(ctx.message.author.name), #Battery
            ':fishing_pole_and_fish:  |  **{}, you caught: :battery:!**'.format(ctx.message.author.name), #Battery
            ':fishing_pole_and_fish:  |  **{}, you caught: :battery:!**'.format(ctx.message.author.name), #Battery
            ':fishing_pole_and_fish:  |  **{}, you caught: :battery:!**'.format(ctx.message.author.name), #Battery
            ':fishing_pole_and_fish:  |  **{}, you caught: :battery:!**'.format(ctx.message.author.name), #Battery
            ':fishing_pole_and_fish:  |  **{}, you caught: :battery:!**'.format(ctx.message.author.name), #Battery
            ':fishing_pole_and_fish:  |  **{}, you caught: :battery:!**'.format(ctx.message.author.name), #Battery
            ':fishing_pole_and_fish:  |  **{}, you caught: :battery:!**'.format(ctx.message.author.name), #Battery
            ':fishing_pole_and_fish:  |  **{}, you caught: :battery:!**'.format(ctx.message.author.name), #Battery
            ':fishing_pole_and_fish:  |  **{}, you caught: :battery:!**'.format(ctx.message.author.name), #Battery
            ':fishing_pole_and_fish:  |  **{}, you caught: :battery:!**'.format(ctx.message.author.name), #Battery
            ':fishing_pole_and_fish:  |  **{}, you caught: :battery:!**'.format(ctx.message.author.name), #Battery
            ':fishing_pole_and_fish:  |  **{}, you caught: :battery:!**'.format(ctx.message.author.name), #Battery
            ':fishing_pole_and_fish:  |  **{}, you caught: :battery:!**'.format(ctx.message.author.name), #Battery
            ':fishing_pole_and_fish:  |  **{}, you caught: :battery:!**'.format(ctx.message.author.name), #Battery
            ':fishing_pole_and_fish:  |  **{}, you caught: :battery:!**'.format(ctx.message.author.name), #Battery
            ':fishing_pole_and_fish:  |  **{}, you caught: :battery:!**'.format(ctx.message.author.name), #Battery
            ':fishing_pole_and_fish:  |  **{}, you caught: :battery:!**'.format(ctx.message.author.name), #Battery
            ':fishing_pole_and_fish:  |  **{}, you caught: :battery:!**'.format(ctx.message.author.name), #Battery
            ':fishing_pole_and_fish:  |  **{}, you caught: :battery:!**'.format(ctx.message.author.name), #Battery
            ':fishing_pole_and_fish:  |  **{}, you caught: :battery:!**'.format(ctx.message.author.name), #Battery
            ':fishing_pole_and_fish:  |  **{}, you caught: :battery:!**'.format(ctx.message.author.name), #Battery
            ':fishing_pole_and_fish:  |  **{}, you caught: :battery:!**'.format(ctx.message.author.name), #Battery
            ':fishing_pole_and_fish:  |  **{}, you caught: :battery:!**'.format(ctx.message.author.name), #Battery
            ':fishing_pole_and_fish:  |  **{}, you caught: :battery:!**'.format(ctx.message.author.name), #Battery
            ':fishing_pole_and_fish:  |  **{}, you caught: :battery:!**'.format(ctx.message.author.name), #Battery
            ':fishing_pole_and_fish:  |  **{}, you caught: :battery:!**'.format(ctx.message.author.name), #Battery
            ':fishing_pole_and_fish:  |  **{}, you caught: :battery:!**'.format(ctx.message.author.name), #Battery
            ':fishing_pole_and_fish:  |  **{}, you caught: :battery:!**'.format(ctx.message.author.name), #Battery
            ':fishing_pole_and_fish:  |  **{}, you caught: :battery:!**'.format(ctx.message.author.name), #Battery
            ':fishing_pole_and_fish:  |  **{}, you caught: :battery:!**'.format(ctx.message.author.name), #Battery
            ':fishing_pole_and_fish:  |  **{}, you caught: :battery:!**'.format(ctx.message.author.name), #Battery
            ':fishing_pole_and_fish:  |  **{}, you caught: :battery:!**'.format(ctx.message.author.name), #Battery
            ':fishing_pole_and_fish:  |  **{}, you caught: :battery:!**'.format(ctx.message.author.name), #Battery
            ':fishing_pole_and_fish:  |  **{}, you caught: :battery:!**'.format(ctx.message.author.name), #Battery
            ':fishing_pole_and_fish:  |  **{}, you caught: :battery:!**'.format(ctx.message.author.name), #Battery
            ':fishing_pole_and_fish:  |  **{}, you caught: :battery:!**'.format(ctx.message.author.name), #Battery
            ':fishing_pole_and_fish:  |  **{}, you caught: :battery:!**'.format(ctx.message.author.name), #Battery
            ':fishing_pole_and_fish:  |  **{}, you caught: :battery:!**'.format(ctx.message.author.name), #Battery
            ':fishing_pole_and_fish:  |  **{}, you caught: :battery:!**'.format(ctx.message.author.name), #Battery
            ':fishing_pole_and_fish:  |  **{}, you caught: :battery:!**'.format(ctx.message.author.name), #Battery
            ':fishing_pole_and_fish:  |  **{}, you caught: :battery:!**'.format(ctx.message.author.name), #Battery
            ':fishing_pole_and_fish:  |  **{}, you caught: :battery:!**'.format(ctx.message.author.name), #Battery
            ':fishing_pole_and_fish:  |  **{}, you caught: :battery:!**'.format(ctx.message.author.name), #Battery
            ':fishing_pole_and_fish:  |  **{}, you caught: :battery:!**'.format(ctx.message.author.name), #Battery
            ':fishing_pole_and_fish:  |  **{}, you caught: :battery:!**'.format(ctx.message.author.name), #Battery
            ':fishing_pole_and_fish:  |  **{}, you caught: :battery:!**'.format(ctx.message.author.name), #Battery
            ':fishing_pole_and_fish:  |  **{}, you caught: :battery:!**'.format(ctx.message.author.name), #Battery
            ':fishing_pole_and_fish:  |  **{}, you caught: :battery:!**'.format(ctx.message.author.name), #Battery
            ':fishing_pole_and_fish:  |  **{}, you caught: :battery:!**'.format(ctx.message.author.name), #Battery
            ':fishing_pole_and_fish:  |  **{}, you caught: :battery:!**'.format(ctx.message.author.name), #Battery
            ':fishing_pole_and_fish:  |  **{}, you caught: :battery:!**'.format(ctx.message.author.name), #Battery
            ':fishing_pole_and_fish:  |  **{}, you caught: :battery:!**'.format(ctx.message.author.name), #Battery
            ':fishing_pole_and_fish:  |  **{}, you caught: :battery:!**'.format(ctx.message.author.name), #Battery
            ':fishing_pole_and_fish:  |  **{}, you caught: :battery:!**'.format(ctx.message.author.name), #Battery
            ':fishing_pole_and_fish:  |  **{}, you caught: :battery:!**'.format(ctx.message.author.name), #Battery
            ':fishing_pole_and_fish:  |  **{}, you caught: :battery:!**'.format(ctx.message.author.name), #Battery
            ':fishing_pole_and_fish:  |  **{}, you caught: :battery:!**'.format(ctx.message.author.name), #Battery
            ':fishing_pole_and_fish:  |  **{}, you caught: :battery:!**'.format(ctx.message.author.name), #Battery
            ':fishing_pole_and_fish:  |  **{}, you caught: :battery:!**'.format(ctx.message.author.name), #Battery
            ':fishing_pole_and_fish:  |  **{}, you caught: :battery:!**'.format(ctx.message.author.name), #Battery
            ':fishing_pole_and_fish:  |  **{}, you caught: :battery:!**'.format(ctx.message.author.name), #Battery
            ':fishing_pole_and_fish:  |  **{}, you caught: :battery:!**'.format(ctx.message.author.name), #Battery
            ':fishing_pole_and_fish:  |  **{}, you caught: :battery:!**'.format(ctx.message.author.name), #Battery
            ':fishing_pole_and_fish:  |  **{}, you caught: :battery:!**'.format(ctx.message.author.name), #Battery
            ':fishing_pole_and_fish:  |  **{}, you caught: :battery:!**'.format(ctx.message.author.name), #Battery
            ':fishing_pole_and_fish:  |  **{}, you caught: :battery:!**'.format(ctx.message.author.name), #Battery
            ':fishing_pole_and_fish:  |  **{}, you caught: :battery:!**'.format(ctx.message.author.name), #Battery
            ':fishing_pole_and_fish:  |  **{}, you caught: :battery:!**'.format(ctx.message.author.name), #Battery
            ':fishing_pole_and_fish:  |  **{}, you caught: :battery:!**'.format(ctx.message.author.name), #Battery
            ':fishing_pole_and_fish:  |  **{}, you caught: :battery:!**'.format(ctx.message.author.name), #Battery
            ':fishing_pole_and_fish:  |  **{}, you caught: :battery:!**'.format(ctx.message.author.name), #Battery
            ':fishing_pole_and_fish:  |  **{}, you caught: :battery:!**'.format(ctx.message.author.name), #Battery
            ':fishing_pole_and_fish:  |  **{}, you caught: :battery:!**'.format(ctx.message.author.name), #Battery
            ':fishing_pole_and_fish:  |  **{}, you caught: :battery:!**'.format(ctx.message.author.name), #Battery
            ':fishing_pole_and_fish:  |  **{}, you caught: :battery:!**'.format(ctx.message.author.name), #Battery
            ':fishing_pole_and_fish:  |  **{}, you caught: :battery:!**'.format(ctx.message.author.name), #Battery
            ':fishing_pole_and_fish:  |  **{}, you caught: :battery:!**'.format(ctx.message.author.name), #Battery
            ':fishing_pole_and_fish:  |  **{}, you caught: :battery:!**'.format(ctx.message.author.name), #Battery
            ':fishing_pole_and_fish:  |  **{}, you caught: :fish:!**'.format(ctx.message.author.name), #Blue fish
            ':fishing_pole_and_fish:  |  **{}, you caught: :fish:!**'.format(ctx.message.author.name), #Blue fish
            ':fishing_pole_and_fish:  |  **{}, you caught: :fish:!**'.format(ctx.message.author.name), #Blue fish
            ':fishing_pole_and_fish:  |  **{}, you caught: :fish:!**'.format(ctx.message.author.name), #Blue fish
            ':fishing_pole_and_fish:  |  **{}, you caught: :fish:!**'.format(ctx.message.author.name), #Blue fish
            ':fishing_pole_and_fish:  |  **{}, you caught: :fish:!**'.format(ctx.message.author.name), #Blue fish
            ':fishing_pole_and_fish:  |  **{}, you caught: :fish:!**'.format(ctx.message.author.name), #Blue fish
            ':fishing_pole_and_fish:  |  **{}, you caught: :fish:!**'.format(ctx.message.author.name), #Blue fish
            ':fishing_pole_and_fish:  |  **{}, you caught: :fish:!**'.format(ctx.message.author.name), #Blue fish
            ':fishing_pole_and_fish:  |  **{}, you caught: :fish:!**'.format(ctx.message.author.name), #Blue fish
            ':fishing_pole_and_fish:  |  **{}, you caught: :fish:!**'.format(ctx.message.author.name), #Blue fish
            ':fishing_pole_and_fish:  |  **{}, you caught: :fish:!**'.format(ctx.message.author.name), #Blue fish
            ':fishing_pole_and_fish:  |  **{}, you caught: :fish:!**'.format(ctx.message.author.name), #Blue fish
            ':fishing_pole_and_fish:  |  **{}, you caught: :fish:!**'.format(ctx.message.author.name), #Blue fish
            ':fishing_pole_and_fish:  |  **{}, you caught: :fish:!**'.format(ctx.message.author.name), #Blue fish
            ':fishing_pole_and_fish:  |  **{}, you caught: :fish:!**'.format(ctx.message.author.name), #Blue fish
            ':fishing_pole_and_fish:  |  **{}, you caught: :fish:!**'.format(ctx.message.author.name), #Blue fish
            ':fishing_pole_and_fish:  |  **{}, you caught: :fish:!**'.format(ctx.message.author.name), #Blue fish
            ':fishing_pole_and_fish:  |  **{}, you caught: :fish:!**'.format(ctx.message.author.name), #Blue fish
            ':fishing_pole_and_fish:  |  **{}, you caught: :fish:!**'.format(ctx.message.author.name), #Blue fish
            ':fishing_pole_and_fish:  |  **{}, you caught: :fish:!**'.format(ctx.message.author.name), #Blue fish
            ':fishing_pole_and_fish:  |  **{}, you caught: :fish:!**'.format(ctx.message.author.name), #Blue fish
            ':fishing_pole_and_fish:  |  **{}, you caught: :fish:!**'.format(ctx.message.author.name), #Blue fish
            ':fishing_pole_and_fish:  |  **{}, you caught: :fish:!**'.format(ctx.message.author.name), #Blue fish
            ':fishing_pole_and_fish:  |  **{}, you caught: :fish:!**'.format(ctx.message.author.name), #Blue fish
            ':fishing_pole_and_fish:  |  **{}, you caught: :fish:!**'.format(ctx.message.author.name), #Blue fish
            ':fishing_pole_and_fish:  |  **{}, you caught: :fish:!**'.format(ctx.message.author.name), #Blue fish
            ':fishing_pole_and_fish:  |  **{}, you caught: :fish:!**'.format(ctx.message.author.name), #Blue fish
            ':fishing_pole_and_fish:  |  **{}, you caught: :fish:!**'.format(ctx.message.author.name), #Blue fish
            ':fishing_pole_and_fish:  |  **{}, you caught: :fish:!**'.format(ctx.message.author.name), #Blue fish
            ':fishing_pole_and_fish:  |  **{}, you caught: :fish:!**'.format(ctx.message.author.name), #Blue fish
            ':fishing_pole_and_fish:  |  **{}, you caught: :fish:!**'.format(ctx.message.author.name), #Blue fish
            ':fishing_pole_and_fish:  |  **{}, you caught: :fish:!**'.format(ctx.message.author.name), #Blue fish
            ':fishing_pole_and_fish:  |  **{}, you caught: :fish:!**'.format(ctx.message.author.name), #Blue fish
            ':fishing_pole_and_fish:  |  **{}, you caught: :fish:!**'.format(ctx.message.author.name), #Blue fish
            ':fishing_pole_and_fish:  |  **{}, you caught: :fish:!**'.format(ctx.message.author.name), #Blue fish
            ':fishing_pole_and_fish:  |  **{}, you caught: :fish:!**'.format(ctx.message.author.name), #Blue fish
            ':fishing_pole_and_fish:  |  **{}, you caught: :fish:!**'.format(ctx.message.author.name), #Blue fish
            ':fishing_pole_and_fish:  |  **{}, you caught: :fish:!**'.format(ctx.message.author.name), #Blue fish
            ':fishing_pole_and_fish:  |  **{}, you caught: :fish:!**'.format(ctx.message.author.name), #Blue fish
            ':fishing_pole_and_fish:  |  **{}, you caught: :fish:!**'.format(ctx.message.author.name), #Blue fish
            ':fishing_pole_and_fish:  |  **{}, you caught: :fish:!**'.format(ctx.message.author.name), #Blue fish
            ':fishing_pole_and_fish:  |  **{}, you caught: :fish:!**'.format(ctx.message.author.name), #Blue fish
            ':fishing_pole_and_fish:  |  **{}, you caught: :fish:!**'.format(ctx.message.author.name), #Blue fish
            ':fishing_pole_and_fish:  |  **{}, you caught: :fish:!**'.format(ctx.message.author.name), #Blue fish
            ':fishing_pole_and_fish:  |  **{}, you caught: :fish:!**'.format(ctx.message.author.name), #Blue fish
            ':fishing_pole_and_fish:  |  **{}, you caught: :fish:!**'.format(ctx.message.author.name), #Blue fish
            ':fishing_pole_and_fish:  |  **{}, you caught: :fish:!**'.format(ctx.message.author.name), #Blue fish
            ':fishing_pole_and_fish:  |  **{}, you caught: :fish:!**'.format(ctx.message.author.name), #Blue fish
            ':fishing_pole_and_fish:  |  **{}, you caught: :fish:!**'.format(ctx.message.author.name), #Blue fish
            ':fishing_pole_and_fish:  |  **{}, you caught: :fish:!**'.format(ctx.message.author.name), #Blue fish
            ':fishing_pole_and_fish:  |  **{}, you caught: :fish:!**'.format(ctx.message.author.name), #Blue fish
            ':fishing_pole_and_fish:  |  **{}, you caught: :fish:!**'.format(ctx.message.author.name), #Blue fish
            ':fishing_pole_and_fish:  |  **{}, you caught: :fish:!**'.format(ctx.message.author.name), #Blue fish
            ':fishing_pole_and_fish:  |  **{}, you caught: :fish:!**'.format(ctx.message.author.name), #Blue fish
            ':fishing_pole_and_fish:  |  **{}, you caught: :fish:!**'.format(ctx.message.author.name), #Blue fish
            ':fishing_pole_and_fish:  |  **{}, you caught: :fish:!**'.format(ctx.message.author.name), #Blue fish
            ':fishing_pole_and_fish:  |  **{}, you caught: :tropical_fish:!**'.format(ctx.message.author.name), #Yellow fish
            ':fishing_pole_and_fish:  |  **{}, you caught: :tropical_fish:!**'.format(ctx.message.author.name), #Yellow fish
            ':fishing_pole_and_fish:  |  **{}, you caught: :tropical_fish:!**'.format(ctx.message.author.name), #Yellow fish
            ':fishing_pole_and_fish:  |  **{}, you caught: :tropical_fish:!**'.format(ctx.message.author.name), #Yellow fish
            ':fishing_pole_and_fish:  |  **{}, you caught: :tropical_fish:!**'.format(ctx.message.author.name), #Yellow fish
            ':fishing_pole_and_fish:  |  **{}, you caught: :tropical_fish:!**'.format(ctx.message.author.name), #Yellow fish
            ':fishing_pole_and_fish:  |  **{}, you caught: :tropical_fish:!**'.format(ctx.message.author.name), #Yellow fish
            ':fishing_pole_and_fish:  |  **{}, you caught: :tropical_fish:!**'.format(ctx.message.author.name), #Yellow fish
            ':fishing_pole_and_fish:  |  **{}, you caught: :tropical_fish:!**'.format(ctx.message.author.name), #Yellow fish
            ':fishing_pole_and_fish:  |  **{}, you caught: :tropical_fish:!**'.format(ctx.message.author.name), #Yellow fish
            ':fishing_pole_and_fish:  |  **{}, you caught: :tropical_fish:!**'.format(ctx.message.author.name), #Yellow fish
            ':fishing_pole_and_fish:  |  **{}, you caught: :tropical_fish:!**'.format(ctx.message.author.name), #Yellow fish
            ':fishing_pole_and_fish:  |  **{}, you caught: :tropical_fish:!**'.format(ctx.message.author.name), #Yellow fish
            ':fishing_pole_and_fish:  |  **{}, you caught: :tropical_fish:!**'.format(ctx.message.author.name), #Yellow fish
            ':fishing_pole_and_fish:  |  **{}, you caught: :tropical_fish:!**'.format(ctx.message.author.name), #Yellow fish
            ':fishing_pole_and_fish:  |  **{}, you caught: :tropical_fish:!**'.format(ctx.message.author.name), #Yellow fish
            ':fishing_pole_and_fish:  |  **{}, you caught: :tropical_fish:!**'.format(ctx.message.author.name), #Yellow fish
            ':fishing_pole_and_fish:  |  **{}, you caught: :tropical_fish:!**'.format(ctx.message.author.name), #Yellow fish
            ':fishing_pole_and_fish:  |  **{}, you caught: :tropical_fish:!**'.format(ctx.message.author.name), #Yellow fish
            ':fishing_pole_and_fish:  |  **{}, you caught: :tropical_fish:!**'.format(ctx.message.author.name), #Yellow fish
            ':fishing_pole_and_fish:  |  **{}, you caught: :tropical_fish:!**'.format(ctx.message.author.name), #Yellow fish
            ':fishing_pole_and_fish:  |  **{}, you caught: :tropical_fish:!**'.format(ctx.message.author.name), #Yellow fish
            ':fishing_pole_and_fish:  |  **{}, you caught: :tropical_fish:!**'.format(ctx.message.author.name), #Yellow fish
            ':fishing_pole_and_fish:  |  **{}, you caught: :tropical_fish:!**'.format(ctx.message.author.name), #Yellow fish
            ':fishing_pole_and_fish:  |  **{}, you caught: :tropical_fish:!**'.format(ctx.message.author.name), #Yellow fish
            ':fishing_pole_and_fish:  |  **{}, you caught: :tropical_fish:!**'.format(ctx.message.author.name), #Yellow fish
            ':fishing_pole_and_fish:  |  **{}, you caught: :tropical_fish:!**'.format(ctx.message.author.name), #Yellow fish
            ':fishing_pole_and_fish:  |  **{}, you caught: :tropical_fish:!**'.format(ctx.message.author.name), #Yellow fish
            ':fishing_pole_and_fish:  |  **{}, you caught: :tropical_fish:!**'.format(ctx.message.author.name), #Yellow fish
            ':fishing_pole_and_fish:  |  **{}, you caught: :tropical_fish:!**'.format(ctx.message.author.name), #Yellow fish
            ':fishing_pole_and_fish:  |  **{}, you caught: :tropical_fish:!**'.format(ctx.message.author.name), #Yellow fish
            ':fishing_pole_and_fish:  |  **{}, you caught: :tropical_fish:!**'.format(ctx.message.author.name), #Yellow fish
            ':fishing_pole_and_fish:  |  **{}, you caught: :tropical_fish:!**'.format(ctx.message.author.name), #Yellow fish
            ':fishing_pole_and_fish:  |  **{}, you caught: :tropical_fish:!**'.format(ctx.message.author.name), #Yellow fish
            ':fishing_pole_and_fish:  |  **{}, you caught: :tropical_fish:!**'.format(ctx.message.author.name), #Yellow fish
            ':fishing_pole_and_fish:  |  **{}, you caught: :tropical_fish:!**'.format(ctx.message.author.name), #Yellow fish
            ':fishing_pole_and_fish:  |  **{}, you caught: :tropical_fish:!**'.format(ctx.message.author.name), #Yellow fish
            ':fishing_pole_and_fish:  |  **{}, you caught: :tropical_fish:!**'.format(ctx.message.author.name), #Yellow fish
            ':fishing_pole_and_fish:  |  **{}, you caught: :tropical_fish:!**'.format(ctx.message.author.name), #Yellow fish
            ':fishing_pole_and_fish:  |  **{}, you caught: :tropical_fish:!**'.format(ctx.message.author.name), #Yellow fish
            ':fishing_pole_and_fish:  |  **{}, you caught: :tropical_fish:!**'.format(ctx.message.author.name), #Yellow fish
            ':fishing_pole_and_fish:  |  **{}, you caught: :tropical_fish:!**'.format(ctx.message.author.name), #Yellow fish
            ':fishing_pole_and_fish:  |  **{}, you caught: :whale:!**'.format(ctx.message.author.name), #Whale
            ':fishing_pole_and_fish:  |  **{}, you caught: :whale:!**'.format(ctx.message.author.name), #Whale
            ':fishing_pole_and_fish:  |  **{}, you caught: :whale:!**'.format(ctx.message.author.name), #Whale
            ':fishing_pole_and_fish:  |  **{}, you caught: :whale:!**'.format(ctx.message.author.name), #Whale
            ':fishing_pole_and_fish:  |  **{}, you caught: :penguin:!**'.format(ctx.message.author.name), #Penguin
            ':fishing_pole_and_fish:  |  **{}, you caught: :penguin:!**'.format(ctx.message.author.name), #Penguin
            ':fishing_pole_and_fish:  |  **{}, you caught: :penguin:!**'.format(ctx.message.author.name), #Penguin
            ':fishing_pole_and_fish:  |  **{}, you caught: :crown:!**'.format(ctx.message.author.name), #Crown
            ':fishing_pole_and_fish:  |  **{}, you caught: :crown:!**'.format(ctx.message.author.name), #Crown
            ':fishing_pole_and_fish:  |  **{}, you caught: :gem:!**'.format(ctx.message.author.name), #Gem
        ]
        fish = (random.choice(possible_responses))
        embed=discord.Embed(title="{}".format(fish), color=0xffffff, timestamp=datetime.utcnow())
        embed.set_author(name="Fishy", icon_url="https://media.giphy.com/media/Y4sT5ESJWdPGtTKqNd/giphy.gif")
        embed.set_thumbnail(url='https://media.giphy.com/media/Y4sT5ESJWdPGtTKqNd/giphy.gif')
        embed.set_footer(text='+fish', icon_url=spin_logo)
        await self.bot.say(embed=embed)

    @fish.error
    async def fish_error(self, error, ctx):
        print ("| {0} has used the fish command on cooldown in {1}".format(ctx.message.author.name, ctx.message.server.name))
        print('|-----------------------------------------------------------------------------')

        user = discord.Member
        embed=discord.Embed(title="", color=0xbfea15, timestamp=datetime.utcnow())
        embed.set_author(name='Cooldown: +fish', icon_url=spin_logo)
        embed.add_field(name="Server", value="{}".format(ctx.message.server.name))
        embed.add_field(name="Channel", value="{}".format(ctx.message.channel.mention))
        embed.add_field(name="User", value="{}".format(ctx.message.author.mention))
        embed.set_thumbnail(url='https://media.giphy.com/media/Y4sT5ESJWdPGtTKqNd/giphy.gif')
        embed.set_footer(text="ID: {}".format(ctx.message.id))
        await self.bot.send_message(discord.Object(id='436634502392053761'), embed=embed)

        embed=discord.Embed(title="", description=f'**You are on cooldown :alarm_clock:.** Try again in {str(round(error.retry_after, 2))} seconds!\n*This message will be deleted once you can use the* `+fish` *command again.*', color=0xbfea15, timestamp=datetime.utcnow())
        embed.set_author(name="Fishy Cooldown".format(user.name))
        embed.set_thumbnail(url="https://i.imgur.com/zEbHiZs.gif")
        embed.set_footer(text='+fish', icon_url=spin_logo)
        botmessage1 = await self.bot.say(embed=embed)
        await asyncio.sleep(error.retry_after)
        await self.bot.delete_message(botmessage1)

def setup(bot):
    bot.add_cog(misccogs(bot))
