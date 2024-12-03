import discord.emoji
from dotenv import load_dotenv
import os
import supabase
from typing import Final
from supabase import create_client, Client
import json
from emote import goalEmote, characterEmote
import discord

# gc = gspread.api_key(os.getenv('GOOGLE_CREDENTIALS'))
def ilrecord(game: str, level: str, type: str, category: str, jump: str, color: str):
    print("Entered Record Command")
    load_dotenv()
    url: Final[str] = os.getenv("SMBELITE_URL")
    key: Final[str] = os.getenv("SMBELITE_KEY")
    supabase: Client = create_client(url, key)
    found_level: str = ""
    response: str = ""
    print(f"Finding record in {game} on {level}...")
    game = game.lower()
    level = level.lower()
    if (category == 'advss'):
        superspeed = True
        category = None
    else:
        superspeed = False
        if (category == 'adv'):
            category = None
    if type != None:
        if type == "score":
            typebool = True
        else:
            typebool = False
    else:
        typebool = False
    if category != None:
        category = category.lower()
    validGame: bool
    elite_level = None
    if game.__contains__("mania") or game.__contains__("bm"):
        game = "mania"
        type = "time"
        elite_game = "bm"
        validGame = True
    elif game.__contains__("rumble") or game.__contains__("br"):
        game = "rumble"
        type = "time"
        elite_game = "br"
        color = None
        validGame = True
    elif game.__contains__("blitz") or game.__contains__("bbhd"):
        game = "bbhd"
        elite_game = "bbhd"
        color = None
        validGame = True
    else:
        validGame = False
        response = "Accepted games are Banana Rumble (br), Banana Mania (bm), or Blitz HD (bbhd) Please make sure you included the correct game name or abbreviations and try again."
    if validGame:
        with open(f"resources/{game}.json", "r") as file:
            json_data = json.load(file)
            for json_category in json_data:
                if category != None:
                    if category == json_category:
                        for level_name in json_data[json_category]:
                            if elite_level == None:
                                lower_level_name: str = level_name.lower()
                                if lower_level_name.__contains__(level):
                                    elite_level = levelName(
                                        game, lower_level_name, color, jump
                                    )
                                    response_level = level_name
                                    if category == None:
                                        category = json_category
                else:
                    for level_name in json_data[json_category]:
                        if elite_level == None:
                            lower_level_name: str = level_name.lower()
                            if lower_level_name.__contains__(level):
                                elite_level = levelName(
                                    game, lower_level_name, color, jump
                                )
                                response_level = level_name
                                if category == None:
                                    category = json_category
        
        if elite_level != None:
            if superspeed:
                elite_level = f'{elite_level}_(super_speed)'
                response_level = f'{response_level} (Super Speed)'
            print(
                f'"game":"{elite_game}","category_name":"{categoryName(game, category, jump, superspeed)}","level":"{elite_level}","is_score":{typebool}'
            )
            if elite_game == "br":
                smb_elite_data = supabase.rpc(
                    "get_chart_submissions",
                    {
                        "game": f"{elite_game}",
                        "category_name": f"{categoryName(game, category, jump, superspeed)}",
                        "level": f"{elite_level}",
                        "is_score": typebool,
                        "version_key": 14
                    },
                ).execute()
            else:
                smb_elite_data = supabase.rpc(
                    "get_chart_submissions",
                    {
                        "game": f"{elite_game}",
                        "category_name": f"{categoryName(game, category, jump, superspeed)}",
                        "level": f"{elite_level}",
                        "is_score": typebool,
                        "version_key": None
                    },
                ).execute()
                
            if smb_elite_data.data == "[]":
                color = "blue"
                smb_elite_data = supabase.rpc(
                    "get_chart_submissions",
                    {
                        "game": f"{elite_game}",
                        "category_name": f"{categoryName(game, category, jump, superspeed)}",
                        "level": f"{elite_level}_(blue)",
                        "is_score": typebool,
                        "version_key": None
                    },
                ).execute()
            if str(smb_elite_data.data).__contains__("'medal': 'platinum'"):
                for entry in smb_elite_data.data:
                    if entry["medal"] == "platinum":
                        record: float = float(entry["record"])
                        response = responseMessage(
                            game, entry, response_level, color, type
                        )
            elif str(smb_elite_data.data).__contains__("'medal': 'gold'"):
                for entry in smb_elite_data.data:
                    if entry["medal"] == "gold":
                        record: float = float(entry["record"])
                        response = responseMessage(
                            game, entry, response_level, color, type
                        )
            else:
                response = f"There is no live proof for this record. Submit one to appear here next time someone calls for {response_level}!"
        else:
            response = f"No level was found with the name {level}. Please try again and double check your parameters!"
    return response


