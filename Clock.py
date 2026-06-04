import tkinter as tk
import datetime
import jdatetime
import requests
from PIL import Image, ImageTk
from io import BytesIO
from helpers import center_window, fit_image

def update():
    current = datetime.datetime.now().strftime("%H:%M:%S")
    label_clock.config(text=current)
    current1 = jdatetime.datetime.now().strftime("%Y/%m/%d")
    label_date_shamsi.config(text=current1)
    current2 = datetime.datetime.now().strftime("%Y/%m/%d")
    label_date_miladi.config(text=current2)

    current =jdatetime.date.today().strftime("%A %d %B %Y")
    label_date_f.config(text=current)

    window.after(1000, update)


def luck() :
    url = "https://api.thecatapi.com/v1/images/search"
    response = requests.get(url)
    data = response.json()
    for i in data :
        imageurl = i["url"]
    img_response = requests.get(imageurl, timeout=10)
    img_data = BytesIO(img_response.content)
    img = Image.open(img_data)
    img_window = tk.Toplevel(window)
    img_window.title("Mewo Image")
    tk_img = ImageTk.PhotoImage(img)
    label = tk.Label(img_window, image=tk_img)
    label.image = tk_img
    label.pack()


window = tk.Tk()
window.title("Persian Calender")
window.geometry("500x500")

window.configure(background="#0F172A")
window.resizable(width=False, height=False)
icon = tk.PhotoImage(file="cat.png")
window.iconphoto(True, icon)

center_frame = tk.Frame(window, bg="#0F172A")
center_frame.pack(expand=True)


label_clock = tk.Label(
    center_frame,
    font=("2  Fantezy", 50, "bold"),
    background="#0F172A",
    foreground="#38BDF8",
    cursor="heart",
)
label_clock.pack(pady=10)


label_date_f = tk.Label(
    center_frame,
    font=("Consolas", 15, "bold"),
    background="#0F172A",
    foreground="#F8FAFC",
)
label_date_f.pack(pady=5)


label_date_shamsi = tk.Label(
    center_frame,
    font=("2  Fantezy", 30, "bold"),
    background="#0F172A",
    foreground="#abadaf",
)
label_date_shamsi.pack(pady=5)


label_date_miladi = tk.Label(
    center_frame,
    font=("Consolas", 15, "bold"),
    background="#0F172A",
    foreground="#797b7d",
)
label_date_miladi.pack(pady=0)


button_luck = tk.Button(
    center_frame,
    text="میوشانس",
    font=("Calibri", 13, "bold"),
    pady=8,
    padx=8,
    background="#1E293B",
    foreground="#818CF8",
    relief="groove",
    bd=0,
    command=luck
)
button_luck.pack(pady=10)


update()
window.mainloop()