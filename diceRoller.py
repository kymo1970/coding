'''
Created on Mar 20, 2022

@author: kymo1
'''
import tkinter.constants as tc
from tkinter import Button, Entry, Label, Tk
import random


def btnClear(dieNum):
    if dieNum == "Die1":
        btnDie1.destroy()
        d1Number = 0
        d2Number = getNumber(d2)
        d3Number = getNumber(d3)
        d4Number = getNumber(d4)
    
        dieTotal = d1Number + d2Number + d3Number + d4Number
    
        lblTotal.config(text = dieTotal)
        lblDisplay.config(text = f"""You have chosen three die that total
{dieTotal} now choose an ability to put that roll into.""")
        
        btnStr = Button(mw, text = "Strength", font = ("Harrington", 20))
        btnStr.grid(row = 3, column = 2)
        
        btnInt = Button(mw, text = "Intelligence", font = ("Harrington", 20))
        btnInt.grid(row = 3, column = 3)
        
        btnDex = Button(mw, text = "Dexterity", font = ("Harrington", 20))
        btnDex.grid(row = 3, column = 4)
        
    if dieNum == "Die2":
        btnDie2.destroy()
        d1Number = getNumber(d1)
        d2Number = 0
        d3Number = getNumber(d3)
        d4Number = getNumber(d4)
    
        dieTotal = d1Number + d2Number + d3Number + d4Number
    
        lblTotal.config(text = dieTotal)
        lblDisplay.config(text = f"""You have chosen three die that total
{dieTotal} now choose an ability to put that roll into.""")
        
        btnStr = Button(mw, text = "Strength", font = ("Harrington", 20))
        btnStr.grid(row = 3, column = 2)
        
        btnInt = Button(mw, text = "Intelligence", font = ("Harrington", 20))
        btnInt.grid(row = 3, column = 3)
        
        btnDex = Button(mw, text = "Dexterity", font = ("Harrington", 20))
        btnDex.grid(row = 3, column = 4)
        
    if dieNum == "Die3":
        btnDie3.destroy()
        d1Number = getNumber(d1)
        d2Number = getNumber(d2)
        d3Number = 0
        d4Number = getNumber(d4)
    
        dieTotal = d1Number + d2Number + d3Number + d4Number
    
        lblTotal.config(text = dieTotal)
        lblDisplay.config(text = f"""You have chosen three die that total
{dieTotal} now choose an ability to put that roll into.""")
        
        btnStr = Button(mw, text = "Strength", font = ("Harrington", 20))
        btnStr.grid(row = 3, column = 2)
        
        btnInt = Button(mw, text = "Intelligence", font = ("Harrington", 20))
        btnInt.grid(row = 3, column = 3)
        
        btnDex = Button(mw, text = "Dexterity", font = ("Harrington", 20))
        btnDex.grid(row = 3, column = 4)

    if dieNum == "Die4":
        btnDie4.destroy()
        d1Number = getNumber(d1)
        d2Number = getNumber(d2)
        d3Number = getNumber(d3)
        d4Number = 0
    
        dieTotal = d1Number + d2Number + d3Number + d4Number
    
        lblTotal.config(text = dieTotal)
        lblDisplay.config(text = f"""You have chosen three die that total
{dieTotal} now choose an ability to put that roll into.""")
        
        btnStr = Button(mw, text = "Strength", font = ("Harrington", 20))
        btnStr.grid(row = 3, column = 2)
        
        btnInt = Button(mw, text = "Intelligence", font = ("Harrington", 20))
        btnInt.grid(row = 3, column = 3)
        
        btnDex = Button(mw, text = "Dexterity", font = ("Harrington", 20))
        btnDex.grid(row = 3, column = 4)
        
    

def getNumber(dieNumber):
    if dieNumber == "\u2680":
        return(1)
    elif dieNumber == "\u2681":
        return(2)
    elif dieNumber == "\u2682":
        return(3)
    elif dieNumber == "\u2683":
        return(4)
    elif dieNumber == "\u2684":
        return(5)
    elif dieNumber == "\u2685":
        return(6)
    else:
        return(0)


def rollFourDie():
    global d1
    d1 = random.choice(die)
    global d2
    d2 = random.choice(die)
    global d3
    d3 = random.choice(die)
    global d4
    d4 = random.choice(die)
    
    d1Number = getNumber(d1)
    d2Number = getNumber(d2)
    d3Number = getNumber(d3)
    d4Number = getNumber(d4)
    
    dieTotal = d1Number + d2Number + d3Number + d4Number
    
    btnDie1.config(text = d1)
    btnDie2.config(text = d2)
    btnDie3.config(text = d3)
    btnDie4.config(text = d4)
   
    
    lblTotal.config(text = dieTotal)
    lblDisplay.config(text = f"""You have rolled a {dieTotal} but you must choose
one die to get rid of to get your total""")

mw = Tk()
mw.title("Kymo's Designs")

die = ["\u2680", "\u2681", "\u2682", "\u2683", "\u2684", "\u2685"]

btnDie1 = Button(mw, text = "", font = ("Harrington", 40), command = lambda: btnClear("Die1"))
btnDie1.grid(row = 0, column = 0)

btnDie2 = Button(mw, text = "", font = ("Harrington", 40), command = lambda: btnClear("Die2"))
btnDie2.grid(row = 0, column = 1)

btnDie3 = Button(mw, text = "", font = ("Harrington", 40), command = lambda: btnClear("Die3"))
btnDie3.grid(row = 1, column = 0)

btnDie4 = Button(mw, text = "", font = ("Harrington", 40), command = lambda: btnClear("Die4"))
btnDie4.grid(row = 1, column = 1, pady = 5)

lblTotalLabel = Label(mw, text = "Total = ", font = ("Harrington", 20))
lblTotalLabel.grid(row = 2, column = 0)

lblTotal = Label(mw, text = "", font = ("Harrington", 20))
lblTotal.grid(row = 2, column = 1)

lblDisplay = Label(mw, text = "", font = ("Harrington", 20))
lblDisplay.grid(row = 0, column = 2, rowspan = 2, columnspan = 3)

btnRollTheDice = Button(mw, text = "Roll Them Bones", font = ("Harrington", 20), command = rollFourDie)
btnRollTheDice.grid(row = 3, column = 0, columnspan = 2, pady = 5, padx = 5)

mw.mainloop()