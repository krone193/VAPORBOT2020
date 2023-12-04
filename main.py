# --- main.py --------------------------------------------------------- #
# --------------------------------------------------------------------- #
# Date    :	29/11/2023                                                  #
# Authors :	krone                                                       #
# --------------------------------------------------------------------- #


# --- Imports --------------------------------------------------------- #
# --------------------------------------------------------------------- #
import json
import project.VAPORBOT2020 as VAPORBOT2020


# --- Defines --------------------------------------------------------- #
# --------------------------------------------------------------------- #
# --- Variables ------------------------------------------------------- #
# --------------------------------------------------------------------- #
fenv = open('env.json', encoding="utf8")
env = json.load(fenv)
fenv.close()
# --------------------------------------------------------------------- #
fcmd = open('commands.json', encoding="utf8")
cmd = json.load(fcmd)
fcmd.close()


# --- Functions ------------------------------------------------------- #
# --------------------------------------------------------------------- #
# --- Classes initialisation ------------------------------------------ #
# --------------------------------------------------------------------- #
# --- Variable initialisation ----------------------------------------- #
# --------------------------------------------------------------------- #


# --- Main ------------------------------------------------------------ #
# --------------------------------------------------------------------- #
if __name__ == '__main__':
    # run the bot
    VAPORBOT2020.run()

# --------------------------------------------------------------------- #
# --- End of file ----------------------------------------------------- #