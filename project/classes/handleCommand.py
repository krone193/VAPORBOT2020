# --- handleCommand.py ----------------------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #
# Date          : 08/12/2023                                                                                           #
# Last edit     : 11/12/2023                                                                                           #
# Author(s)     : krone                                                                                                #
# Description   : class to manage all type of bot slash commands                                                       #
# -------------------------------------------------------------------------------------------------------------------- #


# --- Imports -------------------------------------------------------------------------------------------------------- #
# Discord API wrapper ------------------------------------------------------------------------------------------------ #
import discord
from discord.ext import commands
# Python libraries --------------------------------------------------------------------------------------------------- #
import json
# Project classes ---------------------------------------------------------------------------------------------------- #
import project.classes.handleResponse as handleResponse
import project.classes.handleMusic as handleMusic
# Project functions -------------------------------------------------------------------------------------------------- #
import project.functions.utils as utils


# --- Class | OptionChoices ------------------------------------------------------------------------------------------ #
# -------------------------------------------------------------------------------------------------------------------- #
class OptionChoices:
    # Variables ------------------------------------------------------------------------------------------------------ #
    name: str
    value: str

    # Init: pass a py json object as config -------------------------------------------------------------------------- #
    def __init__(self, name: str, value: str):
        self.name = name
        self.value = value


# --- Class | CommandOptions ----------------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #
class CommandOptions:
    # Variables ------------------------------------------------------------------------------------------------------ #
    name: str
    mode: any
    desc: str
    required: bool
    choices = []

    # Init: pass a py json object as config -------------------------------------------------------------------------- #
    def __init__(self, j_opt: json):
        self.name = j_opt['name']
        self.title = j_opt['desc']
        self.mode = j_opt['type']
        self.required = True if j_opt['required'] == 'true' else False
        if 'choices' in j_opt:
            for choice in j_opt['choices']:
                self.choices.append(OptionChoices(j_opt['choices'][choice]['name'],
                                                  j_opt['choices'][choice]['value']))


# --- Class | SlashCommands ------------------------------------------------------------------------------------------ #
# -------------------------------------------------------------------------------------------------------------------- #
class SlashCommands:
    # Variables ------------------------------------------------------------------------------------------------------ #
    rand: int
    sub_rand: int
    name: str
    desc: str
    mode: str
    data: []
    success: json
    error: json
    options = []
    response_handle: handleResponse.HandleResponse

    # Init: pass a py json object as config -------------------------------------------------------------------------- #
    def __init__(self,
                 j_cmd: json,
                 response_handler: handleResponse.HandleResponse):
        self.rand = 255                 # init last generated random index
        self.sub_rand = 255             # init last generated random for secondary content
        self.name = j_cmd['name']       # init command name
        self.desc = j_cmd['desc']       # init command description
        self.mode = j_cmd['type']       # init command type
        self.data = j_cmd['data']       # init command data
        self.success = j_cmd['success'] if 'success' in j_cmd else None
        self.error = j_cmd['error'] if 'error' in j_cmd else None

        if 'options' in j_cmd:          # if present init options array
            for option in j_cmd['options']:
                self.options.append(CommandOptions(j_cmd['options'][option]))
        self.response_handle = response_handler     # assign response handler


# --- Class | EmbedCommands ------------------------------------------------------------------------------------------ #
# -------------------------------------------------------------------------------------------------------------------- #
class EmbedCommands(SlashCommands):
    def __init__(self,
                 bot: commands.Bot,
                 j_cmd: json,
                 response_handler: handleResponse.HandleResponse):
        super().__init__(j_cmd, response_handler)

        # slash commands execute response ---------------------------------------------------------------------------- #
        @bot.tree.command(name=self.name, description=self.desc)
        async def execute(interaction: discord.Interaction):
            await self.embed(interaction)

    # slash embed commands response ---------------------------------------------------------------------------------- #
    async def embed(self, interaction: discord.Interaction):
        # random index generation
        self.rand = utils.get_random_index_within_data(self.rand, self.data)
        # create the embed to send
        embed = self.response_handle.embed_command_response(interaction, self.data[self.rand])
        # send response and print log
        await interaction.response.send_message(embed=embed, ephemeral=False)
        print('\n* event | slash command')
        print('*   server  :', interaction.guild.name)
        print('*   channel :', interaction.channel.name)
        print('*   command :', self.name)
        print('*   author  :', interaction.user.name)
        print('*   data    :', self.rand + 1, '/', len(self.data))


# --- Class | MusicCommands ------------------------------------------------------------------------------------------ #
# -------------------------------------------------------------------------------------------------------------------- #
class MusicCommands(SlashCommands):
    music_handle: handleMusic.HandleMusic

    # Init: pass a py json object as config -------------------------------------------------------------------------- #
    def __init__(self,
                 bot: commands.Bot,
                 j_cmd: json,
                 response_handler: handleResponse.HandleResponse,
                 music_handler: handleMusic.HandleMusic):
        super().__init__(j_cmd, response_handler)
        self.music_handle = music_handler

        # slash commands execute response ---------------------------------------------------------------------------- #
        @bot.tree.command(name=self.name, description=self.desc)
        async def execute(interaction: discord.Interaction):
            await self.music(interaction)

    # slash music commands response ---------------------------------------------------------------------------------- #
    async def music(self, interaction: discord.Interaction):
        # switch between possible functions
        if self.name == 'pause':
            self.rand = utils.get_random_index_within_data(self.rand, self.success['data'])
            await self.music_handle.pause()
            embed = self.response_handle.embed_music_response(interaction,
                                                              self.success['desc'],
                                                              '',
                                                              self.success['data'][self.rand])
        elif self.name == 'resume':
            self.rand = utils.get_random_index_within_data(self.rand, self.success['data'])
            await self.music_handle.resume()
            embed = self.response_handle.embed_music_response(interaction,
                                                              self.success['desc'],
                                                              '',
                                                              self.success['data'][self.rand])
        else:
            self.rand = utils.get_random_index_within_data(self.rand, self.data)
            song, success = await self.music_handle.play(interaction, self.data[self.rand])
            if success == 0:
                if len(self.success['data']) > 0:
                    self.sub_rand = utils.get_random_index_within_data(self.sub_rand, self.success['data'])
                    image = self.success['data'][self.sub_rand]
                else:
                    image = song['thumbnail']
                embed = self.response_handle.embed_music_response(interaction,
                                                                  self.success['desc'] + '\n' + song['title'],
                                                                  '',
                                                                  image)
            else:
                self.sub_rand = utils.get_random_index_within_data(self.sub_rand, self.error['data'])
                embed = self.response_handle.embed_music_response(interaction,
                                                                  self.error['desc'],
                                                                  'You need to connect to a voice channel first!',
                                                                  self.error['data'][self.sub_rand])
        await interaction.response.send_message(embed=embed, ephemeral=False)
        print('\n* event | slash command')
        print('*   server  :', interaction.guild.name)
        print('*   channel :', interaction.channel.name)
        print('*   command :', self.name)
        print('*   author  :', interaction.user.name)
        print('*   data    :', self.rand + 1, '/', len(self.data))

# -------------------------------------------------------------------------------------------------------------------- #
# --- End of file ---------------------------------------------------------------------------------------------------- #
