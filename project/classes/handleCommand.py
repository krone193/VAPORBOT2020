# --- handleCommand.py ----------------------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #
# Date          : 08/12/2023                                                                                           #
# Last edit     : 10/12/2023                                                                                           #
# Author(s)     : krone                                                                                                #
# Description   : class to manage all type of bot slash commands                                                       #
# -------------------------------------------------------------------------------------------------------------------- #


# --- Imports -------------------------------------------------------------------------------------------------------- #
# Discord API wrapper ------------------------------------------------------------------------------------------------ #
import discord
from discord.ext import commands
# Python libraries --------------------------------------------------------------------------------------------------- #
import math
from random import random
import json
# Project classes ---------------------------------------------------------------------------------------------------- #
import project.classes.handleResponse as handleResponse


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
    name: str
    desc: str
    mode: str
    json: json
    options = []
    response_handle: handleResponse.HandleResponse

    # Init: pass a py json object as config -------------------------------------------------------------------------- #
    def __init__(self,
                 bot: commands.Bot,
                 j_cmd: json,
                 response_handler: handleResponse.HandleResponse):
        self.rand = 255                 # init last generated random index
        self.name = j_cmd['name']       # init command name
        self.desc = j_cmd['desc']       # init command description
        self.mode = j_cmd['type']       # init command type
        self.json = j_cmd               # init content
        if 'options' in j_cmd:          # if present init options array
            for option in j_cmd['options']:
                self.options.append(CommandOptions(j_cmd['options'][option]))
        self.response_handle = response_handler     # assign response handler

        # slash commands execute response ---------------------------------------------------------------------------- #
        @bot.tree.command(name=self.name, description=self.desc)
        async def execute(interaction: discord.Interaction):
            if self.mode == 'embed':
                await self.embed(interaction)
            elif self.mode == 'music':
                await self.music(interaction)
            else:
                await self.embed(interaction)

    # random data indexer update ------------------------------------------------------------------------------------- #
    def get_random_index_within_data(self, data: json) -> int:
        # random index generation
        if len(data) > 1:
            new_rand = self.rand
            while new_rand == self.rand:
                new_rand = math.floor(random() * len(data))
        else:
            new_rand = 0
        return new_rand

    # slash embed commands response ---------------------------------------------------------------------------------- #
    async def embed(self, interaction: discord.Interaction):
        # random index generation
        self.rand = self.get_random_index_within_data(self.json['data'])
        # create the embed to send
        embed = self.response_handle.embed_command_response(interaction, self.json['data'][self.rand])
        # send response and print log
        await interaction.response.send_message(embed=embed, ephemeral=False)
        print('\n* event | slash command')
        print('*   server  :', interaction.guild.name)
        print('*   channel :', interaction.channel.name)
        print('*   command :', self.name)
        print('*   author  :', interaction.user.name)
        print('*   data    :', self.rand + 1, '/', len(self.json['data']))

    # slash music commands response ---------------------------------------------------------------------------------- #
    async def music(self, interaction: discord.Interaction):
        # random index generation
        self.rand = self.get_random_index_within_data(self.json['data'])
        await interaction.response.send_message(content="Sorry, I'm still dreaming about this, but here's your link:\n"
                                                        + self.json['data'][self.rand],
                                                ephemeral=False)
        print('\n* event | slash command')
        print('*   server  :', interaction.guild.name)
        print('*   channel :', interaction.channel.name)
        print('*   command :', self.name)
        print('*   author  :', interaction.user.name)
        print('*   data    :', self.rand + 1, '/', len(self.json['data']))

# -------------------------------------------------------------------------------------------------------------------- #
# --- End of file ---------------------------------------------------------------------------------------------------- #
