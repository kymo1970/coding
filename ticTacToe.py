'''
Created on Feb 6, 2022

@author: kymo1
'''

from tkinter import *
import random


def nextTurn(row, col):
    global player
    
    if gameSpaces[row][col]["text"] == "" and checkWinner() is False:
        
        if player == players[0]:
            
            gameSpaces[row][col]["text"] = player
            gameSpaces[row][col].config(bg = "purple")
            
            if checkWinner() is False:
                player = players[1]
                lblTurn.config(text = player + "'s turn")
                
            elif checkWinner() is True:
                lblTurn.config(text = player + " wins", bg = "purple", fg = "green")
                
            elif checkWinner() == "Cat":
                lblTurn.config(text = "Cats Game!", bg = "red", fg = "blue")
                for row in range(3):
                    for col in range(3):
                        gameSpaces[row][col].config(bg = "blue", fg = "red")
                
        else:
            
            gameSpaces[row][col]["text"] = player
            gameSpaces[row][col].config(bg = "green")
            
            if checkWinner() is False:
                player = players[0]
                lblTurn.config(text = player + "'s turn")
                
            elif checkWinner() is True:
                lblTurn.config(text = player + " wins", bg ="green", fg = "purple")
                
            elif checkWinner() == "Cat":
                lblTurn.config(text = "Cats Game!", bg = "red", fg = "blue")
                for row in range(3):
                    for col in range(3):
                        gameSpaces[row][col].config(bg = "blue", fg = "red")
    

def checkWinner():
    
    for row in range(3):
        if gameSpaces[row][0]["text"] == gameSpaces[row][1]["text"] == gameSpaces[row][2]["text"] != "":
            return True

    for col in range(3):
        if gameSpaces[0][col]["text"] == gameSpaces[1][col]["text"] == gameSpaces[2][col]["text"] != "":
            return True
    
    if gameSpaces[0][0]["text"] == gameSpaces[1][1]["text"] == gameSpaces[2][2]["text"] != "":
        return True
        
    elif gameSpaces[2][0]["text"] == gameSpaces[1][1]["text"] == gameSpaces[0][2]["text"] != "":
        return True
        
    elif emptySpaces() is False:
        return "Cat"
    
    else:
        return False


def emptySpaces():
    spaces = 9
    
    for row in range(3):
        for col in range(3):
            if gameSpaces[row][col]["text"] != "":
                spaces -= 1
                
    if spaces == 0:
        return False
    
    else:
        return True


def newGame():
    
    global player
    
    player = random.choice(players)
    
    lblTurn.config(text = player + "'s turn", bg = "#f0f0f0", fg = "#000000")
    
    for row in range(3):
        for col in range(3):
            gameSpaces[row][col].config(text = "", bg = "#f0f0f0")


w = Tk()
w.title("Kymo's Designs-Tic Tac Toe")

players = ["$", "@"]
player = random.choice(players)
gameSpaces = [[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]]

lblTurn = Label(text = player + "'s turn!", font = ("Harrington", 40))
lblTurn.pack(side = "top")

btnReset = Button(text = "New Game", font = ("Harrington", 20), command = newGame)
btnReset.pack(side = "bottom")

f = Frame(w)
f.pack()

for row in range(3):
    for col in range(3):
        gameSpaces[row][col] = Button(f, text = "",
                                      font = ("Harrington", 40),
                                      width = 5, height = 2,
                                      command = lambda row = row,
                                      col = col: nextTurn(row, col))
        gameSpaces[row][col].grid(row = row, column = col)


w.mainloop()

