import tkinter as tk
from tkinter import simpledialog
import json

class UserInterface:
    def __init__(self, root):
        self.root = root

        self.root.title("Hotkey ScreenGrab")

        self.root.protocol("WM_DELETE_WINDOW", self.minimize_to_tray)

    def minimize_to_tray(self):
        self.root.withdraw()