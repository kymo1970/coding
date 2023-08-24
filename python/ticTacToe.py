from re import L
from tkinter import *
import random


def nextTurn(row, column):
    
    global player

    if buttons[row][column]["text"] == "" and checkWinner() is False:
        if player == players[0]:
            buttons[row][column]["text"] = player

            if checkWinner() is False:
                player = players[1]
                lblPlayersTurn.config(text = (players[1] + "'s turn!"))

            elif checkWinner() is True:
                lblPlayersTurn.config(text = players[0] + " wins")

            elif checkWinner() == "Cats Game":
                lblPlayersTurn.config(text = "Cats Game")
            
        else:

            buttons[row][column]["text"] = player

            if checkWinner() is False:
                player = players[0]
                lblPlayersTurn.config(text = (players[0] + "'s turn!"))

            elif checkWinner() is True:
                lblPlayersTurn.config(text = players[1] + " wins")

            elif checkWinner() == "Cats Game!":
                lblPlayersTurn.config(text = "Cats Game")

def checkWinner():
    
    for row in range(3):
        if buttons[row][0]["text"] == buttons[row][1]["text"] == buttons[row][2]["text"] != "":
            return True

    for column in range(3):
        if buttons[0][column]["text"] == buttons[1][column]["text"] == buttons[2][column]["text"] != "":
            return True

    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        return True

    elif buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        return True

    elif emptySpaces() is False:
        return "Cats Game!"

    else:
        return False

def emptySpaces():
    pass


def newGame():
    pass


w = Tk()
w.title("Kymo's Designs - Tic-Tac-Toe")
w.geometry("400x500")
w.config(bg = "#000000")

players = ["@", "$"]
player = random.choice(players)

buttons = [[0, 0, 0], 
           [0, 0, 0], 
           [0, 0, 0]]

lblPlayersTurn = Label(text = player + "'s turn", 
                        font = ("Z003", 40), 
                        bg = "#000000", 
                        fg = "#00ff00")
lblPlayersTurn.pack(side = "top")

f = Frame(w)
f.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(f, text = "", 
                                        font = ("Z003", 40), width = 4, 
                                        height = 2, bg = "#00ff00", fg = "#000000", 
                                        activebackground = "#000000", 
                                        activeforeground = "#00ff00", 
                                        command = lambda row = row, 
                                        column = column: nextTurn(row, column))

        buttons[row][column].grid(row = row, column = column)

btnReset = Button(text = "Reset", 
                    font = ("Z003", 20), 
                    bg = "#000000", 
                    fg = "#00ff00", 
                    activebackground = "#00ff00", 
                    activeforeground = "#000000", 
                    command = newGame)
btnReset.pack(side = "bottom", pady=10)

w.mainloop()

