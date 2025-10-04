import win32api
import win32con
import pyautogui
import keyboard
import time
import threading

pyautogui.FAILSAFE = True
Delay = 0.5  # Total delay between clicks
clicking = False  # Tracks whether clicking is on or off
check_interval = 0.5  # Interval to check if Q was pressed

def click(x, y):
    pyautogui.moveTo(x, y, 0.5)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    time.sleep(0.003)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

def wait_with_interrupt(total_delay):
    """Sleep in small increments, checking if clicking was turned off."""
    elapsed = 0
    while elapsed < total_delay:
        if not clicking:  # Stop immediately if Q was pressed
            break
        time.sleep(check_interval)
        elapsed += check_interval

def click_loop():
    global clicking
    while True:
        if clicking:
            click(1014, 538)
            wait_with_interrupt(Delay)
            if not clicking: continue

            click(795, 434)
            wait_with_interrupt(Delay)
            if not clicking: continue

            click(1035, 206)
            wait_with_interrupt(Delay)
            if not clicking: continue

            click(856, 459)
            wait_with_interrupt(Delay)
            if not clicking: continue

            click(1110, 808)
            wait_with_interrupt(Delay)
        else:
            time.sleep(0.05)  # Sleep briefly to reduce CPU usage

def toggle_clicking():
    global clicking
    clicking = not clicking
    if clicking:
        print("Clicking started!")
    else:
        print("Clicking stopped!")

# Start clicking loop in a separate thread
threading.Thread(target=click_loop, daemon=True).start()

print("Press 'Q' to toggle clicking on/off immediately at any time.")

# Listen for Q key presses
keyboard.add_hotkey('q', toggle_clicking)

# Keep the script running
keyboard.wait()
