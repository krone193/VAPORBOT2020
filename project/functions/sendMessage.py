# --- sendMessage.py -------------------------------------------------- #
# --------------------------------------------------------------------- #
# Date      : 29/11/2023                                                #
# Authors   : krone                                                     #
# --------------------------------------------------------------------- #
import discord


# --- Imports --------------------------------------------------------- #
# --------------------------------------------------------------------- #
# --- Variables ------------------------------------------------------- #
# --------------------------------------------------------------------- #


# --- Functions ------------------------------------------------------- #
# --------------------------------------------------------------------- #
async def send_message(message, content, embedded, private) -> bool:
    try:
        if embedded:
            await message.author.send(embed=content) if private else await message.channel.send(embed=content)
        else:
            await message.author.send(content) if private else await message.channel.send(content)

    except Exception as err:
        print(err)
        return False

    return True


# --------------------------------------------------------------------- #
# --- End of file ----------------------------------------------------- #
