import tkinter as tk
import webbrowser

def open_link(event):
    webbrowser.open("https://disk.yandex.com.am/i/UqxI_ZO0rKP1kw")

root = tk.Tk()
root.title("Сердца")

canvas = tk.Canvas(root, width=400, height=200)
canvas.pack()

def draw_heart(x, y):
    canvas.create_polygon(x, y+35, x-30, y, x-80, y, x-80, y+90, x, y+150, x+80, y+90, x+80, y, x+30, y, fill="red", outline="black")

draw_heart(100, 50)

draw_heart(300, 50)

canvas.bind("<Button-1>", open_link)

root.mainloop()
