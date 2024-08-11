import tkinter as tk
from tkinter import font as tkfont

class UserInterface:
    def __init__(self, root):
        self.root = root
        self.bold = tkfont.Font(weight="bold")

        #Name
        self.root.title("Hotkey ScreenGrab")

        #Dimensions
        self.root.minsize(400, 100)
        self.root.maxsize(400, 100)
        self.root.geometry("400x100+50+50")
        
        self.save_bar = tk.Frame(self.root, bg="lightgray", height=40)
        self.save_bar.pack(fill="x", side="top")

        self.save_label = tk.Label(self.save_bar, text="Ctrl + Alt + S to capture", bg="lightgray", fg="black", font=self.bold)
        self.save_label.pack(pady=10)

        self.quit_bar = tk.Frame(self.root, bg="gray", height=40)
        self.quit_bar.pack(fill="x", side="top")

        self.quit_label = tk.Label(self.quit_bar, text="Ctrl + Alt + Q to exit", bg="gray", fg="white", font=self.bold)
        self.quit_label.pack(pady=10)

        self.root.protocol("WM_DELETE_WINDOW", self.close_program)

    def close_program(self):
        #print("Quit")
        self.root.destroy()
