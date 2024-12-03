import discord
import gspread
import os
from dotenv import load_dotenv
from emote import characterEmote
def monkeys(user:str):
  print('Entered Monkey Command')
  load_dotenv()
  gc = gspread.service_account(filename='resources/credentials.json')
  sheetid = os.getenv("RUMBLE_SHEET")
  sheet = gc.open_by_key(sheetid)
  worksheet = sheet.get_worksheet(2)
  monkeydata = worksheet.get_all_values()
  # Starting Row
  recordtotal = 0
  i = 3
  charadict = {}
  if (user == None):
    # Grab from P column, Check R for data
    while i < 23:
      if (monkeydata[i][17] != '0'):
        charadict[f'{monkeydata[i][17]}'] = int(monkeydata[i][15])
        i += 1
  else:
    while i < 23:
      charadict[f'{monkeydata[i][17]}'] = 0
      i = i + 1
    i = 3
    while i < 278:
      if (str(monkeydata[i][5]).__contains__(user)):
        charadict[f'{monkeydata[i][4]}'] = charadict[f'{monkeydata[i][4]}'] + 1
        recordtotal = recordtotal + 1
      if (str(monkeydata[i][5]).__contains__('Players')):
        if(worksheet.get_note(f'F{i + 1}').__contains__(user)):
          charadict[f'{monkeydata[i][4]}'] = charadict[f'{monkeydata[i][4]}'] + 1
          recordtotal = recordtotal + 1
      i = i + 1
    i = 3
    while i < 278:
      if (str(monkeydata[i][11]).__contains__(user)):
        charadict[f'{monkeydata[i][10]}'] = charadict[f'{monkeydata[i][10]}'] + 1
        recordtotal = recordtotal + 1
      if (str(monkeydata[i][11]).__contains__('Players')):
        if(worksheet.get_note(f'L{i + 1}').__contains__(user)):
          charadict[f'{monkeydata[i][10]}'] = charadict[f'{monkeydata[i][10]}'] + 1
          recordtotal = recordtotal + 1
      i = i + 1
  if recordtotal == 0 and user != None:
    return('No player was found with that name. Please try again!')
  sortedcharadict = dict(sorted(charadict.items(), key=lambda item: item[1], reverse=True))
  embed = discord.Embed(color=0x00FF00)  # Create an Embed object
  embed.title = f"Banana Rumble IL Records by Character:"
  if (user != None):
    embed.description = f"Pulling records for {user} ({recordtotal} total)..."
  j = 0
  pages: list[discord.Embed] = []
  fieldvalue = ''
  for key, value in sortedcharadict.items():
    if value != 0:
      emote = characterEmote('rumble', key)
      fieldvalue = f'{fieldvalue}<:{emote.name}:{emote.id}> {key}: {value}\n'
      j = j + 1
      if j >= 5:
        j = 0
        embed.add_field(name="", value=fieldvalue, inline=True)
        fieldvalue = ''
        pages.append(embed)
        embed = discord.Embed(color=0x00FF00)  # Create an Embed object
        embed.title = "Banana Rumble IL Records by Character:"
        if (user != None):
          embed.description = f"Pulling records for {user}..."
  if len(pages) < (len(sortedcharadict.items()) / 5):
      embed.add_field(name="", value=fieldvalue, inline=True)
      fieldvalue = ''
      pages.append(embed)
  return(pages)
