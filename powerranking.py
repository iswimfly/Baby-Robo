import discord
import gspread
import os
from dotenv import load_dotenv

def powerranking(game: str):
    print("Entered Power Ranking Command")
    load_dotenv()
    if game == "bbhd":
        sheetid = os.getenv("BBHD_SHEET")
        embedtitle = "Banana Blitz HD"
    if game == "mania":
        sheetid = os.getenv("MANIA_SHEET")
        embedtitle = "Banana Mania"
    if game == "rumble":
        sheetid = os.getenv("RUMBLE_SHEET")
        embedtitle = "Banana Rumble"

    gc = gspread.service_account(filename='resources/credentials.json')
    sheet = gc.open_by_key(sheetid)
    worksheet = sheet.get_worksheet(1)
    pages: list[discord.Embed] = []
    entries = []
    i = 7
    powerrankingsheet = worksheet.get_all_values()
    while i < len(powerrankingsheet):
        if powerrankingsheet[i][1] != "":
            entry = {
                "place": powerrankingsheet[i][0],
                "name": powerrankingsheet[i][1],
                "total": powerrankingsheet[i][2],
            }
            entries.append(entry)
        i = i + 1
    j = 0
    embed = discord.Embed(color=0x00FF00)  # Create an Embed object
    embed.title = f"Power Rankings for {embedtitle}:"
    for entry in entries:
        if entry["place"] == "":
            entry["place"] = place
        else:
            place = entry["place"]
        embed.add_field(
            name=f'{entry["place"]} - {entry["name"]} : {entry["total"]}',
            value="",
            inline=False,
        )
        j = j + 1
        if j >= 5:
            j = 0
            pages.append(embed)
            embed = discord.Embed(color=0x00FF00)  # Create an Embed object
            embed.title = f"Power Rankings for {embedtitle}:"
    if len(pages) < (len(entries) / 5):
        pages.append(embed)
    return pages
