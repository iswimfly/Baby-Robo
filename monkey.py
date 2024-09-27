import discord
import gspread
import os
from dotenv import load_dotenv
from emote import characterEmote
def monkey(user:str):
  load_dotenv()
  gc = gspread.service_account(filename='resources/credentials.json')
  sheetid = os.getenv("RUMBLE_SHEET")
  sheet = gc.open_by_key(sheetid)
  worksheet = sheet.get_worksheet(2)
  monkeydata = worksheet.get_all_values()
  # Starting Row
  i = 3
  charadict = {}
  if (user == None):
    # Grab from U column, Check S for data
    while i < 22:
      if (monkeydata[i][17] != '0'):
        charadict[f'{monkeydata[i][20]}'] = int(monkeydata[i][18])
        i += 1
  else:
    while i < 22:
      charadict[f'{monkeydata[i][20]}'] = 0
      i = i + 1
    i = 3
    while i < 124:
      if (str(monkeydata[i][5]).__contains__(user)):
        charadict[f'{monkeydata[i][4]}'] = charadict[f'{monkeydata[i][4]}'] + 1
      i = i + 1
    i = 3
    while i < 124:
      if (str(monkeydata[i][14]).__contains__(user)):
        charadict[f'{monkeydata[i][13]}'] = charadict[f'{monkeydata[i][13]}'] + 1
      i = i + 1
    print(charadict)  
  sortedcharadict: dict = dict(sorted(charadict.items()))
  embed = discord.Embed(color=0x00FF00)  # Create an Embed object
  embed.title = f"IL Records by Character:"
  j = 0
  pages: list[discord.Embed] = []
  for key, value in sortedcharadict.items():
    if value != 0:
      emote = characterEmote('rumble', key)
      embed.add_field(name="", value=f"<:{emote.name}:{emote.id}> {key}: {value}")
      j = j + 1
      if j >= 5:
        j = 0
        pages.append(embed)
        embed = discord.Embed(color=0x00FF00)  # Create an Embed object
        embed.title = "IL Records by Character:"
  if len(pages) < (len(sortedcharadict.items()) / 5):
      pages.append(embed)
  return(pages)
