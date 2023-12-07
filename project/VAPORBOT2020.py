# --- VAPORBOT2020.py ------------------------------------------------------------------------------------------------ #
# -------------------------------------------------------------------------------------------------------------------- #
# Date          : 22/11/2023                                                                                           #
# Last edit     : 07/12/2023                                                                                           #
# Author(s)     : krone                                                                                                #
# Description   : VAPORBOT2020, a Discord bot powered by aesthetic and nostalgia.                                      #
#                 This file contains the main class for the bot, with all events, commands and loop tasks handling.    #
#                 Current implementations:                                                                             #
#                       * reply to text messages                                                                       #
#                           - on same channel       -> implemented                                                     #
#                           - on private channel    -> implemented                                                     #
#                       * reply on mention                                                                             #
#                           - on direct @mention    -> implemented                                                     #
#                           - block on reply        -> missing                                                         #
#                       * loop for on-time events                                                                      #
#                           - 1 minute loop         -> implemented                                                     #
#                           - send events           -> implemented                                                     #
#                       * slash commands                                                                               #
#                           - random data           -> implemented                                                     #
#                           - track last random     -> missing                                                         #
#                       * reproduce from YouTube                                                                       #
#                           - slash template        -> implemented                                                     #
#                           - start random video    -> missing                                                         #
#                           - track last random     -> missing                                                         #
#                           - stop video            -> missing                                                         #
#                           - pause video           -> missing                                                         #
#                       * deployed message                                                                             #
#                           - send on trigger       -> missing                                                         #
#                       * add activity and status                                                                      #
#                           - set activity          -> missing                                                         #
#                           - set status            -> missing                                                         #
# -------------------------------------------------------------------------------------------------------------------- #


# --- Imports -------------------------------------------------------------------------------------------------------- #
# Discord API wrapper ------------------------------------------------------------------------------------------------ #
import discord
from discord.ext import tasks, commands
# Python libraries --------------------------------------------------------------------------------------------------- #
import json
import asyncio
from datetime import datetime
# Project constants -------------------------------------------------------------------------------------------------- #
import project.constants.events as events
import project.constants.commands as slash
import project.constants.servers as servers
# Project functions -------------------------------------------------------------------------------------------------- #
import project.functions.sendMessage as funcMessaging
# Project classes ---------------------------------------------------------------------------------------------------- #
import project.classes.handleResponse as handleResponse


