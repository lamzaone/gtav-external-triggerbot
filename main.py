import random
import threading
import time
import winsound
import keyboard
import pyautogui
from pynput.mouse import Listener, Button
import os

# Function to update the status line to reflect the state of the triggerbot
def update_status():
    status_text = "[CURRENTLY: {}]".format("ON  " if running else "OFF ")
    status_line = f"LEFT ALT - TOGGLE ON/OFF {status_text}".center(52)
    print("\r{}".format(status_line), end='', flush=True)

# Function to resize the terminal window
def resize_terminal(width, height):
    try:
        os.system(f"resize -s {height} {width}")
    except Exception as e:
        print(f"Error resizing terminal: {e}")

# Example: Resize the terminal to 80 columns and 24 rows
resize_terminal(53, 15)
os.system("mode con cols=53 lines=15")

# Flag to indicate if the right mouse button is currently pressed
right_mouse_pressed = False


# Clear the terminal window
os.system('cls')
version = "1.5.4"
running = True
alive = True

version_msg = "v"+version+" by Azazel"


# Print the header
print("  ____  _          _ _")
print(" / ___|| | ___   _| | | https://discord.gg/RxcMj7x5Bx")
print(f" \___ \| |/ / | | | | |         ")
print("  ___) |   <| |_| | | | ____                _")
print(" |____/|_|\_\\\\__,_|_|_|/ ___|__ _ _ __   __| |_   _")
print("                      | |   / _` | '_ \ / _` | | | |")
print("                      | |__| (_| | | | | (_| | |_| |")
print("                       \____\__,_|_| |_|\__,_|\__, |")
print("                                              |___/ ")
print("====================================================")
print(f"{version_msg.center(52)}")
print("====================================================")
print("END - KILL SCRIPT".center(52))
update_status()


# Function to toggle the main loop
def kill_script():
    global alive
    winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
    alive = not alive


# Function to toggle the triggerbot on/off
def toggle_running():
    global running
    running = not running
    update_status() # Update the status line to reflect thestate of the triggerbot
    if running:
        winsound.PlaySound("SystemHand", winsound.SND_ASYNC)
    else:
        winsound.PlaySound("SystemExit", winsound.SND_ASYNC)


# Set up the hotkeys
keyboard.add_hotkey('left_alt', toggle_running) # Toggle the triggerbot on/off
keyboard.add_hotkey('END', kill_script) # Kill the script


# Function to handle mouse click events
def on_click(x, y, button, pressed):
    global right_mouse_pressed
    if button == Button.right:
        right_mouse_pressed = pressed

# Set up the mouse listener
mouse_listener = Listener(on_click=on_click)
mouse_listener.start()
x = pyautogui.size().width // 2
y = pyautogui.size().height // 2



def check():

    if pyautogui.pixel(x, y)[0] == 193:
        pyautogui.mouseDown()
        time.sleep(random.uniform(0.06, 0.2))
        pyautogui.mouseUp()


while alive:
    if running and right_mouse_pressed:
        color_check_thread = threading.Thread(target=check)
        color_check_thread.start()
        color_check_thread.join()
    time.sleep(0.0005)

# Stop the mouse listener

mouse_listener.stop()
mouse_listener.join()