# --- handleResponse.py ---------------------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #
# Date          : 29/11/2023                                                                                           #
# Last edit     : 10/12/2023                                                                                           #
# Author(s)     : krone                                                                                                #
# Description   : class to populate embedded and text response on VAPORBOT2020's events                                #
# -------------------------------------------------------------------------------------------------------------------- #


# --- Imports -------------------------------------------------------------------------------------------------------- #
# Discord API wrapper ------------------------------------------------------------------------------------------------ #
import discord
import discord.ext.commands
# Python libraries --------------------------------------------------------------------------------------------------- #
import json


# --- Class | HandleResponse ----------------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #
class HandleResponse:
    # Variables ------------------------------------------------------------------------------------------------------ #
    config: json
    events: json

    # Init: pass a py json object as config -------------------------------------------------------------------------- #
    def __init__(self, config: json, events: json):
        self.config = config
        self.events = events

    # ---------------------------------------------------------------------------------------------------------------- #
    def embeds(self, title: str, description: str, user: any, image: str, thumbnail: str) -> discord.Embed:
        embed = discord.Embed(colour=int(self.config['global']['embed_colour'], 16),
                              title=title,
                              type='rich',
                              description=description)
        if user != '':
            embed.set_author(name=user.name, icon_url=user.avatar)
        if image != '':
            embed.set_image(url=image)
        if thumbnail != '':
            embed.set_thumbnail(url=thumbnail)
        return embed

    # ---------------------------------------------------------------------------------------------------------------- #
    def handle_response(self,
                        bot: discord.ext.commands.Bot,
                        ctx: discord.ext.commands.context,
                        is_mention: bool) -> any:
        if is_mention:
            return self.embeds(title=self.config['global']['mention_title'],
                               description=self.config['global']['mention_description'],
                               user=ctx.author,
                               image=self.config['global']['mention_gif'],
                               thumbnail=self.config['global']['embed_thumbnail'])
        else:
            p_message = ctx.message.content.lower()
            if p_message == 'hello':
                return "Hello, I'm " + bot.user.name + " ; )"
            return None

    # ---------------------------------------------------------------------------------------------------------------- #
    def embed_command_response(self, interaction, data) -> discord.Embed:
        return self.embeds(title='',
                           description='',
                           user=interaction.user,
                           image=data,
                           thumbnail='')

    # ---------------------------------------------------------------------------------------------------------------- #
    def embed_timed_event(self, event: json) -> discord.Embed:
        return self.embeds(title=event['title'],
                           description=event['desc'],
                           user='',
                           image=event['data'],
                           thumbnail='')

# -------------------------------------------------------------------------------------------------------------------- #
# --- End of file ---------------------------------------------------------------------------------------------------- #
