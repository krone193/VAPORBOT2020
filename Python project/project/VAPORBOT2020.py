# --- VAPORBOT2020.py -------------------------------------------- #
# --------------------------------------------------------------------- #
# Date    :	22/11/2023                                                  #
# Authors :	krone                                                       #
# --------------------------------------------------------------------- #


# --- Imports --------------------------------------------------------- #
# --------------------------------------------------------------------- #
import discord
from discord import app_commands
from discord.ext import commands
import main
import project.functions.sendMessage as funcMessaging
import project.functions.handleResponse as funcHandling


# --- SW Versions ----------------------------------------------------- #
# --------------------------------------------------------------------- #
SW_VER = "v0.1.0.0"
# --- Changelog ------------------------------------------------------- #
# vxx.xx.xx ----------------------------------------------------------- #
#   .                                                                   #
# --------------------------------------------------------------------- #
# v00.01.00 ----------------------------------------------------------- #
#   Project start                                                       #
# --------------------------------------------------------------------- #


# --- Defines --------------------------------------------------------- #
# --------------------------------------------------------------------- #
# --- Variables ------------------------------------------------------- #
# --------------------------------------------------------------------- #
# --- Classes --------------------------------------------------------- #
# --------------------------------------------------------------------- #
def events(bot):
    @bot.event
    async def on_ready():
        print(f'{bot.user} is now running')
        try:
            sync = await bot.tree.sync()
            print(f"Sync {len(sync)} commands(s)")
        except Exception as err:
            print(err)

    @bot.tree.command(name='hello')
    async def hello(interaction: discord.Interaction):
        await interaction.response.send_message(f"Hey {interaction.user.mention}! This is a slash command!",
                                                ephemeral=False)

    @bot.event
    async def on_message(message):
        username = str(message.author)
        content = str(message.content)
        channel = str(message.channel)

        if username == bot.user:
            return

        if content == '':
            return

        if bot.user.mentioned_in(message) and message.mention_everyone is False:
            ctx = await bot.get_context(message)
            print(ctx)
            user = ctx.author
            print(user)
            response = funcHandling.mention(user)
            await funcMessaging.send_message(message, response, True, False)
            return

        if content[0] == '?':
            content = content[1:]
            private = True
            await message.delete()

        else:
            private = False

        response = funcHandling.handle_response(content)

        if response != '':
            await funcMessaging.send_message(message, response, False, private)


# --- Main ------------------------------------------------------------ #
# --------------------------------------------------------------------- #
def run(env):
    # init intents
    intents = discord.Intents.default()
    intents.message_content = True

    # create Discord Client
    bot = commands.Bot(command_prefix=commands.when_mentioned_or('/'), intents=intents)

    # bot event handling
    events(bot)

    # run VAPORBOT2020
    bot.run(env['dev']['TOKEN'])


# --------------------------------------------------------------------- #
# --- End of file ----------------------------------------------------- #
