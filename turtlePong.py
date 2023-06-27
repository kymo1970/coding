'''
Created on Feb 12, 2022

@author: kymo1
'''

import turtle as t
import winsound


mw = t.Screen()
mw.title("Kymo's Designs - Pong in Turtle")
mw.bgcolor("black")
mw.setup(width = 1000, height = 500)
mw.tracer(0)

# Scores
scoreA = 0
scoreB = 0

# Paddle A
paddleA = t.Turtle()
paddleA.speed(0)
paddleA.shape("square")
paddleA.color("white")
paddleA.shapesize(stretch_wid = 5, stretch_len = 1)
paddleA.penup()
paddleA.goto(-450, 0)

# Paddle B
paddleB = t.Turtle()
paddleB.speed(0)
paddleB.shape("square")
paddleB.color("white")
paddleB.shapesize(stretch_wid = 5, stretch_len = 1)
paddleB.penup()
paddleB.goto(450, 0)

# Ball
ball = t.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("#ffffff")
ball.penup()
ball.goto(0, 0)
ball.dx = .25
ball.dy = .25

# Pen
pen = t.Turtle()
pen.speed(0)
pen.color("#ffffff")
pen.penup()
pen.hideturtle()
pen.goto(0, 200)
pen.write("Player A: 0  Player B: 0", align = "center", font = ("Courier", 24, "normal"))

# Move paddleA up.
def paddleAUp():
    
    if (paddleA.ycor() + 50) < 250:
        y = paddleA.ycor()
        y += 20
        paddleA.sety(y)
    else:
        paddleAYCor = paddleA.ycor()
        paddleA.sety(paddleAYCor)
    

# Move paddleA down.
def paddleADown():
    
    if (paddleA.ycor() - 50) > -250:
        y = paddleA.ycor()
        y -= 20
        paddleA.sety(y)
    else:
        paddleAYCor = paddleA.ycor()
        paddleA.sety(paddleAYCor)
    
    
# Move paddleB up.
def paddleBUp():
    
    if (paddleB.ycor() + 50) < 250:
        y = paddleB.ycor()
        y += 20
        paddleB.sety(y)
    else:
        paddleBYCor = paddleB.ycor()
        paddleB.sety(paddleBYCor)
    
    
# Move paddleB Down.
def paddleBDown():
    
    if (paddleB.ycor() - 50) > -250:
        y = paddleB.ycor()
        y -= 20
        paddleB.sety(y)
    else:
        paddleBYCor = paddleB.ycor()
        paddleB.sety(paddleBYCor)


mw.listen()
mw.onkeypress(paddleAUp, "w")
mw.onkeypress(paddleADown, "s")
mw.onkeypress(paddleBUp, "Up")
mw.onkeypress(paddleBDown, "Down")


# Game loop.
running = True

while running:
    mw.update()
    
    # Get the ball rolling.
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    # Check Borders.
    if ball.ycor() > 240:
        ball.sety(240)
        ball.dy *= -1
        winsound.PlaySound("click.wav", winsound.SND_ASYNC)
        
    if ball.ycor() < -240:
        ball.sety(-240)
        ball.dy *= -1
        winsound.PlaySound("click.wav", winsound.SND_ASYNC)
        
    if ball.xcor() > 490:
        ball.goto(0, 0)
        ball.dx *= -1
        scoreA += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(scoreA, scoreB), align = "center", font = ("Courier", 24, "normal"))
        #winsound.PlaySound("click.wav", winsound.SND_ASYNC)
        
    if ball.xcor() < -490:
        ball.goto(0, 0)
        ball.dx *= -1
        scoreB += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(scoreA, scoreB), align = "center", font = ("Courier", 24, "normal"))
        #winsound.PlaySound("click.wav", winsound.SND_ASYNC)

    if ball.xcor() > 440 and ball.xcor() < 450 and (ball.ycor() < paddleB.ycor() + 40 and ball.ycor() > paddleB.ycor() - 40):
        ball.setx(440)
        ball.dx *= -1
        winsound.PlaySound("click.wav", winsound.SND_ASYNC)
        
    if ball.xcor() < -440 and ball.xcor() > -450 and (ball.ycor() < paddleA.ycor() + 40 and ball.ycor() > paddleA.ycor() - 40):
        ball.setx(-440)
        ball.dx *= -1
        winsound.PlaySound("click.wav", winsound.SND_ASYNC)
        
        
        
        
        
        
        