#!/usr/bin/env python3

from PIL import ImageGrab
from tkinter import *
import tkinter as tk
import pyperclip
import os

script_dir = os.path.dirname(os.path.realpath(__file__))
script_path = os.path.join(script_dir, "picker.py")

def close_window(event=None):
    main.destroy()

main = Tk()
main.title("Picker")
main.geometry("200x200")
main.resizable(0, 0)
main.attributes('-topmost', True)

button = tk.Button(main, text = "Press spacebar")
button.grid(sticky = tk.NSEW)

canvas = tk.Canvas(main, width = 200, height = 200)
canvas.grid(sticky = tk.NSEW)

pic = ImageGrab.grab()

def color():
    x, y = main.winfo_pointerx(), main.winfo_pointery()
    r, g, b = pic.getpixel((x, y))
    hue = f"#{r:02x}{g:02x}{b:02x}"
    button.config(text = f"{x}, {y} = {hue}")
    canvas["background"] = hue
    pyperclip.copy(hue)

button["command"] = color
button.focus_force()

# Close the program with Ctrl+C
main.bind('<Control-c>', close_window)

main.mainloop()