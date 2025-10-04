import pyautogui
import time
import threading
import keyboard
import random

# Safety feature
pyautogui.FAILSAFE = True

# Flag to control clicking
running = False
click_duration = 0.003  # Duration of each click in seconds

# Helper function for human-like mouse movement
def move_mouse_human(x, y):
    # Add small random offset to simulate natural movement
    offset_x = random.randint(-2, 2)
    offset_y = random.randint(-2, 2)
    # Move to target position smoothly
    pyautogui.moveTo(x + offset_x, y + offset_y, duration=random.uniform(0.1, 0.3))

def click_sequence():
    global running
    while running:
        # Step 1: Right click at golden carrot menu (1013, 377), 1s delay
        move_mouse_human(1013, 377)
        pyautogui.rightClick(duration=click_duration)
        time.sleep(1)

        # Step 2: Left click at 64x buy (1069, 379), 1s delay, repeat 35 times
        for _ in range(35):
            if not running:
                return
            move_mouse_human(1069, 379)
            pyautogui.click(duration=click_duration)
            time.sleep(0.002)

        # Wait 1 seconds before Step 3
        if not running: return
        time.sleep(1)

        # Step 3: Left click at sacks (1034, 158), 1s delay
        move_mouse_human(1034, 158)
        pyautogui.click(duration=click_duration)
        time.sleep(0.7)

        # Step 4: Left click at store all (854, 457), 1s delay
        move_mouse_human(854, 457)
        pyautogui.click(duration=click_duration)
        time.sleep(0.7)

        # Step 5: Left click at exit menu (957, 463), 0.5s delay
        move_mouse_human(957, 463)
        pyautogui.click(duration=click_duration)
        time.sleep(0.5)

        # Step 6: Right click at npc (957, 463), 1.5s delay
        move_mouse_human(957, 463)
        pyautogui.rightClick(duration=click_duration)
        time.sleep(1)

        print("Sequence complete! Looping again...")

def toggle_clicker():
    global running
    running = not running
    if running:
        print("Auto-clicker started!")
        threading.Thread(target=click_sequence, daemon=True).start()
    else:
        print("Auto-clicker stopped!")

if __name__ == "__main__":
    print("Press Print Screen to start/stop the auto-clicker.")
    keyboard.add_hotkey('print screen', toggle_clicker)
    keyboard.wait()
