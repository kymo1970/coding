from tkinter import *
from time import *

HEIGHT = 500
WIDTH = 1000
posXVelocity = [1, 2, 3, 4, 5, 6, 7, 8, 9]
negXVelocity = [-1, -2, -3, -4, -5, -6, -7, -8, -9]
posYVelocity = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
negYVelocity = [0, -1, -2, -3, -4, -5, -6, -7, -8, -9]
ballSize = 20
ballX = (WIDTH / 2 - ballSize / 2)
ballY = (HEIGHT / 2 - ballSize / 2)
paddleAWidth, paddleBWidth = 20, 20
paddleAHeight, paddleBHeight = 100, 100
positionX, positionY = 0, 0

def paddleAUp(event):
    padACoords = c.coords(paddleA)
    if padACoords[1] > 0:
        c.move(paddleA, 0, -10)
    else:
        c.move(paddleA, 0, 0)

def paddleBUp(event):
    padBCoords = c.coords(paddleB)
    if padBCoords[1] > 0:
        c.move(paddleB, 0, -10)
    else:
        c.move(paddleB, 0, 0)

def paddleADown(event):
    padACoords = c.coords(paddleA)
    if padACoords[3] < HEIGHT:
        c.move(paddleA, 0, 10)
    else:
        c.move(paddleA, 0, 0)

def paddleBDown(event):
    padBCoords = c.coords(paddleB)
    if padBCoords[3] < HEIGHT:
        c.move(paddleB, 0, 10)
    else:
        c.move(paddleB, 0, 0)


w = Tk()
w.title("Kymo's Designs - Testing Python")

w.bind("<w>", paddleAUp)
w.bind("<Up>", paddleBUp)
w.bind("<s>", paddleADown)
w.bind("<Down>", paddleBDown)

c = Canvas(bg="#000000")
c.config(width=WIDTH, height=HEIGHT)
c.pack()

paddleA = c.create_rectangle(positionX + 50, 
                    positionY + HEIGHT / 2 - paddleAHeight / 2, 
                    (positionX + 50) + paddleAWidth, 
                    positionY + HEIGHT / 2 - paddleAHeight / 2 + paddleAHeight, 
                    fill="#ffffff")

paddleB = c.create_rectangle(WIDTH - 50, 
                    positionY + HEIGHT / 2 - paddleBHeight / 2, 
                    (WIDTH - 50) - paddleBWidth, 
                    positionY + HEIGHT / 2 - paddleBHeight / 2 + paddleBHeight, 
                    fill="#ffffff")

ball = c.create_oval(ballX, 
                    ballY, 
                    ballX + ballSize, 
                    ballY + ballSize, 
                    fill = "#ffffff")


running = True
#while running:
#     c.update()

w.mainloop()