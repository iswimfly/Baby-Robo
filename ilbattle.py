import os
import json
import random
import math


def il_battle(game: str, stagecount: int, args: str):
    # Setup
    stagecount = abs(stagecount)
    if stagecount == 0:
        return "Please provide a stage count above 0 and try again!"
    if game == "bbhd":
        response: str = f"Selected {stagecount} stages from BBHD:"
    else:
        response: str = f"Selected {stagecount} stages from {game}:```"
    # Convert Args into actual categories
    argslist = args.split(",")
    argslist = list(set(argslist))
    while "None" in argslist:
        argslist.remove("None")
    if argslist.__contains__("specials"):
        argslist.remove("specials")
        argslist.append("dx")
        argslist.append("og")
        argslist.append("reverse")
        argslist.append("gb")
        argslist.append("db")
    if argslist.__contains__("dxonly"):
        argslist.remove("dxonly")
        argslist.append("dx")
    # Read json and pull any stages from specified categories
    game = game.lower()
    viable_stages = []
    with open(f"resources/{game}.json", "r") as file:
        json_data = json.load(file)
    if len(argslist) > 0:
        for category in argslist:
            for option in json_data:
                if category == option:
                    for item in json_data[category]:
                        viable_stages.append(item)
    # If no categories, just pull literally every stage
    else:
        for option in json_data:
            for item in json_data[option]:
                viable_stages.append(item)
    i = 0
    while i < stagecount and len(viable_stages) > 0:
        # Dupe prevention
        selected_stage = viable_stages[random.randint(0, len(viable_stages))]
        while response.__contains__(selected_stage):
            selected_stage = viable_stages[random.randint(0, len(viable_stages))]
        response = f"{response}\n{selected_stage}"
        i = i + 1
    response = f"{response}```"
    if len(viable_stages) == 0:
        response = 'Please select a valid category or categories and try again!'
    file.close()
    return response
