# --- main.py -------------------------------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #
# Date          : 29/11/2023                                                                                           #
# Author(s)     : krone                                                                                                #
# Last edit     : 06/12/2023                                                                                           #
# Description   : starting file to initiate and run VAPORBOT2020                                                       #
# -------------------------------------------------------------------------------------------------------------------- #


# --- Imports -------------------------------------------------------------------------------------------------------- #
# Python libraries---------------------------------------------------------------------------------------------------- #
import json
# Project bot -------------------------------------------------------------------------------------------------------- #
import project.VAPORBOT2020 as VAPORBOT2020


# --- Variables ------------------------------------------------------------------------------------------------------ #
# -------------------------------------------------------------------------------------------------------------------- #
# --- Classes -------------------------------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #
# --- Functions ------------------------------------------------------------------------------------------------------ #
# -------------------------------------------------------------------------------------------------------------------- #


# --- Main ----------------------------------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #
if __name__ == '__main__':
    # get dev options
    file_env = open("env.json", encoding="utf8")
    env = json.load(file_env)
    file_env.close()

    # run the bot
    VAPORBOT2020 = VAPORBOT2020.VAPORBOT2020('config.json', 'commands.json')
    VAPORBOT2020.run(env['dev']['token'])

# -------------------------------------------------------------------------------------------------------------------- #
# --- End of file ---------------------------------------------------------------------------------------------------- #
