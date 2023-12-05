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
from datetime import datetime, timedelta
import time
from main import cmd
from main import env
import project.functions.sendMessage as funcMessaging
import project.functions.handleResponse as funcHandling


# --- SW Versions ----------------------------------------------------- #
# --------------------------------------------------------------------- #
SW_VER = "v0.1.2.0"
# --- Changelog ------------------------------------------------------- #
# vxx.xx.xx ----------------------------------------------------------- #
#   .                                                                   #
# --------------------------------------------------------------------- #
# v00.01.00 ----------------------------------------------------------- #
#   Project start                                                       #
# --------------------------------------------------------------------- #


# --- Defines --------------------------------------------------------- #
# --------------------------------------------------------------------- #
TimedEventsInterval = 1     # minutes, check if it's time for a programmed event
# --------------------------------------------------------------------- #
CommandsLiszt = [
    'aesthetic',
    'angry',
    'ban',
    'blushy',
    'coffee',
    'displeased',
    'explore_galaxies',
    'good_morning',
    'happy',
    'headpat',
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
    @bot.tree.command(name=cmd[CommandsLiszt[5]]['NAME'], description=cmd[CommandsLiszt[5]]['DESC'])
    async def slash_command_4(interaction: discord.Interaction):
        await command_embed(interaction, cmd[CommandsLiszt[5]])

    # ----------------------------------------------------------------- #
    @bot.tree.command(name=cmd[CommandsLiszt[6]]['NAME'], description=cmd[CommandsLiszt[6]]['DESC'])
    async def slash_command_4(interaction: discord.Interaction):
        await command_embed(interaction, cmd[CommandsLiszt[6]])

    # ----------------------------------------------------------------- #
    @bot.tree.command(name=cmd[CommandsLiszt[7]]['NAME'], description=cmd[CommandsLiszt[7]]['DESC'])
    async def slash_command_4(interaction: discord.Interaction):
        await command_embed(interaction, cmd[CommandsLiszt[7]])

    # ----------------------------------------------------------------- #
    @bot.tree.command(name=cmd[CommandsLiszt[8]]['NAME'], description=cmd[CommandsLiszt[8]]['DESC'])
    async def slash_command_4(interaction: discord.Interaction):
        await command_embed(interaction, cmd[CommandsLiszt[8]])

    # ----------------------------------------------------------------- #
    @bot.tree.command(name=cmd[CommandsLiszt[9]]['NAME'], description=cmd[CommandsLiszt[9]]['DESC'])
    async def slash_command_4(interaction: discord.Interaction):
        await command_embed(interaction, cmd[CommandsLiszt[9]])

    # ----------------------------------------------------------------- #
    @bot.tree.command(name=cmd[CommandsLiszt[10]]['NAME'], description=cmd[CommandsLiszt[10]]['DESC'])
    async def slash_command_4(interaction: discord.Interaction):
        await command_embed(interaction, cmd[CommandsLiszt[10]])

    # ----------------------------------------------------------------- #
    @bot.tree.command(name=cmd[CommandsLiszt[11]]['NAME'], description=cmd[CommandsLiszt[11]]['DESC'])
    async def slash_command_4(interaction: discord.Interaction):
        await command_embed(interaction, cmd[CommandsLiszt[11]])

    # ----------------------------------------------------------------- #
    @bot.tree.command(name=cmd[CommandsLiszt[12]]['NAME'], description=cmd[CommandsLiszt[12]]['DESC'])
    async def slash_command_4(interaction: discord.Interaction):
        await command_embed(interaction, cmd[CommandsLiszt[12]])

    # ----------------------------------------------------------------- #
    @bot.tree.command(name=cmd[CommandsLiszt[13]]['NAME'], description=cmd[CommandsLiszt[13]]['DESC'])
    async def slash_command_4(interaction: discord.Interaction):
        await command_embed(interaction, cmd[CommandsLiszt[13]])

    # ----------------------------------------------------------------- #
    @bot.tree.command(name=cmd[CommandsLiszt[14]]['NAME'], description=cmd[CommandsLiszt[14]]['DESC'])
    async def slash_command_4(interaction: discord.Interaction):
        await command_embed(interaction, cmd[CommandsLiszt[14]])

    # ----------------------------------------------------------------- #
    @bot.tree.command(name=cmd[CommandsLiszt[15]]['NAME'], description=cmd[CommandsLiszt[15]]['DESC'])
    async def slash_command_4(interaction: discord.Interaction):
        await command_embed(interaction, cmd[CommandsLiszt[15]])

    # ----------------------------------------------------------------- #
    @bot.tree.command(name=cmd[CommandsLiszt[16]]['NAME'], description=cmd[CommandsLiszt[16]]['DESC'])
    async def slash_command_4(interaction: discord.Interaction):
        await command_embed(interaction, cmd[CommandsLiszt[16]])

    # ----------------------------------------------------------------- #
    @bot.tree.command(name=cmd[CommandsLiszt[17]]['NAME'], description=cmd[CommandsLiszt[17]]['DESC'])
    async def slash_command_4(interaction: discord.Interaction):
        await command_embed(interaction, cmd[CommandsLiszt[17]])

    # ----------------------------------------------------------------- #
    @bot.tree.command(name=cmd[CommandsLiszt[18]]['NAME'], description=cmd[CommandsLiszt[18]]['DESC'])
    async def slash_command_4(interaction: discord.Interaction):
        await command_embed(interaction, cmd[CommandsLiszt[18]])

    # ----------------------------------------------------------------- #
    @bot.tree.command(name=cmd[CommandsLiszt[19]]['NAME'], description=cmd[CommandsLiszt[19]]['DESC'])
    async def slash_command_4(interaction: discord.Interaction):
        await command_embed(interaction, cmd[CommandsLiszt[19]])

    # ----------------------------------------------------------------- #
    @bot.tree.command(name=cmd[CommandsLiszt[20]]['NAME'], description=cmd[CommandsLiszt[20]]['DESC'])
    async def slash_command_4(interaction: discord.Interaction):
        await command_embed(interaction, cmd[CommandsLiszt[20]])

    # ----------------------------------------------------------------- #
    @bot.tree.command(name=cmd[CommandsLiszt[21]]['NAME'], description=cmd[CommandsLiszt[21]]['DESC'])
    async def slash_command_4(interaction: discord.Interaction):
        await command_embed(interaction, cmd[CommandsLiszt[21]])

    # ----------------------------------------------------------------- #
    @bot.tree.command(name=cmd[CommandsLiszt[22]]['NAME'], description=cmd[CommandsLiszt[22]]['DESC'])
    async def slash_command_4(interaction: discord.Interaction):
        await command_embed(interaction, cmd[CommandsLiszt[22]])

    # ----------------------------------------------------------------- #
    @bot.tree.command(name=cmd[CommandsLiszt[23]]['NAME'], description=cmd[CommandsLiszt[23]]['DESC'])
    async def slash_command_4(interaction: discord.Interaction):
        await command_embed(interaction, cmd[CommandsLiszt[23]])

    # ----------------------------------------------------------------- #
    # @bot.tree.command(name=cmd[CommandsLiszt[24]]['NAME'], description=cmd[CommandsLiszt[24]]['DESC'])
    # async def slash_command_4(interaction: discord.Interaction):
    #     await command_embed(interaction, cmd[CommandsLiszt[24]])

    # ----------------------------------------------------------------- #
    # @bot.tree.command(name=cmd[CommandsLiszt[25]]['NAME'], description=cmd[CommandsLiszt[25]]['DESC'])
    # async def slash_command_4(interaction: discord.Interaction):
    #     await command_embed(interaction, cmd[CommandsLiszt[25]])

    # ----------------------------------------------------------------- #
    # @bot.tree.command(name=cmd[CommandsLiszt[26]]['NAME'], description=cmd[CommandsLiszt[26]]['DESC'])
    # async def slash_command_4(interaction: discord.Interaction):
    #     await command_embed(interaction, cmd[CommandsLiszt[26]])

    # ----------------------------------------------------------------- #
    # @bot.tree.command(name=cmd[CommandsLiszt[27]]['NAME'], description=cmd[CommandsLiszt[27]]['DESC'])
    # async def slash_command_4(interaction: discord.Interaction):
    #     await command_embed(interaction, cmd[CommandsLiszt[27]])

    # ----------------------------------------------------------------- #
    # @bot.tree.command(name=cmd[CommandsLiszt[28]]['NAME'], description=cmd[CommandsLiszt[28]]['DESC'])
    # async def slash_command_4(interaction: discord.Interaction):
    #     await command_embed(interaction, cmd[CommandsLiszt[28]])

    # ----------------------------------------------------------------- #
    # @bot.tree.command(name=cmd[CommandsLiszt[29]]['NAME'], description=cmd[CommandsLiszt[29]]['DESC'])
    # async def slash_command_4(interaction: discord.Interaction):
    #     await command_embed(interaction, cmd[CommandsLiszt[29]])

    # ----------------------------------------------------------------- #
    # @bot.tree.command(name=cmd[CommandsLiszt[30]]['NAME'], description=cmd[CommandsLiszt[30]]['DESC'])
    # async def slash_command_4(interaction: discord.Interaction):
    #     await command_embed(interaction, cmd[CommandsLiszt[30]])

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


# ----------------------------------------------------------------- #
def get_last_sunday(year, month) -> datetime:
    if month == 12:
        dt = datetime(year + 1, 1, 1, 12)
    else:
        dt = datetime(year, month + 1, 1, 12)

    diff = 7 if dt.isoweekday() == 0 else dt.isoweekday()
    return dt - timedelta(days=diff)


# ----------------------------------------------------------------- #
def dt_next_update(dt: datetime, minutes) -> datetime:
    dest = dt + timedelta(minutes=minutes)
    return dest.replace(second=0)


# ----------------------------------------------------------------- #
def on_time_events(dt: datetime):
    # legal = get_last_sunday(dt.year, 3)
    # solar = get_last_sunday(dt.year, 10)
    # add_hour = 0

    # match dt.month:
    #    case 1 | 2 | 11 | 12:
    #        add_hour = 1
    #    case 4 | 5 | 6 | 7 | 8 | 9:
    #        add_hour = 2
    #    case 3:
    #        add_hour = 1 if dt.day < legal.day else 2
    #    case 10:
    #        add_hour = 2 if dt.day < solar.day else 1

    # dt += timedelta(hours=add_hour)
    print(dt)


# --- Main ------------------------------------------------------------ #
# --------------------------------------------------------------------- #
def run():
    # init intents
    intents = discord.Intents.default()
    intents.message_content = True

    # create Discord Client
    bot = commands.Bot(command_prefix=str(commands.when_mentioned_or("/")), intents=intents)

    # bot event handling
    events(bot)

    # run VAPORBOT2020
    bot.run(env['dev']['TOKEN'])

    # loop for timed events
    dt = datetime.now()
    dt_next = dt_next_update(dt, minutes=TimedEventsInterval)
    print(dt.strftime("%d/%m/%Y %H:%M:%S") + " | Bot started, next wake-up at " +
          dt_next.strftime("%d/%m/%Y %H:%M:%S"))
    while 1:
        dt = datetime.now()
        if dt > dt_next:
            dt_next = dt_next_update(dt, minutes=TimedEventsInterval)
            print(dt.strftime("%d/%m/%Y %H:%M:%S") + " | Main loop, next wake-up at " +
                  dt_next.strftime("%d/%m/%Y %H:%M:%S"))
            # on_time_events(dt)
        else:
            time.sleep(1)


# --------------------------------------------------------------------- #
# --- End of file ----------------------------------------------------- #
