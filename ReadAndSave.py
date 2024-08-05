#Imports
import pyautogui
import pytesseract
from pynput import keyboard, mouse
from PIL import Image

#Path to Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

#Variable Init
start_x = start_y = end_x = end_y = None
capture_mode = True

#Click and Drag Method
def on_click(x, y, button, pressed):
    global start_x, start_y, end_x, end_y

    if button == mouse.Button.left:
        #Start Point
        if pressed:
            start_x, start_y = x, y
        #End Point
        else:
            end_x, end_y = x, y

            region = (min(start_x, end_x), min(start_y, end_y),
                      abs(end_x - start_x), abs(end_y - start_y))

            capture_and_extract(region)

            return False

#Self-explanatory
def capture_and_extract(region):
    #Take screenshot
    screenshot = pyautogui.screenshot(region = region)

    #Save ss
    screenshot_path = "r&s_screenshot.png"
    screenshot.save(screenshot_path)

    #Extract text
    text = pytesseract.image_to_string(Image.open(screenshot_path))

    #Save text
    with open("extracted_text.txt", "a") as file:
        file.write(text + "\n")

    print("Extracted and saved.")

#Excute C&A 
def on_activate_capture():
    print("Click and Drag...")
    mouse_listener = mouse.Listener(on_click = on_click)
    mouse_listener.start()

#Exit
def on_activate_quit():
    global capture_mode
    print("Quitting...")
    capture_mode = False
    

#Main
listener = keyboard.GlobalHotKeys({
    '<ctrl>+<alt>+s': on_activate_capture,
    '<ctrl>+<alt>+q': on_activate_quit})
listener.start()

while capture_mode:
    pass