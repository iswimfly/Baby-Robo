import discord
import discord.emoji


def characterEmote(game: str, charaID: str):
    emote: discord.Emoji = discord.Emoji
    charaID = charaID.lower()
    if game == "rumble":
        if charaID == "aiai":
            emote.name = "BRAiai"
            emote.id = 1288178796373082182
        if charaID == "amy":
            emote.name = "BRAmy"
            emote.id = 1288178808087908364
        if charaID == "axel":
            emote.name = "BRAxel"
            emote.id = 1288178817239744653
        if charaID == "baby":
            emote.name = "BRGod"
            emote.id = 1288178828803575943
        if charaID == "beat":
            emote.name = "BRBeat"
            emote.id = 1288178868615643156
        if charaID == "doctor":
            emote.name = "BRDoctor"
            emote.id = 1288178878694821969
        if charaID == "dr. bad-boon":
            emote.name = "BRHihi"
            emote.id = 1288178891726389300
        if charaID == "easel":
            emote.name = "BREasel"
            emote.id = 1288178907610218517
        if charaID == "fes":
            emote.name = "BRFes"
            emote.id = 1288178920923070535
        if charaID == "gongon":
            emote.name = "BRGonGon"
            emote.id = 1288178930582421666
        if charaID == "knuckles":
            emote.name = "BRKnuckles"
            emote.id = 1288178942230007828
        if charaID == "meemee":
            emote.name = "BRimsorry"
            emote.id = 1288178955026825257
        if charaID == "palette":
            emote.name = "BRPalette"
            emote.id = 1288178966276083783
        if charaID == "sonic":
            emote.name = "BRSonic"
            emote.id = 1288178976912703552
        if charaID == "tails":
            emote.name = "BRTails"
            emote.id = 1288178991580188703
        if charaID == "tee":
            emote.name = "BRTee"
            emote.id = 1288179003881947157
        if charaID == "val":
            emote.name = "BRVal"
            emote.id = 1288179017882533908
        if charaID == "yanyan":
            emote.name = "BrYanYan"
            emote.id = 1288179030809378948
    else:
        if charaID == "aiai":
            emote.name = "BMAiai"
            emote.id = 1288178427769258025
        if charaID == "meemee":
            emote.name = "BMMeeMee"
            emote.id = 1288178687992135821
        if charaID == "baby":
            emote.name = "BMBaby"
            emote.id = 1288178448795172948
        if charaID == "baby robo":
            emote.name = "BMBabyRobo"
            emote.id = 1288178462401630309
        if charaID == "gongon":
            emote.name = "BMGonGon"
            emote.id = 1288178624083791964
        if charaID == "yanyan":
            emote.name = "BMYanYan"
            emote.id = 1288178782221373461
        if charaID == "doctor":
            emote.name = "BMDoctor"
            emote.id = 1288178572577607802
        if charaID == "jam":
            emote.name = "BMJam"
            emote.id = 1288178649052217354
        if charaID == "jet":
            emote.name = "BMJet"
            emote.id = 1288178664051183689
        if charaID == "kiryu":
            emote.name = "BMKiryu"
            emote.id = 1288178675984109649
        if charaID == "beat":
            emote.name = "BMBeat"
            emote.id = 1288178478708949034
        if charaID == "sonic":
            emote.name = "BMSonic"
            emote.id = 1288178740685443174
        if charaID == "tails":
            emote.name = "BMTails"
            emote.id = 1288178769697181696
        if charaID == "sega saturn":
            emote.name = "BMSaturn"
            emote.id = 1288178721878179880
        if charaID == "sega dreamcast":
            emote.name = "BMDreamcast"
            emote.id = 1288178590533287946
        if charaID == "sega game gear":
            emote.name = "BMGameGear"
            emote.id = 1288178609416179834
        if charaID == "hello kitty":
            emote.name = "BMGoodMorningCat"
            emote.id = 1288178634753966132
        if charaID == "morgana":
            emote.name = "BMogna"
            emote.id = 1288178707508236328
        if charaID == "suezo":
            emote.name = "BMimpeter"
            emote.id = 1288178753398374505
        if charaID == "custom":
            emote.name = "CustomCharacter"
            emote.id = 1288179067647950858
    return emote


def goalEmote(goalID: str):
    emote: discord.Emoji = discord.Emoji
    emote.id = 0
    if goalID == "blue":
        emote.name = "goalblue"
        emote.id = 1288179082655305768
    if goalID == "green":
        emote.name = "goalgreen"
        emote.id = 1288179094202093568
    if goalID == "red":
        emote.name = "goalred"
        emote.id = 1288179106579480609
    return emote
