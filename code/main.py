import discord 
import os
import random
from keepalive import keep_alive
import randfacts

#needed for the bot to be able to read messages and respond accordingly
intents = discord.Intents.all()
client = discord.Client(intents=intents) 




pictures = ["https://cdn.vox-cdn.com/thumbor/gzWpnF3DirZJNqcgZOqMURJVSqk=/0x0:1920x964/1200x800/filters:focal(819x200:1125x506)/cdn.vox-cdn.com/uploads/chorus_image/image/71298296/Screen_Shot_2022_08_29_at_11.15.12_AM.0.png", "https://cdn.realsport101.com/images/ncavvykf/gfinityesports/a9874eb678ac589370b9d52e15c7afb5260125c8-1920x1080.jpg?rect=1,0,1919,1080&w=700&h=394&dpr=2", "https://staticg.sportskeeda.com/editor/2022/11/1dbb9-16679386214479-1920.jpg", "https://i.pinimg.com/564x/c0/28/cc/c028cceb5961fd615165ebb0247b1154.jpg", "https://media.discordapp.net/attachments/1039276555718905906/1045261770639548446/image.png?width=708&height=578", "https://media.discordapp.net/attachments/1039276555718905906/1045261770975105044/image.png?width=505&height=578", "https://media.discordapp.net/attachments/1039276555718905906/1045261771293868092/image.png?width=736&height=578", "https://media.discordapp.net/attachments/1039276555718905906/1045261771662958662/image.png?width=889&height=578", "https://media.discordapp.net/attachments/1039276555718905906/1045261942991896586/image.png?width=717&height=578", "https://media.discordapp.net/attachments/1039276555718905906/1045261943679746118/image.png?width=1002&height=578", "https://media.discordapp.net/attachments/1039276555718905906/1045262037837692948/image.png?width=676&height=578", "https://media.discordapp.net/attachments/920289883766030367/1045281671500529674/Screenshot_246.png?width=1065&height=578", "https://i.pinimg.com/564x/1f/7f/a6/1f7fa6fcbd9b5ffe84ad477c21d8d62a.jpg", "https://cdn.discordapp.com/attachments/920289883766030367/1045295052550836225/IMG_2157.png", "https://cdn.discordapp.com/attachments/920289883766030367/1045295082212950046/IMG_2054.png"]

gifs = ["https://media.tenor.com/-7HE9tBSB_oAAAAd/kaveh-genshin-impact.gif", "https://media.tenor.com/36GnTJYQKqUAAAAS/alhaitham-genshin.gif", "https://media.tenor.com/kRG7iEWK3qcAAAAC/haitham-haitham-fawn.gif", "https://media.tenor.com/rRU8G5wQFP8AAAAC/genshin-genshin-impact.gif", "https://media.tenor.com/Vok-BwiMmBIAAAAC/al-haitham-al.gif", "https://media.tenor.com/OZE67Ip-q4sAAAAC/alhaitham-genshin-impact.gif", "https://media.tenor.com/VkE-b5hbjaMAAAAd/starzeeds-alhaitham.gif", "https://media.tenor.com/t-h1OcYv-0QAAAAC/sumeru-genshin.gif"]

@client.event 
async def on_ready():
  print("{0.user} is here.".format(client))

@client.event
async def on_message(message):
  msg = message.content
  if message.author == client.user:
    return
    #check if message from bot
  if msg.startswith("/helloal"):
    await message.channel.send("Greetings traveller.")
  if msg.startswith("/sixteenwheeler"):
    await message.channel.send("https://media.discordapp.net/attachments/981633433665175592/1043700310071328858/Screenshot_2022-11-16_at_11.37.09_PM.png?width=1223&height=158")
  if msg.startswith("/tauntal"):
    await message.channel.send("https://external-preview.redd.it/-w2oZP_3l_ahnH-hHEUlt8wE2cN1Vxcv1CNPJ7ybra8.jpg?auto=webp&s=acba17fffcb7fef01233996bebdb28018256c191")
  if msg.startswith("/pical"):
    pic = random.choice(pictures)
    await message.channel.send(pic)
  if msg.startswith("/helpal"):
    await message.channel.send("```/helloal - greetings\n/nightsal - goodnights\n/profileal - profile\n/tauntal - taunt\n/sixteenwheeler - mocha's legendary writing\n/factal - a random fact\n/pical - random picture of yours truly\n/gifal - a random gif of yours truly\n/kaveh? - thoughts on kaveh\n/promiseal - promise```")
  if msg.startswith("/kaveh?"):
    await message.channel.send("https://cdn.discordapp.com/attachments/920289883766030367/1045282955049844806/image.png")
  if msg.startswith("/profileal"):
    await message.channel.send("https://genshin-impact.fandom.com/wiki/Alhaitham#Profile")
  if msg.startswith("/nightsal"):
    await message.channel.send("Rest well, traveller.")
  if msg.startswith("/promiseal"):
    await message.channel.send("https://cdn.discordapp.com/attachments/920289883766030367/1045300040995979294/IMG_1405.jpg")
  if msg.startswith("/factal"):
    fact = randfacts.get_fact()
    await message.channel.send(fact)
  if msg.startswith("/gifal"):
    gif = random.choice(gifs)
    await message.channel.send(gif)


keep_alive() #to keep the bot running 24/7
client.run(os.getenv("TOKEN")) #your bot's token
  
