'''
Created on Mar 28, 2022

@author: kymo1
'''

from tkinter import Tk, Canvas, Label
import time


WIDTH = 1000
HEIGHT = 500

mw = Tk()
mw.title("Kymo's Designs - Pong in Canvas")
#mw.geometry("1000x500")

#mw.bind("<w>", movePadAUp)
#mw.bind("<s>", movePadADown)
#mw.bind("<Up>", movePadBUp)
#mw.bind("<Down>", movePadBDown)


c = Canvas(mw, bg = "black", width = WIDTH, height = HEIGHT)
c.pack()

#paddleA = c.create_rectangle(20, 200, 40, 300, fill = "white")
#paddleB = c.create_rectangle(980, 200, 960, 300, fill = "white")
ball = c.create_oval(490, 240, 510, 260, fill = "white")

running = True
x = 2
y = 2

while running:
    coordsBall1 = c.coords(ball)
    print(coordsBall1)
    if coordsBall1[1] <= 0 or coordsBall1[3] >= HEIGHT:
        y = -y
        c.move(ball, x, y)
    elif coordsBall1[0] <= 0 or coordsBall1[2] >= WIDTH:
        x = -x
        c.move(ball, x, y)
    else:
        c.move(ball, x, y)
    
    c.update()
    mw.update()
    time.sleep(.01)


mw.mainloop()