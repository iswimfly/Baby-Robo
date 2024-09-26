from dotenv import load_dotenv
import os
import supabase
from typing import Final
from supabase import create_client, Client
from emote import characterEmote
def test():
    emote = characterEmote('mania', 'aiai')
    return(f'<:{str(emote.name)}:{emote.id}>')