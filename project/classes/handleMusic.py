# --- handleMusic.py ------------------------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #
# Date          : 07/12/2023                                                                                           #
# Last edit     : 10/11/2024                                                                                           #
# Author(s)     : krone                                                                                                #
# Description   : class to manage YouTube reproduction on Discord's voice channels                                     #
# -------------------------------------------------------------------------------------------------------------------- #


# --- Imports -------------------------------------------------------------------------------------------------------- #
# Discord API wrapper ------------------------------------------------------------------------------------------------ #
import discord
from discord.ext import commands
# YouTube libraries -------------------------------------------------------------------------------------------------- #
from yt_dlp import YoutubeDL
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
        data = await loop.run_in_executor(None,
                                          lambda: ytdl.extract_info(url=url,
                                                                    download=False,
                                                                    force_generic_extractor=True))
        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]
        filename = data['url'] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, **dictionaries.FFMPEG_OPTIONS), data=data)


# --- Class | HandleMusic -------------------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #
class HandleMusic(commands.Cog):
    # Variables ------------------------------------------------------------------------------------------------------ #
    is_playing = False
    is_paused = False
    vc = None
    playlist = json
    playlistIndex: int
    ytdl: YoutubeDL
    loop: asyncio.AbstractEventLoop

    # Init: pass a py json object as config -------------------------------------------------------------------------- #
    def __init__(self):
        self.is_playing = False
        self.is_paused = False
        self.vc = None
        self.ytdl = YoutubeDL(dictionaries.YTDL_OPTIONS)

    async def play_loop(self, voice_channel: discord.VoiceChannel, playlist: json, start: int) -> [any, bool]:
        self.playlistIndex = start
        self.playlist = playlist
        # try to connect to voice channel
        if self.vc is None or not self.vc.is_connected():
            self.vc = await voice_channel.connect()
            # in case we fail to connect
            if self.vc is None:
                return 'Could not connect to the voice channel', False
        self.is_playing = True
        self.loop = asyncio.get_event_loop()
        data = await self.loop.run_in_executor(None, lambda: self.ytdl.extract_info(
            self.playlist[self.playlistIndex], download=False))
        self.vc.play(discord.FFmpegPCMAudio(data['url'], **dictionaries.FFMPEG_OPTIONS),
                     after=lambda e: asyncio.run_coroutine_threadsafe(self.play_next(), self.loop))
        return data, True

    async def play_music(self, voice_channel: discord.VoiceChannel, url: str) -> [any, bool]:
        # try to connect to voice channel
        if self.vc is None or not self.vc.is_connected():
            self.vc = await voice_channel.connect()
            # in case we fail to connect
            if self.vc is None:
                return 'Could not connect to the voice channel', False
        self.is_playing = True
        self.loop = asyncio.get_event_loop()
        data = await self.loop.run_in_executor(None, lambda: self.ytdl.extract_info(url, download=False))
        song = data['url']
        self.vc.play(discord.FFmpegPCMAudio(song, **dictionaries.FFMPEG_OPTIONS), after=self.signal_stream_end)
        return data, True

    async def play(self, interaction: discord.Interaction, loop: bool,  queue: json, start: int) -> [any, bool]:
        try:
            voice_channel = interaction.user.voice.channel
        except:
            return 'You need to connect to a voice channel first', False
        if self.is_paused:
            await self.resume()
        else:
            if self.is_playing:
                await self.vc.disconnect()
            if loop:
                return await self.play_loop(voice_channel, queue, start)
            else:
                return await self.play_music(voice_channel, queue[start])

    def signal_stream_end(self, error):
        self.is_playing = False
        self.is_paused = False
        print('\n* event | stream closed')
        print(f"*   playing : {self.is_playing}")
        print(f"*   paused  : {self.is_paused}")
        coro = self.vc.disconnect()
        fut = asyncio.run_coroutine_threadsafe(coro, self.loop)
        try:
            fut.result()
        except:
            pass

    async def play_next(self):
        # increment index
        self.playlistIndex += 1
        if self.playlistIndex >= len(self.playlist):
            self.playlistIndex = 0
        # play new song
        self.loop = asyncio.get_event_loop()
        data = await self.loop.run_in_executor(None, lambda: self.ytdl.extract_info(
            self.playlist[self.playlistIndex], download=False))
        self.vc.play(discord.FFmpegPCMAudio(data['url'], **dictionaries.FFMPEG_OPTIONS),
                     after=lambda e: asyncio.run_coroutine_threadsafe(self.play_next(), self.loop))
        print('\n* event | music loop next')
        print(f"*   now playing: {self.playlistIndex}")

    async def wait_end(self):
        if self.vc is not None:
            while self.is_playing or self.is_paused:
                await asyncio.sleep(1)
            await self.disconnect()

    async def pause(self) -> [str, bool]:
        if self.is_playing:
            self.is_playing = False
            self.is_paused = True
            self.vc.pause()
            return '', True
        return "I'm not playing anything", False

    async def resume(self) -> [str, bool]:
        if self.is_paused:
            self.is_paused = False
            self.is_playing = True
            self.vc.resume()
            return '', True
        elif not self.is_playing:
            return "I'm not playing anything", False
        return "I'm already paused", False

    async def disconnect(self) -> [str, bool]:
        self.is_playing = False
        self.is_paused = False
        if self.vc is not None:
            if self.vc.is_connected():
                await self.vc.disconnect()
                self.vc = None
                return '', True
        return "I'm not in a voice channel", False

# -------------------------------------------------------------------------------------------------------------------- #
# --- End of file ---------------------------------------------------------------------------------------------------- #
