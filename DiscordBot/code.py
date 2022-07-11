import warnings
warnings.filterwarnings("ignore")

import asyncio
import nextcord
from nextcord.ext import commands
from discord.ext.commands import Bot
from config import *
import os
import discord
import random
import time
from PIL import Image
from io import BytesIO
from PIL import ImageFont
from PIL import ImageDraw
from PIL import ImageOps
import urllib.request
from io import StringIO
import requests
from datetime import *


intents = nextcord.Intents.all()
client = commands.Bot(intents=intents)

emojiBank = [
  "<:allahlaugh:865451761363714048>","<:allahlove:865451914116202546>","<:appol2:754931642920992789>","<:cuama2:966213963354366032>",
  "<:gita:865451761003266059>","<:halal:855232117222801408>","<:huaha:889959304055119962>","<:imingith:876981609901994064>","<:quran:854811024174481428>",
  "<:razormoment:885404310953918465>"]

@client.event
#METHODS
async def on_message(message):
  #await message.add_reaction('<:apple:996155436724125877>')
  time = datetime.now()
  dt_string = time.strftime("%d/%m/%Y %H:%M:%S")
  if (len(message.content) >= 0 and '13:56' in dt_string and message.author.id != 995420207348715581):
    await message.reply('It is 1:56 pm and I want to die')

  if((message.channel.name == 'redditbot') and (len(message.attachments) >= 0)):
    chan = client.get_channel(941270556035125249)
    response = requests.get(message.content)
    im = Image.open(BytesIO(response.content))
    width, height = im.size
    im = im.resize((width//8, height//8))
    im.save("food.png")
    await chan.send(file=nextcord.File('food.png'))
    await chan.send('@everyone Dinner is served!')

  if 'autist' in message.content.lower() or 'autistic' in message.content.lower():
    await message.reply('Auditor')

  if 'ezekiel' in message.content.lower():
    if message.author.id == 268129103490711552 or message.author.id == 948373812657934347:
      await message.reply('aight griggy')
      await asyncio.sleep(2)
      await message.channel.send('don’t pretend to be all high level')
    elif message.author.id == 756328976737370153:
      await message.reply('aight gayjay')
      await asyncio.sleep(2)
      await message.channel.send('don’t pretend to be all high level')

  if ('new york' in message.content.lower() or 'nyc' in message.content.lower()) and message.author.id != 995420207348715581:
    nyc_date = random.randint(1, 27)
    await message.reply('I’ll be in nyc aug ' + str(nyc_date) + '-' + str(nyc_date + 4) +' :stuck_out_tongue:')
  
  if 'thank fuck' in message.content.lower():
    await message.channel.send('Yo, Fuck!')
    time.sleep(2)
    await message.reply('Thank You!')

  if message.author.id == 656886199465672704:
    await message.channel.send('<:VenkataNarasimhaRajuvaripet:996154811063996426>')

  if 'no gita' in message.content.lower() and message.author.id != 995420207348715581:
    await message.reply('Im at gitas place. She’s letting me suck on her gulab and lick her vindaloo. A little masala is leaking out. I show her this discord server and her perception of reality imploded around her.')

  if 'hinjew' in message.content.lower():
    rand = random.randrange(0, len(emojiBank))
    await message.reply('Laughed... '+ emojiBank[rand])

  if 'gita status' in message.content.lower():
    count = 34
    today = datetime.today().strftime('%Y-%m-%d')
    year = str(today[0:4])
    month = str(today[5:7])
    day = str(today[8:10])
    print(year + ' ' + month +' ' + day)
    d0 = date(2022, 7, 11)
    d1 = date(int(year), int(month), int(day))
    delta = d1 - d0
    await message.reply('Day ' + str(delta.days + count) + ' no gita, why even live <:endlessdespair:996143285322133625>')

  if 'childrens place' in message.content.lower():
    await message.reply('https://www.zara.com/us/')

  if 'physics man?' in message.content.lower():
    await message.channel.send(file=nextcord.File('physics.png'))

  if '🇹🇷' in message.content.lower() or 'turkey' in message.content.lower() or 'turkiye' in message.content.lower():
    await message.reply(':flag_in::flag_in::flag_in::flag_in::flag_in::flag_in::flag_in::flag_in::flag_in::flag_in::flag_in::flag_in:')
    await message.reply(':flag_am::flag_am::flag_am::flag_am::flag_am::flag_am::flag_am::flag_am::flag_am::flag_am::flag_am::flag_am:')
    await message.reply(':flag_in::flag_in::flag_in::flag_in::flag_in::flag_in::flag_in::flag_in::flag_in::flag_in::flag_in::flag_in:')
    await message.reply(':flag_am::flag_am::flag_am::flag_am::flag_am::flag_am::flag_am::flag_am::flag_am::flag_am::flag_am::flag_am:')
    await message.reply(':flag_in::flag_in::flag_in::flag_in::flag_in::flag_in::flag_in::flag_in::flag_in::flag_in::flag_in::flag_in:')
    await message.reply(':flag_am::flag_am::flag_am::flag_am::flag_am::flag_am::flag_am::flag_am::flag_am::flag_am::flag_am::flag_am:')
    await message.reply(':flag_in::flag_in::flag_in::flag_in::flag_in::flag_in::flag_in::flag_in::flag_in::flag_in::flag_in::flag_in:')
    await message.reply(':flag_am::flag_am::flag_am::flag_am::flag_am::flag_am::flag_am::flag_am::flag_am::flag_am::flag_am::flag_am:')
    await message.reply(':flag_in::flag_in::flag_in::flag_in::flag_in::flag_in::flag_in::flag_in::flag_in::flag_in::flag_in::flag_in:')
    await message.reply(':flag_am::flag_am::flag_am::flag_am::flag_am::flag_am::flag_am::flag_am::flag_am::flag_am::flag_am::flag_am:')

  if '🇦🇿' in message.content.lower() or 'azerbaijan' in message.content.lower():
    await message.reply(':flag_in::flag_in::flag_in::flag_in::flag_in::flag_in::flag_in::flag_in::flag_in::flag_in::flag_in::flag_in:')
    await message.reply(':flag_am::flag_am::flag_am::flag_am::flag_am::flag_am::flag_am::flag_am::flag_am::flag_am::flag_am::flag_am:')
    await message.reply(':flag_in::flag_in::flag_in::flag_in::flag_in::flag_in::flag_in::flag_in::flag_in::flag_in::flag_in::flag_in:')
    await message.reply(':flag_am::flag_am::flag_am::flag_am::flag_am::flag_am::flag_am::flag_am::flag_am::flag_am::flag_am::flag_am:')
    await message.reply(':flag_in::flag_in::flag_in::flag_in::flag_in::flag_in::flag_in::flag_in::flag_in::flag_in::flag_in::flag_in:')
    await message.reply(':flag_am::flag_am::flag_am::flag_am::flag_am::flag_am::flag_am::flag_am::flag_am::flag_am::flag_am::flag_am:')
    await message.reply(':flag_in::flag_in::flag_in::flag_in::flag_in::flag_in::flag_in::flag_in::flag_in::flag_in::flag_in::flag_in:')
    await message.reply(':flag_am::flag_am::flag_am::flag_am::flag_am::flag_am::flag_am::flag_am::flag_am::flag_am::flag_am::flag_am:')
    await message.reply(':flag_in::flag_in::flag_in::flag_in::flag_in::flag_in::flag_in::flag_in::flag_in::flag_in::flag_in::flag_in:')
    await message.reply(':flag_am::flag_am::flag_am::flag_am::flag_am::flag_am::flag_am::flag_am::flag_am::flag_am::flag_am::flag_am:')

  if '🇵🇰' in message.content.lower() or 'pakistan' in message.content.lower() or 'pakistani' in message.content.lower():
    await message.reply(':flag_in::flag_in::flag_in::flag_in::flag_in::flag_in::flag_in::flag_in::flag_in::flag_in::flag_in::flag_in:')
    await message.reply(':flag_am::flag_am::flag_am::flag_am::flag_am::flag_am::flag_am::flag_am::flag_am::flag_am::flag_am::flag_am:')
    await message.reply(':flag_in::flag_in::flag_in::flag_in::flag_in::flag_in::flag_in::flag_in::flag_in::flag_in::flag_in::flag_in:')
    await message.reply(':flag_am::flag_am::flag_am::flag_am::flag_am::flag_am::flag_am::flag_am::flag_am::flag_am::flag_am::flag_am:')
    await message.reply(':flag_in::flag_in::flag_in::flag_in::flag_in::flag_in::flag_in::flag_in::flag_in::flag_in::flag_in::flag_in:')
    await message.reply(':flag_am::flag_am::flag_am::flag_am::flag_am::flag_am::flag_am::flag_am::flag_am::flag_am::flag_am::flag_am:')
    await message.reply(':flag_in::flag_in::flag_in::flag_in::flag_in::flag_in::flag_in::flag_in::flag_in::flag_in::flag_in::flag_in:')
    await message.reply(':flag_am::flag_am::flag_am::flag_am::flag_am::flag_am::flag_am::flag_am::flag_am::flag_am::flag_am::flag_am:')
    await message.reply(':flag_in::flag_in::flag_in::flag_in::flag_in::flag_in::flag_in::flag_in::flag_in::flag_in::flag_in::flag_in:')
    await message.reply(':flag_am::flag_am::flag_am::flag_am::flag_am::flag_am::flag_am::flag_am::flag_am::flag_am::flag_am::flag_am:')

  if message.author == client.user:
    return
  
  if (message.content.lower()[-3:] == 'png' or message.content.lower()[-3:] == 'jpg'):
    with Image.open('foot.png') as foot:
        response = requests.get(message.content)
        im = Image.open(BytesIO(response.content))
        width, height = im.size
        foot = foot.resize((width // 3, (height // 3)))
        foot_width, foot_height = foot.size
        im.paste(foot, (0, height - foot_height), foot)
        im.save("profile.png")
        await message.channel.send(file=nextcord.File('profile.png'))

  if 'stephanie zheng' in message.content.lower():
    await message.channel.send(message.author.mention + ', you know what you did.')
    await asyncio.sleep(2)
    await message.channel.send("aight im out for a bit")
    await asyncio.sleep(2)
    await client.change_presence(status=discord.Status.invisible)
    await asyncio.sleep(30)
    await client.change_presence(status=discord.Status.online)
    try:
        await message.author.send("IM GONNA FUCKING KILL YOU")
    except:
        print("Error: Cannot send message to user because their DMs are off.")
    #await client.close()
    return


  if message.content.lower()[0:3] == "why":
    await message.reply('Checking...')

  if message.content.lower()[0:3] == "how":
    await message.reply('Checking...')

  if message.content.lower()[0:3] == "who":
    await message.reply('Checking...')

  if message.content.lower()[0:4] == "what":
    await message.reply('Checking...')

  if message.content.lower()[0:4] == "when":
    await message.reply('Checking...')

  if message.content.lower()[0:5] == "where":
    await message.reply('Checking...')
    
  if message.content.lower()[0:4] == "fuck":
    await message.reply('Fucking...')

  if message.content.lower()[0:3] == "kys":
    await message.reply('Killing...')

  if((message.content.lower()[0:5] == "don't" or message.content.lower()[0:4] == "dont")):
    ind1 = message.content.find(" ")
    ind2 = message.content[6:].find(" ") + 6
    if(ind2 == 5):
      await message.reply("Un" + message.content[ind1 + 1:] + "ing...")
    else:
      await message.reply("Un" + message.content[ind1 + 1 :ind2] + "ing...")

@client.event
async def on_ready():
  print('Bot is now working!')
  await client.change_presence(activity=nextcord.Game(name='League of Legends'))

client.run(token)

