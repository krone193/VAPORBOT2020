# --- dictionaries.py ------------------------------------------------------------------------------------------------ #
# -------------------------------------------------------------------------------------------------------------------- #
# Date          : 09/12/2023                                                                                           #
# Last edit     : 16/06/2026                                                                                           #
# Author(s)     : krone                                                                                                #
# Description   : CONST list of all dictionaries and const for VAPORBOT2020                                            #
# -------------------------------------------------------------------------------------------------------------------- #


# --- Imports -------------------------------------------------------------------------------------------------------- #
# Discord API wrapper ------------------------------------------------------------------------------------------------ #
import discord


# -------------------------------------------------------------------------------------------------------------------- #
DEPLOYS = {
    'debug': 'debug',
    'release': 'release'
}
# -------------------------------------------------------------------------------------------------------------------- #
PHYS = {
    'development': 'dev',
    'production': 'raspi'
}
# -------------------------------------------------------------------------------------------------------------------- #
ACTIVITIES = {
    'LISTENING': discord.ActivityType.listening,
    'PLAYING': discord.ActivityType.playing,
    'STREAMING': discord.ActivityType.streaming,
    'COMPETING': discord.ActivityType.competing
}
# -------------------------------------------------------------------------------------------------------------------- #
YTDL_OPTIONS = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'm4a',
        'preferredquality': '192',
    }],
    'extractor_args': {
        'extract-audio': True,
        'sleep-interval': 5,
        'sleep-requests': 1,
    },
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0',  # bind to ipv4 since ipv6 addresses cause issues sometimes
    'verbose': True,
}
# -------------------------------------------------------------------------------------------------------------------- #
FFMPEG_OPTIONS = {
    'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5 -probesize 200M',
    'options': '-vn'
}

# -------------------------------------------------------------------------------------------------------------------- #
# --- End of file ---------------------------------------------------------------------------------------------------- #
