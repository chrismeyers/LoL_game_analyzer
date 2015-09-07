LoL_game_analyzer
===============

This project parses a specified statistic from a player's previous 10 games and plots the values.

<img src="http://i.imgur.com/MEz3Sbh.png" alt="Current GUI" width="494px" height="446px">

##Dependencies:
This application was built for Python **3** and requires it to run properly.  There are also a few third-party libraries that were used to provide graphing functionality:

1. The library `matplotlib` is needed for this project to run.
	* Visit `http://matplotlib.org/users/installing.html` for installation instructions for your system.

##Usage:
1. If needed, create a folder in the root directory named `notes`.
2. Create a .txt file inside the `notes` directory named `key.txt`.
3. Enter your api key into the `key.txt` file (key can be found at https://developer.riotgames.com/)
   * Make sure there are no spaces before, after, or in the key.
4. Run `python3 gui.py` from within `LoL_game_analyzer/src/`

##Legal

LoL_game_analyzer isn’t endorsed by Riot Games and doesn’t reflect the views or opinions of Riot Games or anyone officially involved in producing or managing *League of Legends*. *League of Legends* and Riot Games are trademarks or registered trademarks of Riot Games, Inc. *League of Legends* © Riot Games, Inc.
