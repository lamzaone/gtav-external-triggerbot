# GTAV/FIVEM external triggerbot

## Version 2.0.0 Changelog - Performance update
  - **Removed Discord Link**: The Discord link has been removed from the terminal window for a cleaner experience.
  - **Customizable Pixel Search Color**: Users can now change the pixel search color, with the default key set to Left Ctrl.
  - **Enhanced Pixel Detection**: Pixel detection performance has been boosted by approximately 60%, leveraging ctypes to integrate C++ libraries.This version now has a very good reaction time, giving you a big edge over your opponents.

---

Very simple GTAV trigger bot for default crosshair made in python.

made out of boredom and pure curiousity of how well could pixel detection work in automating tasks inside videogames.
Why triggerbot and not something else? I don't know, this is the first thing that i thought of where the execution and reaction time would be this crucial.


- Undetected
- Completely external

  
Remaining unnoticed by anti-cheat systems and similar measures **doesn't** justify or encourage cheating in multiplayer games.

  The script checks the color of the pixel in the middle of the screen while you hold down rightclick.

  If an enemy NPC/player walks in front of it, the color changes to a dark red, which the script detects, and then sends clicks in random bursts.

  Reaction time: 0.025-0.035s average.  This delay makes it less viable on fivem due to the bad sync of the game and additional ping

```
pip install -r requirements.txt
```

to compile
```
pyinstaller --onefile .\main.py -n trigger.exe
```

