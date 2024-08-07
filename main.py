# SV-Hello
# 08/05/2024

import tkinter as tk

from KeyboardHandler import KeyboardHandler
from ReadCapture import ReadCapture
#from UserInterface import UserInterface

def main():
    tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    #root = tk.Tk()

    #ui = UserInterface(root)
    read_capture = ReadCapture(tesseract_cmd)
    handler = KeyboardHandler(read_capture)
    
    print("Begin.")
    handler.start_listening()
    #print("HERE")
    #root.mainloop()

if __name__ == "__main__":
    main()