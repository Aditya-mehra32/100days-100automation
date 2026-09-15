import pyautogui
from datetime import datetime
import os

# Create screenshots folder
folder = "screenshots"
os.makedirs(folder, exist_ok=True)

# Take screenshot
screenshot = pyautogui.screenshot()

# Generate filename
filename = datetime.now().strftime("screenshot_%Y-%m-%d_%H-%M-%S.png")

# Save screenshot
path = os.path.join(folder, filename)
screenshot.save(path)

print(f"Screenshot saved: {path}")
