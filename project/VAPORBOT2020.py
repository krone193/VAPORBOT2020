# --- VAPORBOT2020.py ------------------------------------------------------------------------------------------------ #
# -------------------------------------------------------------------------------------------------------------------- #
# Date          : 22/11/2023                                                                                           #
# Last edit     : 29/12/2023                                                                                           #
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
#                           - start random video    -> implemented                                                     #
#                           - track last random     -> implemented                                                     #
#                           - stop video            -> implemented                                                     #
#                           - pause video           -> implemented                                                     #
#                           - resume video          -> implemented                                                     #
#                           - auto-disconnect       -> implemented                                                     #
#                           - queue management      -> missing                                                         #
#                       * deployed message                                                                             #
#                           - send on trigger       -> missing                                                         #
#                       * add activity and status                                                                      #
#                           - set activity          -> implemented                                                     #
#                           - set status            -> implemented                                                     #
#                       * purge channel at fixed time                                                                  #
#                           - manage delete event   -> implemented                                                     #
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
import project.constants.dictionaries as dictionaries
# Project functions -------------------------------------------------------------------------------------------------- #
import project.functions.sendMessage as funcMessaging
import project.functions.manageJsons as funcJsonManage
# Project classes ---------------------------------------------------------------------------------------------------- #
import project.classes.handleCommand as handleCommand
import project.classes.handleResponse as handleResponse
import project.classes.handleMusic as handleMusic


