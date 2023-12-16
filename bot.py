from hata import Client, Guild, ActivityType, Activity, wait_for_interruption
from hata.ext.slash import setup_ext_slash

import os
import random
import time
import cat_api
import fox_api


# Replace 'YOUR_TOKEN' with your actual bot token
TOKEN = MyCoolToken


global allowed_users

allowed_users = ["484365255502200853"]

global statussel
statussel = True

global onlypfp
onlypfp = False
# Create a bot instance

MY_GUILD = Guild.precreate(1116116269406621769)

bot = Client(TOKEN)

slash = setup_ext_slash(bot, use_default_exception_handler = False)

@bot.events
async def ready(client):
    print(f'{client:f} logged in.')



@bot.interactions(is_global = True)
async def help(client,event):
  
  text = """
Bun bot by ```@julimiro```
"/help" summons this help menu
"/bun" summons bun
"/gif" summons a gif used by bun
"/quote" sends a bun quote
"/statistics" sends some statistics
"/speechbubble" sends a speech buble gif

Admin tools (needs to have perms):
"/disablestatus" disable's bot's status message
"/status" changes between two preprogrammed statuses"""
  return text


    
    
@bot.interactions(is_global = True)
async def disablestatus(client,event):
  
  if str(event.user.id) in allowed_users:
    await bot.change_presence(activity=None)
    return "Status disabled!"
  else:
    return f"Sorry {str(client.message.author)}! You do not have permissions to do that."


@bot.interactions(is_global = True)
async def status(client,event,statustype: ("number")):

  print(type(statustype))
  if str(event.user.id) in allowed_users:
      print(statustype)
      arg = int(statustype)
      arg -= 1
      print(arg)
      if int(arg) == 0:
        await bot.edit_presence(activity = Activity("shit music", activity_type = 2))
        return "Changed status"
      elif int(arg) == 2:
        await bot.edit_presence(activity = Activity("Changed", activity_type = 0))
        return "Status changed."
      elif int(arg) == 1:
        await bot.edit_presence(activity = Activity("furry porn", activity_type = 1))
        return "A new status :yo:"
      elif int(arg) == 3:
        await bot.edit_presence(activity = Activity("How to be a furry", activity_type = 1))
        return "New status"
      elif int(arg) == 4:
        await bot.edit_presence(activity = Activity("How to act like a femboy", activity_type = 1))
        return "Statues 5 :3"
      else:
        return "Sorry! That doesn't exist..."


@bot.interactions(is_global = True)
async def bun(client,event):
    
    # Replace 'YOUR_LINK' with the link you want to send
    import links
    if onlypfp:
      link = links.pfp
    else:
      links_list = links.links
      print(links_list)
      random_num = random.randint(1,len(links_list))-1
      print(random_num)
      link = links_list[random_num]
    print(link)
    
    if os.path.isfile("buns"):
      with open("buns") as f:
        quotes = f.read()
    else:
      quotes = 0
    with open("buns","w") as f:
        f.write(str(int(quotes)+1))
    return link


@bot.interactions(is_global = True)
async def gif(client,event):
      
    # Replace 'YOUR_LINK' with the link you want to send
      import links
      links_list = links.gifs
      print(links_list)
      random_num = random.randint(1,len(links_list))-1
      print(random_num)
      link = links_list[random_num]
      print(link)
      
      if os.path.isfile("gifs"):
        with open("gifs") as f:
          quotes = f.read()
      else:
        quotes = 0
      with open("gifs","w") as f:
        f.write(str(int(quotes)+1))
      return link


@bot.interactions(is_global = True)
async def quote(client,event):
      
    # Replace 'YOUR_LINK' with the link you want to send
      import links
      links_list = links.quotes
      print(links_list)
      random_num = random.randint(1,len(links_list))-1
      print(random_num)
      link = links_list[random_num]
      print(link)
      
      if os.path.isfile("quotes"):
        with open("quotes") as f:
          quotes = f.read()
      else:
        quotes = 0
      with open("quotes","w") as f:
        f.write(str(int(quotes)+1))
      return link


@bot.interactions(is_global = True)
async def speechbubble(client,event):
      
    # Replace 'YOUR_LINK' with the link you want to send
      import links
      links_list = links.bubles
      print(links_list)
      random_num = random.randint(1,len(links_list))-1
      print(random_num)
      link = links_list[random_num]
      print(link)
      
      if os.path.isfile("bubles"):
        with open("bubles") as f:
          quotes = f.read()
      else:
        quotes = 0
      with open("bubles","w") as f:
        f.write(str(int(quotes)+1))
      return link

@bot.interactions(is_global = True)
async def statistics(client,event):
  if os.path.isfile("gifs"):
    with open("gifs") as f:
      gifs = f.read()
  else:
    gifs = "0"
  if os.path.isfile("quotes"):
    with open("quotes") as f:
      quotes =  f.read()
  else:
    quotes = "0"
  if os.path.isfile("buns"):
    with open("buns") as f:
      buns = f.read()
  else:
    buns = "0"
  
  if os.path.isfile("bubles"):
    with open("bubles") as f:
      bubles = f.read()
  else:
    bubles = "0"

  text = f"""# Cool statistics 😎

## buns : {buns}

## gifs : {gifs}

## quotes : {quotes}

## bubbles : {bubles}
"""
  return text
  

@bot.interactions(is_global = True)
async def update(client,event):
  
  update_txt ="""# Updates again...
yea! bun bot was updated again! Here's a list of changes :
- removed "/cat"

for info about previous updates visit <https://github.com/Juliasmatius/Changelogs/blob/main/bunbot.md>
Version 0.7c
Last update : 15.12.2023
"""
  return update_txt


# Run the bot

bot.start()
