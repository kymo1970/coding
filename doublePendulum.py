from tkinter import *
from math import *

HEIGHT = 1000
WIDTH = 1000
M1 = 20
M2 = 20
L1 = 200
L2 = 200
A1 = 0
A2 = 0

x1 = L1 * sin(A1)
y1 = L1 * cos(A1)
x2 = L2 * sin(A2)
y2 = L2 * cos(A2)
center = (WIDTH/2, HEIGHT/2)
x, y = center

mw = Tk()
mw.geometry("1000x1000")
c = Canvas()
c.config(width = 1000, height = 1000, bg = "black")
c.pack()
c.create_line(x, y, x, y+L1, fill="red", width=2)
c.create_line(x, y+L1, x, y+L1+L2, fill="red", width=2)
c.create_oval((x1-M1), (y1+L1) - (M1), (x1+M1), (y1+L1+M1), fill="green")
c.create_oval((x2-M1), (y2+L1+L2) - (M1), (x2+M1), (y2+L1+L2+M1), fill="green")

c.update()
mw.mainloop()