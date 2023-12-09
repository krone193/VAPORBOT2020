# --- VAPORBOT2020.py ------------------------------------------------------------------------------------------------ #
# -------------------------------------------------------------------------------------------------------------------- #
# Date          : 22/11/2023                                                                                           #
# Last edit     : 09/12/2023                                                                                           #
# Author(s)     : krone                                                                                                #
# Description   : VAPORBOT2020, a Discord bot powered by aesthetic and nostalgia.                                      #
#                 This file contains the main class for the bot, with all events, commands and loop tasks handling.    #
#                 Current implementations:                                                                             #
#                       * reply to text messages                                                                       #
#                           - on same channel       -> implemented                                                     #
#                           - on private channel    -> implemented                                                     #
#                       * reply on mention                                                                             #
#                           - on direct @mention    -> implemented                                                     #
#                           - block on reply        -> implemented                                                     #
#                       * loop for on-time events                                                                      #
#                           - 1 minute loop         -> implemented                                                     #
#                           - send events           -> implemented                                                     #
#                       * slash commands                                                                               #
#                           - random data           -> implemented                                                     #
#                           - track last random     -> implemented                                                     #
#                           - option & choices      -> missing                                                         #
#                       * reproduce from YouTube                                                                       #
#                           - slash template        -> implemented                                                     #
#                           - start random video    -> missing                                                         #
#                           - track last random     -> missing                                                         #
#                           - stop video            -> missing                                                         #
#                           - pause video           -> missing                                                         #
#                       * deployed message                                                                             #
#                           - send on trigger       -> missing                                                         #
#                       * add activity and status                                                                      #
#                           - set activity          -> implemented                                                     #
#                           - set status            -> implemented                                                     #
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
import project.constants.servers as servers
import project.constants.dictionaries as dictionaries
# Project functions -------------------------------------------------------------------------------------------------- #
import project.functions.sendMessage as funcMessaging
# Project classes ---------------------------------------------------------------------------------------------------- #
import project.classes.handleCommand as handleCommand
import project.classes.handleResponse as handleResponse


# --- Class | VAPORBOT 2020 ------------------------------------------------------------------------------------------ #
# -------------------------------------------------------------------------------------------------------------------- #
class VAPORBOT2020:
    # Variables ------------------------------------------------------------------------------------------------------ #
    bot: commands.Bot
    config: json
    cmd: json
    deploy: str
    status: discord.Status
    act_type: discord.BaseActivity
    act_name: discord.Activity
    dt: datetime
    responseHandler: handleResponse
    slash_commands = list()

    # Init: pass a .js file name for 'config' and 'commands' arguments ----------------------------------------------- #
    def __init__(self, config_json: str, commands_json: str, deploy: str):
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

        # set execution environment
        self.deploy = deploy

        # init response handler
        self.responseHandler = handleResponse.HandleResponse(config=self.config)
        print("#   responseHandler ok  #")

        # init intents
        intents = discord.Intents.default()
        intents.message_content = True
        intents.members = True
        intents.messages = True
        print("#   intents:            #")
        print("#    └ default  +       #")
        print("#    └ members  = true  #")
        print("#    └ messages = true  #")
        print("#    └ content  = true  #")

        # create Discord Client
        self.bot = commands.Bot(command_prefix=str(commands.when_mentioned_or("/")),
                                intents=intents,
                                allowed_mention=discord.AllowedMentions(everyone=True))
        print("#   discord bot created #")

        # create and assign slash commands
        for command in self.cmd:
            if command == 'test' and deploy == 'release':
                print("#   skip test command   #")
                print("# --------------------- #")
            else:
                self.slash_commands.append(handleCommand.SlashCommands(self.bot, self.cmd[command],
                                                                       self.responseHandler))
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
            if deploy == 'release':
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
            self.update_datetime()
            print("\n* event | on_ready (start)")
            print(f'*   {self.dt.strftime("%d/%m/%Y %H:%M:%S")}')
            print(f'*   {self.bot.user}')
            print(f'*   {self.bot.user.id}')
            try:
                self.status = discord.Status.online
                self.activity = discord.Activity(type=dictionaries.activities[self.config['global']['activity_type']],
                                                 name=self.config['global']['activity_name'])
                await self.bot.change_presence(status=self.status, activity=self.activity)
                print(f"*   status")
                print(f"*     └ {self.status}")
                print(f"*   activity")
                print(f"*     └ {self.activity.type}")
                print(f"*     └ {self.activity.name}")
                sync = await self.bot.tree.sync()
                self.update_datetime()
                print('\n* event | on_ready (close)')
                print(f'*   {self.dt.strftime("%d/%m/%Y %H:%M:%S")}')
                print(f"*   synced {len(sync)} command(s)")
            except Exception as err:
                print(err)

        @self.bot.event
        async def on_message(message: discord.Message):
            self.update_datetime()
            username = str(message.author)
            content = str(message.content)
            # do not process own messages
            if username == self.bot.user:
                return
            # do not process messages with no content
            if content == '':
                return
            # determine if response on private channel
            if content[0] == '?':
                content = content[1:]
                private = True
                await message.delete()
            else:
                private = False
            # get message complete context
            ctx = await self.bot.get_context(message)
            # check if possible to reply to mentions
            is_mention = False
            if self.bot.user.mentioned_in(message) and message.mention_everyone is False:
                if message.reference is None:
                    is_mention = True
                else:
                    reply_msg = await ctx.channel.fetch_message(message.reference.message_id)
                    if reply_msg.author != self.bot.user:
                        is_mention = True
            # get response
            response = self.responseHandler.handle_response(self.bot, ctx, is_mention)
            # send response
            if response is not None:
                await funcMessaging.send_message(message, response, is_mention, private)
                print('\n* event | on message')
                print(f'*   {self.dt.strftime("%d/%m/%Y %H:%M:%S")}')
                print(f'*   server  : {ctx.guild.name}')
                print(f'*   channel : {ctx.channel.name}')
                print(f'*   author  : {ctx.author.name}')
                print('*   type    :', "@mention" if is_mention else "text")

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
        print('\n* event | timed_events')
        print(f'*   {self.dt.strftime("%d/%m/%Y %H:%M:%S")}')
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


# -------------------------------------------------------------------------------------------------------------------- #
# --- End of file ---------------------------------------------------------------------------------------------------- #
