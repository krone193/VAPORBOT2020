# --- handleResponse.py ---------------------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #
# Date          : 29/11/2023                                                                                           #
# Last edit     : 06/12/2023                                                                                           #
# Author(s)     : krone                                                                                                #
# Description   : class to populate embedded and text response on VAPORBOT2020's events                                #
# -------------------------------------------------------------------------------------------------------------------- #


# --- Imports -------------------------------------------------------------------------------------------------------- #
# Discord API wrapper ------------------------------------------------------------------------------------------------ #
import discord
# Python libraries --------------------------------------------------------------------------------------------------- #
import json


# --- Class | HandleResponse ----------------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #
class HandleResponse:
    # Variables ------------------------------------------------------------------------------------------------------ #
    config: json

    # Init: pass a py json object as config -------------------------------------------------------------------------- #
    def __init__(self, config: json):
        self.config = config

    # ---------------------------------------------------------------------------------------------------------------- #
    def embeds(self, title: str, description: str, user: any, image: str, thumbnail: str) -> discord.Embed:
        embed = discord.Embed(colour=int(self.config['global']['embed_colour'], 16),
                              title=title,
                              type='rich',
                              description=description
                              )
        if user != '':
            embed.set_author(name=user.name, icon_url=user.avatar)
        if image != '':
            embed.set_image(url=image)
        if thumbnail != '':
            embed.set_thumbnail(url=thumbnail)
        return embed

    # ---------------------------------------------------------------------------------------------------------------- #
    def handle_response(self, message) -> str:
        p_message = message.lower()
        if p_message == 'hello':
            return "Hello, I'm " + self.config['global']['name'] + " ; )"
        return ''

    # ---------------------------------------------------------------------------------------------------------------- #
    def mention(self, user) -> discord.Embed:
        return self.embeds(title=self.config['global']['mention_title'],
                           description=self.config['global']['mention_description'],
                           user=user,
                           image=self.config['global']['mention_gif'],
                           thumbnail=self.config['global']['embed_thumbnail'])

    # ---------------------------------------------------------------------------------------------------------------- #
    def embed_command_response(self, interaction, data) -> discord.Embed:
        return self.embeds(title='',
                           description='',
                           user=interaction.user,
                           image=data,
                           thumbnail='')

    # ---------------------------------------------------------------------------------------------------------------- #
    def embed_timed_event(self, server: str, event: str) -> discord.Embed:
        return self.embeds(title=self.config[server][event]['title'],
                           description=self.config[server][event]['desc'],
                           user='',
                           image=self.config[server][event]['data'],
                           thumbnail='')

# -------------------------------------------------------------------------------------------------------------------- #
# --- End of file ---------------------------------------------------------------------------------------------------- #
