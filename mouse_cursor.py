import pyautogui
import math
import time

# Function to move the mouse in a circular pattern
def move_mouse_infinite():
    screenWidth, screenHeight = pyautogui.size()  # Get screen resolution

    # Starting position
    x_center, y_center = screenWidth / 2, screenHeight / 2
    
    radius = 100  # Radius of the circle
    angle = 0  # Start angle

    while True:
        # Calculate new x, y based on the angle
        x = x_center + radius * math.cos(math.radians(angle))
        y = y_center + radius * math.sin(math.radians(angle))
        
        pyautogui.moveTo(x, y, duration=0.1)  # Move the mouse
        angle += 1  # Increment the angle to create continuous motion
        
        # Reset the angle to keep it within 0-360 degrees range
        if angle >= 360:
            angle = 0

        # Sleep for a short duration to avoid consuming too much CPU
        time.sleep(0.01)

# Start the infinite mouse movement
if __name__ == "__main__":
    move_mouse_infinite()
