# GTAV/FIVEM external triggerbot

Very simple GTAV trigger bot for default crosshair made in python
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

