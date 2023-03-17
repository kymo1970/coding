from tkinter import *
from time import *


def update():
    currentTime = strftime("%I:%M:%S %p")
    lblTime.config(text = currentTime)
    currentDay = strftime("%A")
    lblDay.config(text = currentDay)
    currentDate = strftime("%B %d, %Y")
    lblDate.config(text = currentDate)

    w.after(1000, update)
    

w = Tk()
w.title("Kymo's Designs - Clock")
w.geometry("400x195")

lblTime = Label(w, font = ("Z003", 50), fg = "#00ff00", bg = "#000000", width = 400)
lblTime.pack()

lblDay = Label(w, font = ("Z003", 50), fg = "#00ff00", bg = "#000000", width = 400)
lblDay.pack()

lblDate = Label(w, font = ("Z003", 35), fg = "#00ff00", bg = "#000000", width = 400)
lblDate.pack()

update()

w.mainloop()