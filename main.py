#▀▀█▀▀ █▀▀█ ░▀░ ▀█░█▀ ░▀░ █▀▀█   █▀▀▄ █▀▀█ ▀▀█▀▀   █▀▀▄ █░░█   █▀▀▄ █▀▀█ █▀▀█ █░█
#░░█░░ █▄▄▀ ▀█▀ ░█▄█░ ▀█▀ █▄▄█   █▀▀▄ █░░█ ░░█░░   █▀▀▄ █▄▄█   █░░█ █▄▄█ █▄▄▀ █▀▄
#░░▀░░ ▀░▀▀ ▀▀▀ ░░▀░░ ▀▀▀ ▀░░▀   ▀▀▀░ ▀▀▀▀ ░░▀░░   ▀▀▀░ ▄▄▄█   ▀▀▀░ ▀░░▀ ▀░▀▀ ▀░▀

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

Bot = Bot(command_prefix="+")
Bot.remove_command('help')
status = ['v3.2.8 | +help', 'Chat With Other Trivia Enthusiasts', 'Bot created by dark#9999', 'trivia on Trivia Nation', 'Win Money!']

async def change_status():
    await Bot.wait_until_ready()
    msgs = cycle(status)

    while not Bot.is_closed:
        current_status = next(msgs)
        await Bot.change_presence(game=discord.Game(name=current_status, type=1))
        await asyncio.sleep(45)

#█▀▀█ █▀▀▄   █▀▀█ █▀▀ █▀▀█ █▀▀▄ █░░█
#█░░█ █░░█   █▄▄▀ █▀▀ █▄▄█ █░░█ █▄▄█
#▀▀▀▀ ▀░░▀   ▀░▀▀ ▀▀▀ ▀░░▀ ▀▀▀░ ▄▄▄█
@Bot.event
async def on_ready():
    print('/-----------------------------------------------------------------------------')
    print('| # LOADING...')
    Bot.load_extension("main-cogs")
    print('| main-cogs:             ' + 'Loaded')
    Bot.load_extension("custom-cogs")
    print('| custom-cogs:           ' + 'Loaded')
    Bot.load_extension("staff-cogs")
    print('| staff-cogs:            ' + 'Loaded')
    Bot.load_extension("misc-cogs")
    print('| misc-cogs:             ' + 'Loaded')
    Bot.load_extension("role-cogs")
    print('| role-cogs:             ' + 'Loaded')
    Bot.load_extension("ticket-cogs")
    print('| ticket-cogs:           ' + 'Loaded')
    print('|-----------------------------------------------------------------------------')
    print('| # ME')
    print('| Name:     ' + 'Trivia Bot')
    print('| ID:       ' + '452889188166139914')
    print('| Invite:   https://discord.now.sh/' + '452889188166139914' + '?p1543892215')
    print('|-----------------------------------------------------------------------------')
    print('| # SERVERS (1)')
    print('| > Name:   ' + "Trivia Central")
    print('|   Owner:  ' + "RobertoDraws#1234")
    print('\-----------------------------------------------------------------------------')

Bot.loop.create_task(change_status())
Bot.run("NDcxMDY3NDYxMjUzMzMyOTkz.DjfbYg.0LkZJAfyKhf8FD2a89w8fjo2Otw")
