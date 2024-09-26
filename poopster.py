import os
import urllib.request


def poopster(args: str):
    print("Poopster Called!")
    if args == None:
        link = f"https://poopster.anvilsp.com/api?"
    else:
        link = f"https://poopster.anvilsp.com/api?input={args.replace(' ','%20')}"
    response = urllib.request.urlopen(link).read()
    response = str(response)
    response = response.removeprefix("b'")
    response = response.removesuffix("'")
    return response