# --- Class | VAPORBOT 2020 ------------------------------------------------------------------------------------------ #
# -------------------------------------------------------------------------------------------------------------------- #
class VAPORBOT2020:
    # Variables ------------------------------------------------------------------------------------------------------ #
    bot: commands.Bot
    config: json
    holidays: json
    mood_cmd: json
    music_cmd: json
    events: json
    deploy: str
    status: discord.Status
    act_type: discord.BaseActivity
    act_name: discord.Activity
    dt: datetime
    responseHandler: handleResponse
    musicHandler: handleMusic
    slash_commands = list()

    # Init: pass a .js file name for 'config' and 'commands' arguments ----------------------------------------------- #
    def __init__(self,
                 config_json: str,
                 holidays_json: str,
                 mood_json: str,
                 music_json: str,
                 events_json: str,
                 deploy: str
                 ):
        print('# --- INIT SEQUENCE --- #')

        # load configuration and content JSON files
        self.config = funcJsonManage.load_file(config_json, '#   config  file loaded #')
        self.holidays = funcJsonManage.load_file(holidays_json, '#   holiday file loaded #')
        self.mood_cmd = funcJsonManage.load_file(mood_json, '#   mood    file loaded #')
        self.music_cmd = funcJsonManage.load_file(music_json, '#   music   file loaded #')
        self.events = funcJsonManage.load_file(events_json, '#   events  file loaded #')

        # set execution environment
        if dictionaries.DEPLOYS[deploy] is None:
            print('#   wrong deploy arg    #')
            print('# --- EXIT SEQUENCE --- #')
            exit(1)
        self.deploy = deploy
        if self.deploy == dictionaries.DEPLOYS['release']:
            print('#   deploy  : release   #')
        else:
            print('#   deploy  : debug     #')

        # init handlers
        print('#   handlers:           #')
        self.responseHandler = handleResponse.HandleResponse(config=self.config,
                                                             events=self.events)  # response handler
        print('#    └ response  -> ok  #')
        self.musicHandler = handleMusic.HandleMusic()  # music handler
        print('#    └ music     -> ok  #')

        # init intents
        intents = discord.Intents.default()
        intents.message_content = True
        intents.members = True
        intents.messages = True
        print('#   intents:            #')
        print('#    └ default  +       #')
        print('#    └ members  = true  #')
        print('#    └ messages = true  #')
        print('#    └ content  = true  #')

        # create Discord Client
        self.bot = commands.Bot(command_prefix=str(commands.when_mentioned_or('/')),
                                intents=intents,
                                allowed_mention=discord.AllowedMentions(everyone=True))
        print('#   discord bot created #')

        # create and assign mood slash commands
        for command in self.mood_cmd:
            if command == 'test' and self.deploy == dictionaries.DEPLOYS['release']:
                print('#   skip test command   #')
            elif self.mood_cmd[command]['type'] == 'mood':
                self.slash_commands.append(handleCommand.MoodCommands(self.bot,
                                                                      self.mood_cmd[command],
                                                                      self.responseHandler))
        print('#   mood commands   ok  #')

        # create and assign music slash commands
        for command in self.music_cmd:
            if command == 'test' and self.deploy == dictionaries.DEPLOYS['release']:
                print('#   skip test command   #')
            elif self.music_cmd[command]['type'] == 'music':
                self.slash_commands.append(handleCommand.MusicCommands(self.bot,
                                                                       self.music_cmd[command],
                                                                       self.responseHandler,
                                                                       self.musicHandler))
        print('#   music commands  ok  #')
        print('# --------------------- #')

        # show version
        print(f"\n# --- {self.config['global']['name']} --- #")
        print(f"#   version : {self.config['global']['version']}   #")
        print(f"#   phase   : {self.config['global']['phase']}      #")
        print('# --------------------- #')

        @self.bot.event
        async def setup_hook() -> None:
            self.update_datetime()
            # wait for the next minute to start
            print('\n# --- HOOK SEQUENCE --- #')
            if deploy == 'release':
                print('# sync sequence start   #')
                while self.dt.second > 0:
                    sec = 60 - self.dt.second
                    print(f'#   - {sec:02d}', 'seconds' if sec > 1 else 'second ', 'left   #')
                    await asyncio.sleep(1)
                    self.update_datetime()
            # align the timer to trigger on minute start
            print('# timed_events start    #')
            self.timed_events_task.start()
            print('# --------------------- #')

        @self.bot.event
        async def on_ready():
            self.update_datetime()
            print('\n* event | on_ready (start)')
            print(f'*   {self.dt.strftime("%d/%m/%Y %H:%M:%S")}')
            print(f'*   {self.bot.user}')
            print(f'*   {self.bot.user.id}')
            try:
                self.status = discord.Status.online
                self.activity = discord.Activity(type=dictionaries.ACTIVITIES[self.config['global']['activity_type']],
                                                 name=self.config['global']['activity_name'])
                await self.bot.change_presence(status=self.status, activity=self.activity)
                print(f'*   status')
                print(f'*     └ {self.status}')
                print(f'*   activity')
                print(f'*     └ {self.activity.type}')
                print(f'*     └ {self.activity.name}')
                sync = await self.bot.tree.sync()
                self.update_datetime()
                print('\n* event | on_ready (close)')
                print(f'*   {self.dt.strftime("%d/%m/%Y %H:%M:%S")}')
                print(f'*   synced {len(sync)} command(s)')
            except Exception as err:
                print(err)

        @self.bot.event
        async def on_message(message: discord.Message):
            self.update_datetime()
            # do not process own messages
            if message.author == self.bot.user:
                return
            # do not process messages with no content
            if message.content == '':
                return
            # determine if response on private channel
            if message.content[0] == '?':
                message.content = message.content[1:]
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
                print('*   type    :', '@mention' if is_mention else 'text')

    # Run VAPORBOT2020 ----------------------------------------------------------------------------------------------- #
    def run(self, token: str):
        self.bot.run(token)

    # Update VAPORBOT inner date time reference ---------------------------------------------------------------------- #
    def update_datetime(self):
        self.dt = datetime.now()

    # Task loop for scheduled events handling ------------------------------------------------------------------------ #
    @tasks.loop(minutes=1)
    async def timed_events_task(self):
        self.update_datetime()
        print('\n* event | timed_events')
        print(f'*   {self.dt.strftime("%d/%m/%Y %H:%M:%S")}')
        for event in self.events:
            # check if on event trigger
            if (self.dt.isoweekday() in self.events[event]['iso_weekdays']  # check if on event's weekday(s)
                    and self.dt.hour in self.events[event]['hours']         # check if on event's hour(s)
                    and self.dt.minute in self.events[event]['minutes']):   # check if on event's minute(s)
                # switch for event types
                match self.events[event]['type']:
                    case 'delete':
                        # purge channel content
                        print(f'*   purging {self.events[event]["channel"]}')
                        channel = self.bot.get_channel(
                            self.config[self.events[event]['server']][self.events[event]['channel']])
                        await channel.purge()
                        print(f'*   {self.events[event]["channel"]} purged')
                    case 'message':
                        # check if in a national holiday
                        if self.dt.strftime("%d/%m") in self.holidays["holidays"]:
                            continue
                        # if CISA event, check for specific closure days
                        elif (event.find("CISA") >= 0) and (self.dt.strftime("%d/%m") in self.holidays["CISA"]):
                            continue
                        # if ElFa event, check for specific closure days
                        elif (event.find("ELFA") >= 0) and (self.dt.strftime("%d/%m") in self.holidays["ELFA"]):
                            continue
                        # manage message creation and send
                        channel = self.bot.get_channel(
                            self.config[self.events[event]['server']][self.events[event]['channel']])
                        embed = self.responseHandler.embed_timed_event(self.events[event])      # create event embed
                        await channel.send(embed=embed, content=self.events[event]['content'])  # send event message

    # Semaphore for scheduled events handling task ------------------------------------------------------------------- #
    @timed_events_task.before_loop
    async def timed_events_task_before_loop(self):
        await self.bot.wait_until_ready()

# -------------------------------------------------------------------------------------------------------------------- #
# --- End of file ---------------------------------------------------------------------------------------------------- #
