'''
Created on Mar 24, 2022

@author: James Eyrich @ Kymo's Designs
'''

from tkinter import Tk, Canvas, Label
import time
import random

WIDTH = 1000
HEIGHT = 500
BALL_DIAMETER = 20
PADDLE_WIDTH = 20
PADDLE_HEIGHT = 100
ballX = ((WIDTH / 2) - (BALL_DIAMETER / 2))
ballY = ((HEIGHT / 2) - (BALL_DIAMETER / 2))
PADDLE_A_X = 40
paddleAY = (HEIGHT / 2) - 50

PADDLE_B_X = 960
paddleBY = (HEIGHT / 2) - 50

xSpeedPos = [2, 3, 4, 5, 6, 7, 8, 9]
xSpeedNeg = [-2, -3, -4, -5, -6, -7, -8, -9]
ySpeedPos = [0, 1, 2, 3, 4]
ySpeedNeg = [0, -1, -2, -3, -4]

x = random.choice(xSpeedPos)
y = random.choice(ySpeedPos)


def movePadAUp(event):
    coordsPaddleA = c.coords(paddleA)
    print(coordsPaddleA)
    if coordsPaddleA[1] <= 0:
        c.move(paddleA, 0, 0)
    else:
        c.move(paddleA, 0, -10)

def movePadADown(event):
    coordsPaddleA = c.coords(paddleA)
    if coordsPaddleA[3] >= HEIGHT:
        c.move(paddleA, 0, 0)
    else:
        c.move(paddleA, 0, 10)

def movePadBUp(event):
    coordsPaddleB = c.coords(paddleB)
    if coordsPaddleB[1] <= 0:
        c.move(paddleB, 0, 0)
    else:
        c.move(paddleB, 0, -10)

def movePadBDown(event):
    coordsPaddleB = c.coords(paddleB)
    if coordsPaddleB[3] >= HEIGHT:
        c.move(paddleB, 0, 0)
    else:
        c.move(paddleB, 0, 10)

mw = Tk()
mw.title("Kymo's Designs - Pong in Canvas")

player1Score = 0
player2Score = 0

lblPlayer1Score = Label(mw, text = f"Player1:  {player1Score}", font = ("Harrington", 20))
lblPlayer1Score.grid(row = 0, column = 0)

lblPlayer2Score = Label(mw, text = f"Player2:  {player2Score}", font = ("Harrington", 20))
lblPlayer2Score.grid(row = 0, column = 1)

mw.bind("<w>", movePadAUp)
mw.bind("<s>", movePadADown)
mw.bind("<Up>", movePadBUp)
mw.bind("<Down>", movePadBDown)


c = Canvas(mw, bg = "black", width = WIDTH, height = HEIGHT)
c.grid(row = 1, column = 0, columnspan = 2)

paddleA = c.create_rectangle(PADDLE_A_X, paddleAY, (PADDLE_A_X + PADDLE_WIDTH), (paddleAY + PADDLE_HEIGHT), fill = "white")
paddleB = c.create_rectangle(PADDLE_B_X, paddleBY, (PADDLE_B_X - PADDLE_WIDTH), (paddleBY + PADDLE_HEIGHT), fill = "white")
ball = c.create_oval(ballX, ballY, (ballX + BALL_DIAMETER), (ballY + BALL_DIAMETER), fill = "white")


running = True

while running:
    coordsBall = c.coords(ball)
    #print(coordsBall)
    
    # Check colissions with window frame.
    if coordsBall[1] <= 0 and x > 0:
        x = random.choice(xSpeedPos)
        y = random.choice(ySpeedPos)
        c.move(ball, x, y)
    elif coordsBall[3] >= HEIGHT and x > 0:
        x = random.choice(xSpeedPos)
        y = random.choice(ySpeedNeg)
        c.move(ball, x, y)
    elif coordsBall[1] <= 0 and x < 0:
        x = random.choice(xSpeedNeg)
        y = random.choice(ySpeedPos)
        c.move(ball, x, y)
    elif coordsBall[3] >= HEIGHT and x < 0:
        x = random.choice(xSpeedNeg)
        y = random.choice(ySpeedNeg)
        c.move(ball, x, y)
    else:
        c.move(ball, x, y)
        
    if coordsBall[2] >= WIDTH:
        c.delete(ball)
        ball = c.create_oval(ballX, ballY, (ballX + BALL_DIAMETER), (ballY + BALL_DIAMETER), fill = "white")
        x = random.choice(xSpeedPos)
        y = random.choice(ySpeedPos)
        c.move(ball, x, y)
        player1Score += 1
        lblPlayer1Score.config(text = f"Player 1:  {player1Score}", font = ("Harrington", 20))

        
    elif coordsBall[0] <= 0:
        c.delete(ball)
        ball = c.create_oval(ballX, ballY, (ballX + BALL_DIAMETER), (ballY + BALL_DIAMETER), fill = "white")
        x = random.choice(xSpeedPos)
        y = random.choice(ySpeedPos)
        c.move(ball, x, y)
        player2Score += 1
        lblPlayer2Score.config(text = f"Player 2:  {player2Score}", font = ("Harrington", 20))
        
    # Check colissions with paddles.
    # Paddle a
    coordsPaddleA = c.coords(paddleA)
    if coordsBall[0] <= (coordsPaddleA[2]) and coordsBall[2] >= coordsPaddleA[0] and (coordsBall[1] <= (coordsPaddleA[3]) and coordsBall[3] >= coordsPaddleA[1]):
        x = random.choice(xSpeedPos)
        y = random.choice(ySpeedPos)
        c.move(ball, x, y)
        
    coordsPaddleB = c.coords(paddleB)
    if coordsBall[2] >= (coordsPaddleB[0]) and coordsBall[0] <= coordsPaddleB[2] and (coordsBall[1] <= (coordsPaddleB[3]) and coordsBall[3] >= coordsPaddleB[1]):
        x = random.choice(xSpeedNeg)
        y = random.choice(ySpeedPos)
        c.move(ball, x, y)

    c.update()
    mw.update()
    time.sleep(.02)

mw.mainloop()

