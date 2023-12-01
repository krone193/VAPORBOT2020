# --- handleResponse.py ----------------------------------------------- #
# --------------------------------------------------------------------- #
# Date      : 29/11/2023                                                #
# Authors   : krone                                                     #
# --------------------------------------------------------------------- #


# --- Imports --------------------------------------------------------- #
# --------------------------------------------------------------------- #
import discord
import math
from random import random
from main import env


# --- Variables ------------------------------------------------------- #
# --------------------------------------------------------------------- #


# --- Functions ------------------------------------------------------- #
# --------------------------------------------------------------------- #
def handle_response(message) -> str:
    p_message = message.lower()

    if p_message == 'hello':
        return 'Hello ; )'

    if p_message == 'help':
        return "you're on your own"

    return ''


def embedf(title, description, user, image, thumbnail) -> discord.Embed:
    embed = discord.Embed(colour=int(env['dev']['EMBED_COLOUR'], 16),
                          title=title,
                          type='rich', description=description
                          )
    embed.set_author(name=user.name, icon_url=user.avatar)
    embed.set_image(url=image)
    embed.set_thumbnail(url=thumbnail)
    return embed


def mention(user) -> discord.Embed:
    return embedf(title='【Ｖ Ａ Ｐ Ｏ Ｒ Ｂ Ｏ Ｔ ２ ０ ２ ０】',
                  description="Hello there!\n" +
                              "I'm a bot powered by raw A̸͎̦͒́̿ ̷͖̺̿̃Ḙ̶̅͌ ̸̻̬͍̐̕S̴͓̼̪͊ ̴̺̦̈́T̶͇̈̈́͝ ̵̦̊̿H̷̳̟̥̆̂̓ ̵̞̓̒E̸͔̻̭̋̔ ̶̲̻͆T̴̨̳̝͗ ̶̟̮̮̽Ị̷̜̯͋͗͠ ̷̢̛͎̭̿C̷̝͊̃ ̵̩̤̤̊̈́S̸̨͇̍.\n" +
                              "and pure ᑎOᔕTᗩᒪGIᗩ",
                  user=user,
                  image=env['dev']['MENTION_GIF'],
                  thumbnail=env['dev']['THUMBNAIL_PICTURE'])


# --------------------------------------------------------------------- #
def embed_command_response(interaction, data) -> discord.Embed:
    index = math.floor(random() * len(data))
    return embedf(title='',
                  description='',
                  user=interaction.user,
                  image=data[index],
                  thumbnail='')


# --------------------------------------------------------------------- #
# --- End of file ----------------------------------------------------- #