def levelName(game: str, level: str, color: str, jump: str):
    print(level)
    if game == "bbhd":
        level = bbhdFormat(level)
    if (
        level.__contains__("smb2 casual 1")
        or level.__contains__("smb2 casual 2")
        or level.__contains__("smb2 casual 3")
        or level.__contains__("smb2 casual 4")
    ):
        level = level.replace("smb2 casual ", "world 1-")
    if level.__contains__("smb1"):
        level = level.replace("smb1 ", "")
    if level.__contains__("smb2"):
        level = level.replace("smb2 ", "")
        if level.__contains__("normal 1"):
            level = level.replace("normal 1", "world_3-")
        if level.__contains__("expert 2"):
            level = level.replace("expert 2", "world_7-")
    if level.__contains__("casual ex"):
        level = level.replace("casual ex", "casual X")
    if level.__contains__("normal ex"):
        level = level.replace("normal ex", "normal X")
    if level.__contains__("expert ex"):
        level = level.replace("expert ex", "expert X")
    if level.__contains__("master ex"):
        level = level.replace("master ex", "master X")
    if level.__contains__("dx") and game == "mania":
        level = level.replace("dx", "DX")
    if level.__contains__("-ex") and game == "rumble":
        level = level.replace("-ex", "_EX-")
    if level.__contains__("original stage mode 6 ~ chaos"):
        level = level.replace("original stage mode 6 ~ chaos", "DX_mode_39_-_chaos")
    level = level.replace(" ", "_")
    level = level.replace("~", "-")
    if jump == "jump":
        level = f"{level}_({jump})"
    if color != None:
        level = f"{level}_({color})"
    return level


def categoryName(game: str, category: str, jump: str, superspeed: bool):
    elite_category = ""
    if game != "mania":
        if (superspeed == False):
            elite_category = "main"
        else:
            elite_category = "super_speed"
    else:
        if category == "story" or category == "smb1" or category == "smb2":
            elite_category = "main"
        else:
            elite_category = "special"
        if jump == "jump":
            elite_category = f"{elite_category}_jump"
    return elite_category


def bbhdFormat(level: str):
    if level.__contains__("island"):
        level = level.replace("monkey island ", "world 1-")
    if level.__contains__("jungle"):
        level = level.replace("jumble jungle ", "world 2-")
    if level.__contains__("sherbet"):
        level = level.replace("smooth sherbet ", "world 3-")
    if level.__contains__("desert"):
        level = level.replace("detrius desert ", "world 4-")
    if level.__contains__("ocean"):
        level = level.replace("pirates' ocean ", "world 5-")
    if level.__contains__("caverns"):
        level = level.replace("cobalt caverns ", "world 6-")
    if level.__contains__("pools"):
        level = level.replace("volcanic pools ", "world 7-")
    if level.__contains__("case"):
        level = level.replace("space case ", "world 8-")
    if level.__contains__("swamp"):
        level = level.replace("sinking swamp ", "world 9-")
    if level.__contains__("heaven"):
        level = level.replace("ultra heaven ", "world 10-")
    return level


def responseMessage(game: str, entry, level: str, color: str, type: str):
    goalKind: discord.Emoji = discord.Emoji
    if color != None:
        goalKind = goalEmote(color)
        level = f"{level} <:{goalKind.name}:{goalKind.id}>"
    record = entry["record"]
    charaEmote: discord.Emoji = characterEmote(game, entry["monkey"]["monkey_name"])
    if type == "time":
        if game == "rumble":
            record = f"**{record:0.3f}** <:{charaEmote.name}:{charaEmote.id}>"
        else:
            record = f"**{record:0.2f}** <:{charaEmote.name}:{charaEmote.id}>"
    if entry["medal"] == "gold":
        record = f"TIED {record}. Proof provided"
    response: str = (
        f"World record for {level} is {record} by **{entry['profile']['username']}** {entry['proof']}"
    )
    return response
