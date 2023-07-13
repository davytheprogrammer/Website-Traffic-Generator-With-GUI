import pyautogui
import random
import time

# Get the screen size
screen_width, screen_height = pyautogui.size()


# Generate random mouse movements
def move_mouse_randomly():
    while True:
        # Generate random coordinates within the screen boundaries
        x = random.randint(0, screen_width)
        y = random.randint(0, screen_height)

        # Move the mouse to the random coordinates
        pyautogui.moveTo(x, y, duration=0.7)

        # Pause for a random duration
        time.sleep(random.uniform(0.5, 2.5))


# Start moving the mouse randomly
move_mouse_randomly()
