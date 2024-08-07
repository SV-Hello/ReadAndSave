import threading
import tkinter as tk
import threading
import pyautogui

from tkinter import Canvas
from pynput import keyboard

class KeyboardHandler:
    def __init__(self, read_capture, root):
        self.running = True
        self.capturing = False
        
        self.read_capture = read_capture
        self.root = root

    def create_overlay(self):
            #Overlay
            self.root = tk.Tk()
            self.root.attributes("-fullscreen", True)
            self.root.attributes("-topmost", True)
            self.root.attributes("-alpha", "0.5")
            self.root.config(bg="gray")

            self.canvas = Canvas(self.root, bg="black", highlightthickness=0)
            self.canvas.pack(fill=tk.BOTH, expand=True)
            
            self.canvas.bind("<ButtonPress-1>", self.on_mouse_down)
            self.canvas.bind("<B1-Motion>", self.on_mouse_drag)
            self.canvas.bind("<ButtonRelease-1>", self.on_mouse_up)

    #MOUSE EVENTS
    def on_mouse_down(self, event):
        print("Mouse down")
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
        self.root.destroy()

    #KEYBIND EVENTS
    #Do capture
    def on_activate_capture(self):
        print("Activate")
        self.create_overlay()
        self.root.mainloop()

        #To prevent double-clicking erranous activation of keybinds
        pyautogui.keyUp('ctrlleft')
        pyautogui.keyUp('altleft')
        pyautogui.keyUp('s')

    #Exit program
    def on_activate_quit(self):
        print("Quit")
        self.running = False

    #Begin running of software
    def start_listening(self):
        listener = keyboard.GlobalHotKeys({
            '<ctrl>+<alt>+s':  self.on_activate_capture,
            '<ctrl>+<alt>+q': self.on_activate_quit})
        listener.start()

        while self.running:
            pass

        