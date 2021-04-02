from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from tkinter import *
import time

class ObjectivelyBetterTkWindow(Tk):
    def __init__(self):
        super().__init__()
        self.r, self.g, self.b = 255, 0, 0
        self.dr, self.dg, self.db = 0, 1, 0

    def mainloop(self, n=0):
        if self.r >= 255 and self.g >= 255:
            self.dr, self.dg, self.db = -1, 0, 0
        elif self.r >= 255 and self.b >= 255:
            self.dr, self.dg, self.db = 0, 0, -1
        elif self.r >= 255 and self.b == 0:
            self.dr, self.dg, self.db = 0, 1, 0
        elif self.g >= 255 and self.b >= 255:
            self.dr, self.dg, self.db = 0, -1, 0
        elif self.g >= 255 and self.r== 0:
            self.dr, self.dg, self.db = 0, 0, 1
        elif self.b >= 255 and self.g == 0:
            self.dr, self.dg, self.db = 1, 0, 0
        self.r += self.dr
        self.g += self.dg
        self.b += self.db
        print(self.r, self.g, self.b)
        super().mainloop(n=n)

    def get_rgb(self):
        """[summary]

        Returns:
            tuple: red, green, blue values
        """
        return self.r, self.g, self.b

def search_results():
    pass

def rgb_to_hex(rgb):
    """changes rgb values to hex

    Args:
        rgb (tuple): tuple of red, green, and blue

    Returns:
        string: hex value
    """
    r, g, b = rgb
    return f"#{r:02x}{g:02x}{b:02x}"

window = ObjectivelyBetterTkWindow()
window.geometry("450x200")
search = Label(window, text = "type search stuff here", font = ("Comic Sans MS", 15))
search.place(x = 10, y = 10)

entries = []
entries.append(Entry(window))
for i in range(len(entries)):
    entry = entries[i]
    entry.place(x = 250, y = i*10 + 10)

search_button = Button(window, text = "search", command = search_results, width = 12, bg = rgb_to_hex(window.get_rgb()))
search_button.place(x = 150, y = 150)

window.mainloop()