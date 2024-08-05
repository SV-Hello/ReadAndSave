#Imports
import pyautogui
import pytesseract
import tkinter as tk
import threading
import time
import os

from tkinter import Canvas
from pynput import keyboard
from PIL import Image
from pathlib import Path

class ReadCapture:
    def __init__(self, tesseract_cmd):
    
        pytesseract.pytesseract.tesseract_cmd = tesseract_cmd
    
        self.desktop_path = Path(os.environ['USERPROFILE']) / 'Desktop'



    def capture(self, start_x, start_y, end_x, end_y):
        print("Capture start")

        region = (min(start_x, end_x), min(start_y, end_y), 
                       abs(end_x - start_x), abs(end_y - start_y))
        

        #Extract text
        text = pytesseract.image_to_string(pyautogui.screenshot(region = region))
        
        #Save text
        textfile_name = "extracted_text.txt"
        with open(self.desktop_path / textfile_name, "a"  if os.path.isfile(self.desktop_path / textfile_name) else "w") as file:
            file.write("------------------------------------------\n\n")
            file.write(text + "\n")

        print("Extracted and saved.")
   