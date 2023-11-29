# --- handleResponse.py ----------------------------------------------- #
# --------------------------------------------------------------------- #
# Date      : 29/11/2023                                                #
# Authors   : krone                                                     #
# --------------------------------------------------------------------- #


# --- Imports --------------------------------------------------------- #
# --------------------------------------------------------------------- #
import discord
import main


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


def mention(user) -> discord.Embed:
    embed = discord.Embed(colour=int(main.env['dev']['EMBED_COLOUR'], 16),
                          title='【Ｖ Ａ Ｐ Ｏ Ｒ Ｂ Ｏ Ｔ ２ ０ ２ ０】',
                          type='rich', description="Hello there!\n" +
                                                    "I'm a bot powered by raw A̸͎̦͒́̿ ̷͖̺̿̃Ḙ̶̅͌ ̸̻̬͍̐̕S̴͓̼̪͊ ̴̺̦̈́T̶͇̈̈́͝ ̵̦̊̿H̷̳̟̥̆̂̓ ̵̞̓̒E̸͔̻̭̋̔ ̶̲̻͆T̴̨̳̝͗ ̶̟̮̮̽Ị̷̜̯͋͗͠ ̷̢̛͎̭̿C̷̝͊̃ ̵̩̤̤̊̈́S̸̨͇̍.\n" +
                                                    "and pure ᑎOᔕTᗩᒪGIᗩ"
                          )
    embed.set_author(name=user.name, icon_url=user.avatar)
    embed.set_image(url=main.env['dev']['MENTION_GIF'])
    embed.set_thumbnail(url=main.env['dev']['THUMBNAIL_PICTURE'])
    return embed


# --------------------------------------------------------------------- #
# --- End of file ----------------------------------------------------- #
