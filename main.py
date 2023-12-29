# --- main.py -------------------------------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #
# Date          : 29/11/2023                                                                                           #
# Last edit     : 29/12/2023                                                                                           #
# Author(s)     : krone                                                                                                #
# Description   : starting file to initiate and run VAPORBOT2020                                                       #
# -------------------------------------------------------------------------------------------------------------------- #


# --- Imports -------------------------------------------------------------------------------------------------------- #
# Python libraries---------------------------------------------------------------------------------------------------- #
import sys
# Project bot -------------------------------------------------------------------------------------------------------- #
import project.VAPORBOT2020 as VAPORBOT2020
# Project functions -------------------------------------------------------------------------------------------------- #
import project.functions.manageJsons as funcJsonManage
# Project constants -------------------------------------------------------------------------------------------------- #
import project.constants.dictionaries as const


# --- Variables ------------------------------------------------------------------------------------------------------ #
# -------------------------------------------------------------------------------------------------------------------- #
env_file = 'resources/env.json'
config_file = 'resources/config.json'
holidays_file = 'resources/holidays.json'
mood_file = 'resources/mood.json'
music_file = 'resources/music.json'
events_file = 'resources/events.json'
deploy = 'debug'
phy = 'development'
release_file_path = '/home/krone/Bots/VAPORBOT2020/'


# --- Classes -------------------------------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #
# --- Functions ------------------------------------------------------------------------------------------------------ #
# -------------------------------------------------------------------------------------------------------------------- #


# --- Main ----------------------------------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #
if __name__ == '__main__':
    # check sys arguments
    try:
        deploy = sys.argv[1]
        phy = sys.argv[2]
    except IndexError:
        deploy = 'debug'
        phy = 'development'

    if const.DEPLOYS[deploy] is None:
        exit(1)
    if const.PHYS[phy] is None:
        exit(1)

    # adjust file path if in release environment
    if const.PHYS[phy] == const.PHYS['production']:
        env_file = release_file_path + env_file
        config_file = release_file_path + config_file
        holidays_file = release_file_path + holidays_file
        mood_file = release_file_path + mood_file
        music_file = release_file_path + music_file
        events_file = release_file_path + events_file

    # parse environment file
    env = funcJsonManage.load_file(env_file, '')

    # run the bot
    VAPORBOT2020 = VAPORBOT2020.VAPORBOT2020(config_file,
                                             holidays_file,
                                             mood_file,
                                             music_file,
                                             events_file,
                                             const.DEPLOYS[deploy])
    VAPORBOT2020.run(env[deploy]['token'])

# -------------------------------------------------------------------------------------------------------------------- #
# --- End of file ---------------------------------------------------------------------------------------------------- #
