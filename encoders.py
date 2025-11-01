import os
import base64
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw() # Hides the main window

file_path = filedialog.askopenfilename(
        title="Select a file",
        initialdir=".",  # Optional: starting directory
        filetypes=(("jpeg", "*.jpeg"), ("Jpg", "*.jpg*"), ("png","*.png")) # Optional: file type filters
    )

with open(file_path, "rb") as image_file:
    base64_string = base64.b64encode(image_file.read()).decode('utf-8')
with open("return.txt", "w") as image_file:
    image_file.write(base64_string)