# --- Class | VAPORBOT 2020 ------------------------------------------------------------------------------------------ #
# -------------------------------------------------------------------------------------------------------------------- #
class VAPORBOT2020:
    # Variables ------------------------------------------------------------------------------------------------------ #
    bot: commands.Bot
    config: json
    cmd: json
    dt: datetime
    responseHandler: handleResponse

    # Init: pass a .js file name for 'config' and 'commands' arguments ----------------------------------------------- #
    def __init__(self, config_json: str, commands_json: str):
        # load configurations json
        print("# --- INIT SEQUENCE --- #")
        file_config = open(config_json, encoding="utf8")
        self.config = json.load(file_config)
        file_config.close()
        print("#   config file loaded  #")

        # load commands json
        file_cmd = open(commands_json, encoding="utf8")
        self.cmd = json.load(file_cmd)
        file_cmd.close()
        print("#   command file loaded #")

        # init response handler
        self.responseHandler = handleResponse.HandleResponse(config=self.config)
        print("#   responseHandler ok  #")

        # init intents
        intents = discord.Intents.default()
        intents.message_content = True
        intents.members = True
        intents.messages = True
        print("#   intents: default    #")
        print("#    + members  = true  #")
        print("#    + messages = true  #")
        print("#    + content  = true  #")

        # create Discord Client
        self.bot = commands.Bot(command_prefix=str(commands.when_mentioned_or("/")),
                                intents=intents,
                                allowed_mention=discord.AllowedMentions(everyone=True))
        print("#   discord bot created #")

        # create and assign slash commands
        self.slash_commands_setup()
        print("#   slash commands ok   #")
        print("# --------------------- #")

        # show version
        print("\n# ---", self.config['global']['name'], "--- #")
        print("#   version :", self.config['global']['version'], "  #")
        print("#   phase   :", self.config['global']['phase'], "     #")
        print("# --------------------- #")

        @self.bot.event
        async def setup_hook() -> None:
            self.update_datetime()
            # wait for the next minute to start
            print("\n# --- HOOK SEQUENCE --- #")
            print("# sync sequence start   #")
            while self.dt.second > 0:
                sec = 60 - self.dt.second
                if sec > 9:
                    print("#   -", str(sec), "seconds left   #")
                elif sec > 1:
                    print("#   -", str(sec), " seconds left   #")
                else:
                    print("#   -", str(sec), " second left    #")
                await asyncio.sleep(1)
                self.update_datetime()
            # align the timer to trigger on minute start
            print("# timed_events start    #")
            self.timed_events_task.start()
            print("# --------------------- #")

        @self.bot.event
        async def on_ready():
            print("\n* event | on_ready (start)")
            print(f'*   {self.bot.user}')
            print(f'*   {self.bot.user.id}')
            try:
                sync = await self.bot.tree.sync()
                print("\n* event | on_ready (close)")
                print(f"*   synced {len(sync)} command(s)")
            except Exception as err:
                print(err)

        @self.bot.event
        async def on_message(message):
            username = str(message.author)
            content = str(message.content)
            # channel = str(message.channel)
            if username == self.bot.user:
                return
            if content == '':
                return
            if self.bot.user.mentioned_in(message) and message.mention_everyone is False:
                ctx = await self.bot.get_context(message)
                response = self.responseHandler.mention(ctx.author)
                await funcMessaging.send_message(message, response, True, False)
                print("\n* event | bot @mention")
                print("*   server  :", ctx.guild.name)
                print("*   channel :", ctx.channel.name)
                print("*   author  :", ctx.author.name)
                return
            if content[0] == '?':
                content = content[1:]
                private = True
                await message.delete()
            else:
                private = False
            response = self.responseHandler.handle_response(content)
            if response != '':
                await funcMessaging.send_message(message, response, False, private)

    # Run VAPORBOT2020 ----------------------------------------------------------------------------------------------- #
    def run(self, token: str):
        self.bot.run(token)

    # Update VAPORBOT inner date time reference ---------------------------------------------------------------------- #
    def update_datetime(self):
        self.dt = datetime.now()

    # Task loop for scheduled events handling ------------------------------------------------------------------------ #
    @tasks.loop(minutes=1)
    async def timed_events_task(self):
        # loop functions --------------------------------------------------------------------------------------------- #
        self.update_datetime()
        print("\n* event | timed_events")
        print(self.dt.strftime("*   %d/%m/%Y %H:%M:%S"))
        event = events.NULL
        server = servers.NULL
        # working day handling --------------------------------------------------------------------------------------- #
        if 1 <= self.dt.isoweekday() <= 5:
            # good morning positive vibes ---------------------------------------------------------------------------- #
            if self.dt.hour == events.MORNING_HOUR and self.dt.minute == events.MORNING_MINUTE:
                event = events.MORNING
                server = servers.SOVIET_ONION
            # coffe break -------------------------------------------------------------------------------------------- #
            if ((self.dt.hour == events.COFFEE_HOURS[0] or self.dt.hour == events.COFFEE_HOURS[1])
                    and self.dt.minute == events.COFFEE_MINUTE):
                event = events.COFFEE
                server = servers.SOVIET_ONION
            # lunch break start -------------------------------------------------------------------------------------- #
            if self.dt.hour == events.LUNCH_HOUR and self.dt.minute == events.LUNCH_MINUTE:
                event = events.LUNCH
                server = servers.SOVIET_ONION
            # El.Fa. end of day -------------------------------------------------------------------------------------- #
            if self.dt.hour == events.BYE_ELFA_HOUR and self.dt.minute == events.BYE_ELFA_MINUTE:
                event = events.BYE_ELFA
                server = servers.SOVIET_ONION
            # CISA end of day ---------------------------------------------------------------------------------------- #
            if self.dt.hour == events.BYE_CISA_HOUR and self.dt.minute == events.BYE_CISA_MINUTE:
                event = events.BYE_CISA
                server = servers.SOVIET_ONION
        # week-end days handling ------------------------------------------------------------------------------------- #
        else:
            if (self.dt.hour == 9 or self.dt.hour == 15) and self.dt.minute == 0:
                event = events.ANGS
                server = servers.SOVIET_ONION

        # in case of event send content ------------------------------------------------------------------------------ #
        if event != events.NULL and server != servers.NULL:
            channel = self.bot.get_channel(int(self.config[server][event]['channel']))
            embed = self.responseHandler.embed_timed_event(server, event)
            await channel.send(embed=embed, content=self.config[server][event]['content'])

    # Semaphore for scheduled events handling task ------------------------------------------------------------------- #
    @timed_events_task.before_loop
    async def timed_events_task_before_loop(self):
        await self.bot.wait_until_ready()

    # Slash commands' common function to generate and send the embedded response ------------------------------------- #
    async def slash_commands_embed(self, interaction: discord.Interaction, cmd_index: int):
        embed = self.responseHandler.embed_command_response(interaction, self.cmd[slash.LIZST[cmd_index]]['data'])
        await interaction.response.send_message(embed=embed, ephemeral=False)
        print("\n* event | slash command")
        print("*   server  :", interaction.guild.name)
        print("*   channel :", interaction.channel.name)
        print("*   command :", self.cmd[slash.LIZST[cmd_index]]['name'])
        print("*   author  :", interaction.user.name)

    # Slash commands' generation and setup --------------------------------------------------------------------------- #
    def slash_commands_setup(self):
        # ------------------------------------------------------------------------------------------------------------ #
        @self.bot.tree.command(name=self.cmd[slash.LIZST[0]]['name'], description=self.cmd[slash.LIZST[0]]['desc'])
        async def slash_command_00(interaction: discord.Interaction):
            await self.slash_commands_embed(interaction, 0)

        # ------------------------------------------------------------------------------------------------------------ #
        @self.bot.tree.command(name=self.cmd[slash.LIZST[1]]['name'], description=self.cmd[slash.LIZST[1]]['desc'])
        async def slash_command_01(interaction: discord.Interaction):
            await self.slash_commands_embed(interaction, 1)

        # ------------------------------------------------------------------------------------------------------------ #
        @self.bot.tree.command(name=self.cmd[slash.LIZST[2]]['name'], description=self.cmd[slash.LIZST[2]]['desc'])
        async def slash_command_02(interaction: discord.Interaction):
            await self.slash_commands_embed(interaction, 2)

        # ------------------------------------------------------------------------------------------------------------ #
        @self.bot.tree.command(name=self.cmd[slash.LIZST[3]]['name'], description=self.cmd[slash.LIZST[3]]['desc'])
        async def slash_command_03(interaction: discord.Interaction):
            await self.slash_commands_embed(interaction, 3)

        # ------------------------------------------------------------------------------------------------------------ #
        @self.bot.tree.command(name=self.cmd[slash.LIZST[4]]['name'], description=self.cmd[slash.LIZST[4]]['desc'])
        async def slash_command_04(interaction: discord.Interaction):
            await self.slash_commands_embed(interaction, 4)

        # ------------------------------------------------------------------------------------------------------------ #
        @self.bot.tree.command(name=self.cmd[slash.LIZST[5]]['name'], description=self.cmd[slash.LIZST[5]]['desc'])
        async def slash_command_05(interaction: discord.Interaction):
            await self.slash_commands_embed(interaction, 5)

        # ------------------------------------------------------------------------------------------------------------ #
        @self.bot.tree.command(name=self.cmd[slash.LIZST[6]]['name'], description=self.cmd[slash.LIZST[6]]['desc'])
        async def slash_command_06(interaction: discord.Interaction):
            await self.slash_commands_embed(interaction, 6)

        # ------------------------------------------------------------------------------------------------------------ #
        @self.bot.tree.command(name=self.cmd[slash.LIZST[7]]['name'], description=self.cmd[slash.LIZST[7]]['desc'])
        async def slash_command_07(interaction: discord.Interaction):
            await self.slash_commands_embed(interaction, 7)

        # ------------------------------------------------------------------------------------------------------------ #
        @self.bot.tree.command(name=self.cmd[slash.LIZST[8]]['name'], description=self.cmd[slash.LIZST[8]]['desc'])
        async def slash_command_08(interaction: discord.Interaction):
            await self.slash_commands_embed(interaction, 8)

        # ------------------------------------------------------------------------------------------------------------ #
        @self.bot.tree.command(name=self.cmd[slash.LIZST[9]]['name'], description=self.cmd[slash.LIZST[9]]['desc'])
        async def slash_command_09(interaction: discord.Interaction):
            await self.slash_commands_embed(interaction, 9)

        # ------------------------------------------------------------------------------------------------------------ #
        @self.bot.tree.command(name=self.cmd[slash.LIZST[10]]['name'], description=self.cmd[slash.LIZST[10]]['desc'])
        async def slash_command_10(interaction: discord.Interaction):
            await self.slash_commands_embed(interaction, 10)

        # ------------------------------------------------------------------------------------------------------------ #
        @self.bot.tree.command(name=self.cmd[slash.LIZST[11]]['name'], description=self.cmd[slash.LIZST[11]]['desc'])
        async def slash_command_11(interaction: discord.Interaction):
            await self.slash_commands_embed(interaction, 11)

        # ------------------------------------------------------------------------------------------------------------ #
        @self.bot.tree.command(name=self.cmd[slash.LIZST[12]]['name'], description=self.cmd[slash.LIZST[12]]['desc'])
        async def slash_command_12(interaction: discord.Interaction):
            await self.slash_commands_embed(interaction, 12)

        # ------------------------------------------------------------------------------------------------------------ #
        @self.bot.tree.command(name=self.cmd[slash.LIZST[13]]['name'], description=self.cmd[slash.LIZST[13]]['desc'])
        async def slash_command_13(interaction: discord.Interaction):
            await self.slash_commands_embed(interaction, 13)

        # ------------------------------------------------------------------------------------------------------------ #
        @self.bot.tree.command(name=self.cmd[slash.LIZST[14]]['name'], description=self.cmd[slash.LIZST[14]]['desc'])
        async def slash_command_14(interaction: discord.Interaction):
            await self.slash_commands_embed(interaction, 14)

        # ------------------------------------------------------------------------------------------------------------ #
        @self.bot.tree.command(name=self.cmd[slash.LIZST[15]]['name'], description=self.cmd[slash.LIZST[15]]['desc'])
        async def slash_command_15(interaction: discord.Interaction):
            await self.slash_commands_embed(interaction, 15)

        # ------------------------------------------------------------------------------------------------------------ #
        @self.bot.tree.command(name=self.cmd[slash.LIZST[16]]['name'], description=self.cmd[slash.LIZST[16]]['desc'])
        async def slash_command_16(interaction: discord.Interaction):
            await self.slash_commands_embed(interaction, 16)

        # ------------------------------------------------------------------------------------------------------------ #
        @self.bot.tree.command(name=self.cmd[slash.LIZST[17]]['name'], description=self.cmd[slash.LIZST[17]]['desc'])
        async def slash_command_17(interaction: discord.Interaction):
            await self.slash_commands_embed(interaction, 17)

        # ------------------------------------------------------------------------------------------------------------ #
        @self.bot.tree.command(name=self.cmd[slash.LIZST[18]]['name'], description=self.cmd[slash.LIZST[18]]['desc'])
        async def slash_command_18(interaction: discord.Interaction):
            await self.slash_commands_embed(interaction, 18)

        # ------------------------------------------------------------------------------------------------------------ #
        @self.bot.tree.command(name=self.cmd[slash.LIZST[19]]['name'], description=self.cmd[slash.LIZST[19]]['desc'])
        async def slash_command_19(interaction: discord.Interaction):
            await self.slash_commands_embed(interaction, 19)

        # ------------------------------------------------------------------------------------------------------------ #
        @self.bot.tree.command(name=self.cmd[slash.LIZST[20]]['name'], description=self.cmd[slash.LIZST[20]]['desc'])
        async def slash_command_20(interaction: discord.Interaction):
            await self.slash_commands_embed(interaction, 20)

        # ------------------------------------------------------------------------------------------------------------ #
        @self.bot.tree.command(name=self.cmd[slash.LIZST[21]]['name'], description=self.cmd[slash.LIZST[21]]['desc'])
        async def slash_command_21(interaction: discord.Interaction):
            await self.slash_commands_embed(interaction, 21)

        # ------------------------------------------------------------------------------------------------------------ #
        @self.bot.tree.command(name=self.cmd[slash.LIZST[22]]['name'], description=self.cmd[slash.LIZST[22]]['desc'])
        async def slash_command_22(interaction: discord.Interaction):
            await self.slash_commands_embed(interaction, 22)

        # ------------------------------------------------------------------------------------------------------------ #
        @self.bot.tree.command(name=self.cmd[slash.LIZST[23]]['name'], description=self.cmd[slash.LIZST[23]]['desc'])
        async def slash_command_23(interaction: discord.Interaction):
            await self.slash_commands_embed(interaction, 23)


# -------------------------------------------------------------------------------------------------------------------- #
# --- End of file ---------------------------------------------------------------------------------------------------- #
