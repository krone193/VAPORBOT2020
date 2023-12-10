# --- handleMusic.py ------------------------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #
# Date          : 07/12/2023                                                                                           #
# Last edit     : 10/12/2023                                                                                           #
# Author(s)     : krone                                                                                                #
# Description   : class to manage YouTube reproduction on Discord's voice channels                                     #
# -------------------------------------------------------------------------------------------------------------------- #


# --- Imports -------------------------------------------------------------------------------------------------------- #
# Discord API wrapper ------------------------------------------------------------------------------------------------ #
import discord
from discord.ext import commands
# YouTube libraries -------------------------------------------------------------------------------------------------- #
import youtube_dl
# Python libraries --------------------------------------------------------------------------------------------------- #
import asyncio
import json
# Project constants -------------------------------------------------------------------------------------------------- #
import project.constants.dictionaries as dictionaries


# --- Class | YTDLSource --------------------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #
class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)
        self.data = data
        self.title = data.get('title')
        self.url = data.get('url')

    @classmethod
    async def from_url(cls, ytdl, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))
        filename = data['url'] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, **dictionaries.FFMPEG_OPTIONS), data=data)


# --- Class | HandleMusic -------------------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #
class HandleMusic(commands.Cog):
    # Variables ------------------------------------------------------------------------------------------------------ #
    config: json
    cmd: json
    ytdl: youtube_dl.YoutubeDL

    # Init: pass a py json object as config -------------------------------------------------------------------------- #
    def __init__(self, config: json, cmd: json):
        self.config = config
        self.cmd = cmd
        self.ytdl = youtube_dl.YoutubeDL(dictionaries.YTDL_OPTIONS)

    async def play(self, ctx: discord.ext.commands.context, url: str):
        player = await YTDLSource.from_url(self.ytdl, url)
        ctx.voice_client.play(player, after=lambda e: print("player error") if e else None)
        await ctx.send(f'Now playing: {player.title}')

# -------------------------------------------------------------------------------------------------------------------- #
# --- End of file ---------------------------------------------------------------------------------------------------- #
