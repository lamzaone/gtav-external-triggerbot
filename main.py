import random
import threading
import time
import winsound
import keyboard
import pyautogui
from pynput.mouse import Listener, Button
import os


version = "1.5.4" # exactly what it says
running = True # Whether or not the triggerbot is running
alive = True # Whether or not the main loop is running, used to kill the script completely
right_mouse_pressed = False # Whether or not the right mouse button is pressed

# define the keybinds
kill_script_keybind = "END"
toggle_running_keybind = "left_alt" 



# Function to update the status line to reflect the state of the triggerbot
def update_status():
    status_text = "[CURRENTLY: {}]".format("ON  " if running else "OFF ") # If the triggerbot is running, display ON, otherwise display OFF
    status_line = f"LEFT ALT - TOGGLE ON/OFF {status_text}".center(52)
    print("\r{}".format(status_line), end='', flush=True) # using \r to overwrite the previous line in the terminal

# Function to resize the terminal window
def resize_terminal(width, height):
    try:
        os.system(f"resize -s {height} {width}")
    except Exception as e:
        print(f"Error resizing terminal: {e}")

resize_terminal(53, 15)
os.system("mode con cols=53 lines=15")





# Function to toggle the main loop
def kill_script():
    global alive
    winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
    alive = not alive


# Function to toggle the triggerbot on/off
def toggle_running():
    global running
    running = not running
    update_status() # call update_status to update the status line in the terminal window
    if running:
        winsound.PlaySound("SystemHand", winsound.SND_ASYNC)
    else:                  # yay sounds
        winsound.PlaySound("SystemExit", winsound.SND_ASYNC)




# Function to handle mouse click events
def on_click(x, y, button, pressed):
    global right_mouse_pressed
    if button == Button.right:
        right_mouse_pressed = pressed # Set right_mouse_pressed to True if the right mouse button is pressed, otherwise set it to False

# Set up the mouse listener
mouse_listener = Listener(on_click=on_click)
mouse_listener.start()

# Get the center of the screen
x = pyautogui.size().width // 2
y = pyautogui.size().height // 2

# Function to check the color of the pixel at the center of the screen
def check():
    if pyautogui.pixel(x, y)[0] == 193: # Check if the pixel at the center of the screen is red
        pyautogui.mouseDown() # If it is, hold down the left mouse button
        time.sleep(random.uniform(0.06, 0.2)) # Wait a random amount of time between 0.06 and 0.2 seconds
        pyautogui.mouseUp() # Release the left mouse button

# Set up the hotkeys
keyboard.add_hotkey(toggle_running_keybind, toggle_running) # Toggle the triggerbot on/off
keyboard.add_hotkey(kill_script_keybind, kill_script) # Kill the script

os.system('cls')
version_msg = "v"+version+" by Azazel"
print("  ____  _          _ _")
print(" / ___|| | ___   _| | | https://discord.gg/RxcMj7x5Bx")
print(" \___ \| |/ / | | | | |         ")
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


# Main loop
while alive: # While alive is True, run the main loop
    if running and right_mouse_pressed: # If the triggerbot is running and the right mouse button is pressed, run the check function in a separate thread
        color_check_thread = threading.Thread(target=check) # This is done to prevent the main loop from being blocked by the check function
        color_check_thread.start() # Start the thread
        color_check_thread.join() # Wait for the thread to finish
    time.sleep(0.0005) # Sleep for 0.0005 seconds to prevent the script from using too much CPU




# Stop the mouse listener
mouse_listener.stop()
mouse_listener.join()