# About the Project
"Battle of Odds" is a short, simple turn-based battle game between a knight and a witch. In this game, there is no confirmed win between either side. Quite literally "odds" (or more aptly, the `random` module :P) determines who wins or loses by altering the base attack damage of either side on each turn through generating random integer values within a specified range.

This game was created on August, 2024 as part of a contest submission for a Python course. Our task was to create a game that somehow utilised the `pokemon.csv` file (included in the repository). I did so by extracting the maximum HP and corresponding ATK data from those contained within the file to implement each character's maximum health and base attack. 

# How to Play
Simply press the Space bar and watch each other's health go down until you win! (or lose!)

# Installation Procedure
1. Download the repository onto your local computer.
2. Install pygame using `pip install pygame` in the command line.
3. Run `main.py` using Python IDLE or any other IDE that supports Python.  
_**For VSCode**_
- _IF PYGAME DOES NOT DETECT AFTER INSTALLATION, SET INTERPRETER PATH TO THE "Global" PATH (C:\Python{version}\python.exe) INSTEAD OF THE "Recommended" PATH._
- _If you receive any `FileNotFound` errors when attempting to run `main.py` by itself, please Open the root folder in the window instead and run `main.py` from there. The reason for this error is the use of relative file paths to load the assets, which VSCode cannot detect unless it opens the project as a whole._ 

# Resources
- "Player" and "Witch" portraits(on either side of the GUI), Background, Tileset, Decorations (grass, flowers) created and owned by myself.
- GUI elements from [Minimal Fantasy GUI by etahoshi]
- "Player" sprites from [Animated Pixel Hero by rvros] 
- "Witch" sprites from [Witches Pack by 9E0]

[Minimal Fantasy GUI by etahoshi]: https://etahoshi.itch.io/minimal-fantasy-gui-by-eta
[Animated Pixel Hero by rvros]: https://rvros.itch.io/animated-pixel-hero
[Witches Pack by 9E0]: https://9e0.itch.io/witches-pack

# Known Issues
- The game cannot be packaged into an executable due to a Windows error where Python executables are often incorrectly flagged as viruses.
- The game window can look oversized, with elements cutting off screen (including the title bar) on larger displays/displays scaled upto 200%.
- The window itself is hard-coded to be 1600x900 and manually re-adjusting these values from within the code does not automatically resize the elements inside the window due to the presence of other hard-coded values.
- There is no system to restart the game or return to the main menu after the game has been won or lost.
- There is no buffer implemented for key pressing, meaning the player can continuously spam the Spacebar and deplete both characters' HP until the end of the game, effectively cancelling out the `hurt(witch)` animation. 
- The different tiles are layered together and exported as a single `tile.png` instead of placing individual tiles using any tile-mapping algorithm. The same goes for `grass.png`.
