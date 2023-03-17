'''

Program: Dice Adventures
Date: 9/3/2022
Author: James Eyrich for Kymo's Designs

'''

from tkinter import *
import random
import time


myDice = ["\u2680", "\u2681", "\u2682", "\u2683", "\u2684", "\u2685"]

def rollDice():

    shake = 75
    i = 0
    while(i <= shake):
        #Pick 2 random dice.
        die1 = random.choice(myDice)
        die2 = random.choice(myDice)

        #Update the die labels.
        lblDie1.config(text = die1)
        lblDie2.config(text = die2)
        i += 1
        mw.update()
        time.sleep(.01)    


mw = Tk()
mw.title("Dice Adventures - Kymo's Designs")
mw.geometry("500x500")

f1 = Frame(mw)
f1.grid(row = 0, column = 0)

f2 = Frame(mw)
f2.grid(row = 0, column = 1)

f3 = Frame(mw)
f3.grid(row = 1, column = 0, columnspan = 2)


lblDie1 = Label(f1, text = "", font = ("Helvitica", 50))
lblDie1.pack()

lblDie2 = Label(f2, text = "", font = ("Helvitica", 50))
lblDie2.pack()

btnRollDice = Button(f3, text = "Roll Them Bones", command = rollDice)
btnRollDice.pack(anchor = S)


mw.mainloop()

