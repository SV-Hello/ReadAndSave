import threading
import tkinter as tk
import threading
import pyautogui
import sys

from tkinter import Canvas, Toplevel
from pynput import keyboard

class KeyboardHandler:
    def __init__(self, read_capture, root):
        self.running = True
        self.capturing = False
        
        self.read_capture = read_capture
        self.root = root
        self.overlay = None

        self.start_listening()

    def create_overlay(self):
            #Overlay
            self.overlay = Toplevel(self.root)
            self.overlay.title("Overlay")     
            
            self.overlay.attributes("-fullscreen", True)
            self.overlay.attributes("-topmost", True)
            self.overlay.attributes("-alpha", "0.5")
            self.overlay.config(bg="gray")

            self.canvas = Canvas(self.overlay, bg="black", highlightthickness=0)
            self.canvas.pack(fill=tk.BOTH, expand=True)
            
            self.overlay.overrideredirect(True)
            
            self.canvas.bind("<ButtonPress-1>", self.on_mouse_down)
            self.canvas.bind("<B1-Motion>", self.on_mouse_drag)
            self.canvas.bind("<ButtonRelease-1>", self.on_mouse_up)

    #MOUSE EVENTS
    def on_mouse_down(self, event):
        #print("Mouse down")
        self.start_x, self.start_y = event.x, event.y
        self.rect_id = self.canvas.create_rectangle(self.start_x, self.start_y, self.start_x, self.start_y,
                                                    outline="red", width=2, fill="red", stipple="gray25")
    
    def on_mouse_drag(self, event):
        #print("Mouse drag")
        self.end_x, self.end_y = event.x, event.y
        self.canvas.coords(self.rect_id, self.start_x, self.start_y, self.end_x, self.end_y)

    def on_mouse_up(self, event):
        #print("Mouse up")
        self.end_x, self.end_y = event.x, event.y
        threading.Thread(target=self.read_capture.capture, args=(self.start_x, self.start_y, self.end_x, self.end_y)).start()
        self.overlay.destroy()

    #KEYBIND EVENTS
    #Do capture
    def on_activate_capture(self):
        #print("Activate")
        self.create_overlay()

        #To prevent double-clicking erranous activation of keybinds
        pyautogui.keyUp('ctrlleft')
        pyautogui.keyUp('altleft')
        pyautogui.keyUp('s')

    #Exit program
    def on_activate_quit(self):
        #print("Quit")
        self.root.destroy()
        sys.exit("Program Shutdown")
        #self.running = False

    #Begin running of software
    def start_listening(self):
        #print("Listening...")

        listener = keyboard.GlobalHotKeys({
            '<ctrl>+<alt>+s':  self.on_activate_capture,
            '<ctrl>+<alt>+q': self.on_activate_quit})
        listener.start()

        