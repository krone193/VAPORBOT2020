# --- VAPORBOT2020.py -------------------------------------------- #
# --------------------------------------------------------------------- #
# Date    :	22/11/2023                                                  #
# Authors :	krone                                                       #
# --------------------------------------------------------------------- #


# --- Imports --------------------------------------------------------- #
# --------------------------------------------------------------------- #
import discord
from discord.ext import commands
import json
from main import cmd
from main import env
import project.functions.sendMessage as funcMessaging
import project.functions.handleResponse as funcHandling


# --- SW Versions ----------------------------------------------------- #
# --------------------------------------------------------------------- #
SW_VER = "v0.1.1.0"
# --- Changelog ------------------------------------------------------- #
# vxx.xx.xx ----------------------------------------------------------- #
#   .                                                                   #
# --------------------------------------------------------------------- #
# v00.01.00 ----------------------------------------------------------- #
#   Project start                                                       #
# --------------------------------------------------------------------- #


# --- Defines --------------------------------------------------------- #
# --------------------------------------------------------------------- #
CommandsLiszt = [
    'aesthetic',
    'angry',
    'ban',
    'headpat',  # tmp placing
    'happy',    # tmp placing
    'blushy',
    'coffee',
    'displeased',
    'explore_galaxies',
    'good_morning',
    # 'happy',
    # 'headpat',
    'hug',
    'laugh',
    'opsy',
    'pause',
    'please',
    'rainy_mood',
    'resume',
    'sad',
    'shifting_dreams',
    'smile',
    'smirk',
    'sob',
    'sorry',
    'swish'
]


# --- Variables ------------------------------------------------------- #
# --------------------------------------------------------------------- #
# --- Classes --------------------------------------------------------- #
# --------------------------------------------------------------------- #
async def command_embed(interaction: discord.Interaction, payload: json):
    embed = funcHandling.embed_command_response(interaction, payload['DATA'])
    await interaction.response.send_message(embed=embed, ephemeral=False)


def events(bot):
    # ----------------------------------------------------------------- #
    @bot.event
    async def on_ready():
        print(f'{bot.user} is now running')
        try:
            sync = await bot.tree.sync()
            print(f"Sync {len(sync)} commands(s)")
        except Exception as err:
            print(err)

    # ----------------------------------------------------------------- #
    @bot.tree.command(name=cmd[CommandsLiszt[0]]['NAME'], description=cmd[CommandsLiszt[0]]['DESC'])
    async def slash_command_0(interaction: discord.Interaction):
        await command_embed(interaction, cmd[CommandsLiszt[0]])

    # ----------------------------------------------------------------- #
    @bot.tree.command(name=cmd[CommandsLiszt[1]]['NAME'], description=cmd[CommandsLiszt[1]]['DESC'])
    async def slash_command_1(interaction: discord.Interaction):
        await command_embed(interaction, cmd[CommandsLiszt[1]])

    # ----------------------------------------------------------------- #
    @bot.tree.command(name=cmd[CommandsLiszt[2]]['NAME'], description=cmd[CommandsLiszt[2]]['DESC'])
    async def slash_command_2(interaction: discord.Interaction):
        await command_embed(interaction, cmd[CommandsLiszt[2]])

    # ----------------------------------------------------------------- #
    @bot.tree.command(name=cmd[CommandsLiszt[3]]['NAME'], description=cmd[CommandsLiszt[3]]['DESC'])
    async def slash_command_3(interaction: discord.Interaction):
        await command_embed(interaction, cmd[CommandsLiszt[3]])

    # ----------------------------------------------------------------- #
    @bot.tree.command(name=cmd[CommandsLiszt[4]]['NAME'], description=cmd[CommandsLiszt[4]]['DESC'])
    async def slash_command_4(interaction: discord.Interaction):
        await command_embed(interaction, cmd[CommandsLiszt[4]])

    # ----------------------------------------------------------------- #
    @bot.event
    async def on_message(message):
        username = str(message.author)
        content = str(message.content)
        # channel = str(message.channel)

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
def run():
    # init intents
    intents = discord.Intents.default()
    intents.message_content = True

    # create Discord Client
    bot = commands.Bot(command_prefix=commands.when_mentioned_or("/"), intents=intents)

    # bot event handling
    events(bot)

    # run VAPORBOT2020
    bot.run(env['dev']['TOKEN'])


# --------------------------------------------------------------------- #
# --- End of file ----------------------------------------------------- #
