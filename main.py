import random
from win32process import REALTIME_PRIORITY_CLASS
import time
import winsound
import keyboard
import pyautogui
from pynput.mouse import Listener, Button
import os
from ctypes import *

version = "2.0.0"



# =================== KEYBINDS ===================

kill_script_keybind = "END"                       # PANIC KEY (kills the script)
toggle_running_keybind = "left_alt"               # TOGGLE ON/OFF
change_pixel_color_keybind = "left_ctrl"          # CHANGE PIXEL COLOR


# ================== UTILITIES ===================

user = windll.LoadLibrary("user32.dll")     # User32.dll
dc = user.GetDC(0)                          # Device context
gdi = windll.LoadLibrary("gdi32.dll")       # Graphics Device Interface

running = True                              # Running state
alive = True                                # Alive state
right_mouse_pressed = False                 # Right mouse button pressed state

def resize_terminal():
    os.system("mode con cols=53 lines=16")


def print_header():
    os.system('cls')
    print("  ____  _          _ _")
    print(" / ___|| | ___   _| | |           github.com/lamzaone")
    print(" \___ \| |/ / | | | | |         ")
    print("  ___) |   <| |_| | | | ____                _")
    print(" |____/|_|\_\\\\__,_|_|_|/ ___|__ _ _ __   __| |_   _")
    print("                      | |   / _` | '_ \ / _` | | | |")
    print("                      | |__| (_| | | | | (_| | |_| |")
    print("                       \____\__,_|_| |_|\__,_|\__, |")
    print("                                              |___/ ")
    print("====================================================")
    print(f"v{version}".center(52))
    print("====================================================")
    print(f"{kill_script_keybind.upper()} - PANIC KEY".center(52))
    print(f"{toggle_running_keybind.upper()} - TOGGLE ON/OFF".center(52))
    print(f"{change_pixel_color_keybind.upper()} - UPDATE PIXEL COLOR".center(52))
    

def kill_script():
    global alive
    winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
    alive = not alive

def toggle_running():
    global running
    running = not running
    if running:
        # winsound.PlaySound("SystemHand", winsound.SND_ASYNC)
        pass
    else:                 
        winsound.PlaySound("SystemExit", winsound.SND_ASYNC)



# ==================== MOUSE LISTENER ====================
def on_click(x, y, button, pressed):
    global right_mouse_pressed
    if button == Button.right:
        right_mouse_pressed = pressed 

mouse_listener = Listener(on_click=on_click)
mouse_listener.start()


# ================ PIXEL COLOR DETECTION =================
x = user.GetSystemMetrics(0) // 2 
y = user.GetSystemMetrics(1) // 2
search_color = 5197761 #7002955

def get_pixel():
    return gdi.GetPixel(dc, x, y)

def check():
    global search_color
    print(get_pixel())
    if get_pixel() == search_color:
        pyautogui.mouseDown()
        time.sleep(random.uniform(0.06, 0.2))
        pyautogui.mouseUp()

def change_pixel_color():
    global search_color
    search_color = get_pixel()


# ================= SET PRIORITY ===================
kernel32 = windll.kernel32
pid = os.getpid()
handle = kernel32.OpenProcess(0x1F0FFF, False, pid)                 # full access rights handle
kernel32.SetPriorityClass(handle, REALTIME_PRIORITY_CLASS)          # -20 is the highest priority
kernel32.CloseHandle(handle)                                        # close the handle to prevent memory leaks 

# ==================== MAIN LOOP ===================
keyboard.add_hotkey(toggle_running_keybind, toggle_running)
keyboard.add_hotkey(kill_script_keybind, kill_script)
keyboard.add_hotkey(change_pixel_color_keybind, change_pixel_color)

print_header()
while alive:
    if os.get_terminal_size().columns != 53 or os.get_terminal_size().lines != 16:
        resize_terminal()
        print_header()

    while running and right_mouse_pressed: # If the triggerbot is running and the right mouse button is pressed, run the check function in a separate thread
        check()
    time.sleep(0.001) # Sleep for 0.0005 seconds to prevent the script from using too much CPU

# Stop the mouse listener
mouse_listener.stop()
mouse_listener.join()