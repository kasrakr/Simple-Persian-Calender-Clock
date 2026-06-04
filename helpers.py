import tkinter as tk
from PIL import Image, ImageTk

def center_window(parent, child):
    parent.update_idletasks()
    child.update_idletasks()
    parent_x = parent.winfo_x()
    parent_y = parent.winfo_y()
    parent_width = parent.winfo_width()
    parent_height = parent.winfo_height()
    child_width = child.winfo_width()
    child_height = child.winfo_height()
    if child_width <= 1:
        child_width = child.winfo_reqwidth()
    if child_height <= 1:
        child_height = child.winfo_reqheight()
    x = parent_x + (parent_width // 2) - (child_width // 2)
    y = parent_y + (parent_height // 2) - (child_height // 2)
    child.geometry(f"+{x}+{y}")

def fit_image(image, max_width, max_height):
    img_width, img_height = image.size
    width_ratio = max_width / img_width
    height_ratio = max_height / img_height
    scale_factor = min(width_ratio, height_ratio)
    new_width = int(img_width * scale_factor)
    new_height = int(img_height * scale_factor)
    return image.resize((new_width, new_height), Image.Resampling.LANCZOS)