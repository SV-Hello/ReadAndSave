#Imports
import pyautogui
import pytesseract
import tkinter as tk
import threading
import time

from tkinter import Canvas
from pynput import keyboard
from PIL import Image

#Path to Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

class ReadAndSave:
    def __init__(self):
        #Variable Init

        #For capturing
        self.start_x = self.start_y = self.end_x = self.end_y = None
        self.region = None
        self.capture_mode = True

        #For overlay
        self.overlay = None
        self.canvas = None
        self.root = None

    def create_overlay(self):
        #Overlay
        self.root = tk.Tk()
        self.root.attributes("-fullscreen", True)
        self.root.attributes("-topmost", True)
        #self.root.attributes("-transparentcolor", "black")
        self.root.attributes("-alpha", "0.5")
        self.root.config(bg="gray")

        self.canvas = Canvas(self.root, bg="black", highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        
        self.canvas.bind("<ButtonPress-1>", self.on_mouse_down)
        self.canvas.bind("<B1-Motion>", self.on_mouse_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_mouse_up)

    def on_mouse_down(self, event):
        print("Mouse down")
        self.start_x, self.start_y = event.x, event.y
        self.rect_id = self.canvas.create_rectangle(self.start_x, self.start_y, self.start_x, self.start_y,
                                                    outline="red", width=2, fill="red", stipple="gray25")
    
    def on_mouse_drag(self, event):
        print("Mouse drag")
        self.end_x, self.end_y = event.x, event.y
        self.canvas.coords(self.rect_id, self.start_x, self.start_y, self.end_x, self.end_y)

    def on_mouse_up(self, event):
        print("Mouse up")
        self.end_x, self.end_y = event.x, event.y
        threading.Thread(target=self.capture_and_extract, args=(self.start_x, self.start_y, self.end_x, self.end_y)).start()
        time.sleep(0.001)
        self.root.destroy()


    #Self-explanatory
    def capture_and_extract(self, start_x, start_y, end_x, end_y):
        #Take screenshot
        print("Capture start")
        region = (min(start_x, end_x), min(start_y, end_y), 
                       abs(end_x - start_x), abs(end_y - start_y))

        screenshot = pyautogui.screenshot(region = region)

        #Save ss
        screenshot_path = "r&s_screenshot.png"
        screenshot.save(screenshot_path)

        #Extract text
        text = pytesseract.image_to_string(Image.open(screenshot_path))

        #Save text
        with open("extracted_text.txt", "a") as file:
            file.write("------------------------------------------\n\n")
            file.write(text + "\n")

        print("Extracted and saved.")

    #Excute C&A
    def on_activate_capture(self):
        print("Click and Drag...")
        self.create_overlay()
        self.root.mainloop()

    #Exit
    def on_activate_quit(self):
        print("Quitting...")
        self.capture_mode = False
    

#Main
def main():
    print("Start!")
    read_and_save = ReadAndSave()

    listener = keyboard.GlobalHotKeys({
        '<ctrl>+<alt>+s': read_and_save.on_activate_capture,
        '<ctrl>+<alt>+q': read_and_save.on_activate_quit})
    listener.start()

    while read_and_save.capture_mode:
        pass

if __name__ == "__main__":
    main()