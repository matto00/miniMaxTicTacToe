# miniMaxTicTacToe
Minimax algorithm implementation in Python, with PyGame use for GUI

---

## Structure
* This application runs as a pyhon module and can be run from the command line with the command
'python3 -m App'
from the root directory.

* Within the module is a sub-module for the game itself, wherein lies the settings file. If you'd like to edit any of the game settings, it can be done in 'App/_Game/settings.py

## Game Save-states
* Each time the application properly deconstructs, it saves the current state of the game in a binary file, you can enable and disable both save-states in general or the option to load a saved game-state

	* Both options are set to 'True' by default
