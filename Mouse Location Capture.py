import pyautogui
import keyboard

counter = 1

print("Press 'Print Screen' to capture mouse position. Press 'Esc' to exit.")

while True:
    if keyboard.is_pressed("print screen"):  # Detect Print Screen key
        x, y = pyautogui.position()  # Get current mouse position
        print(f"{counter}. X={x} , Y={y}")
        counter += 1
        keyboard.wait("print screen")  # Prevent multiple captures on one press

    if keyboard.is_pressed("esc"):  # Exit when Esc is pressed
        print("Exiting...")
        break
