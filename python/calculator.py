'''
Date: 07/22/22
Author: James Eyrich
Program: Calculator
Tutorial: Bro Code YouTube
'''

from tkinter import *


def buttonPress(btn):
    global equationText
    equationText = equationText + str(btn)

    equationLabelText.set(equationText)

def equals():
    global equationText

    try:
        total = str(eval(equationText))

        equationLabelText.set(total)
        equationText = total
    except ZeroDivisionError:
        equationLabelText.set("You can not divide by zero!")
        equationText = ""
    except SyntaxError:
        equationLabelText.set("You can not do that!!")
        equationText = ""

def clear():
    global equationText
    equationLabelText.set("")
    equationText = ""


w = Tk()
w.title("Kymo's Designs - Calculator")
w.geometry("400x460")
w.config(bg = "#777777")


equationText = ""
equationLabelText = StringVar()

lblEquation = Label(w, textvariable = equationLabelText, font = ("Z003", 20), fg = "#00ff00", bg = "#000000", width = 30, height = 2)
lblEquation.pack(pady = 10)

f = Frame(w)
f.pack()

# Create buttons for the frame.
btnOne = Button(f, text = 1, bg = "#000000", 
                fg = "#00ff00", activebackground = "#00ff00", 
                activeforeground = "#000000", font = ("Z003", 35), 
                padx = 20, pady = 10, command = lambda: buttonPress(1))
btnTwo = Button(f, text = 2, bg = "#000000", 
                fg = "#00ff00", activebackground = "#00ff00", 
                activeforeground = "#000000", font = ("Z003", 35), 
                padx = 20, pady = 10, command = lambda: buttonPress(2))
btnThree = Button(f, text = 3, bg = "#000000", 
                fg = "#00ff00", activebackground = "#00ff00", 
                activeforeground = "#000000", font = ("Z003", 35), 
                padx = 20, pady = 10, command = lambda: buttonPress(3))
btnFour = Button(f, text = 4, bg = "#000000", 
                fg = "#00ff00", activebackground = "#00ff00", 
                activeforeground = "#000000", font = ("Z003", 35), 
                padx = 20, pady = 10, command = lambda: buttonPress(4))
btnFive = Button(f, text = 5, bg = "#000000", 
                fg = "#00ff00", activebackground = "#00ff00", 
                activeforeground = "#000000", font = ("Z003", 35), 
                padx = 20, pady = 10, command = lambda: buttonPress(5))
btnSix = Button(f, text = 6, bg = "#000000", 
                fg = "#00ff00", activebackground = "#00ff00", 
                activeforeground = "#000000", font = ("Z003", 35), 
                padx = 20, pady = 10, command = lambda: buttonPress(6))
btnSeven = Button(f, text = 7, bg = "#000000", 
                fg = "#00ff00", activebackground = "#00ff00", 
                activeforeground = "#000000", font = ("Z003", 35), 
                padx = 20, pady = 10, command = lambda: buttonPress(7))
btnEight = Button(f, text = 8, bg = "#000000", 
                fg = "#00ff00", activebackground = "#00ff00", 
                activeforeground = "#000000", font = ("Z003", 35), 
                padx = 20, pady = 10, command = lambda: buttonPress(8))
btnNine = Button(f, text = 9, bg = "#000000", 
                fg = "#00ff00", activebackground = "#00ff00", 
                activeforeground = "#000000", font = ("Z003", 35), 
                padx = 20, pady = 10, command = lambda: buttonPress(9))
btnZero = Button(f, text = 0, bg = "#000000", 
                fg = "#00ff00", activebackground = "#00ff00", 
                activeforeground = "#000000", font = ("Z003", 35), 
                padx = 20, pady = 10, command = lambda: buttonPress(0))
btnPlus = Button(f, text = "+", bg = "#000000", 
                fg = "#00ff00", activebackground = "#00ff00", 
                activeforeground = "#000000", font = ("Z003", 35), 
                padx = 18, pady = 10, command = lambda: buttonPress("+"))
btnMinus = Button(f, text = "-", bg = "#000000", 
                fg = "#00ff00", activebackground = "#00ff00", 
                activeforeground = "#000000", font = ("Z003", 35), 
                padx = 24, pady = 10, command = lambda: buttonPress("-"))
btnDivide = Button(f, text = "/", bg = "#000000", 
                fg = "#00ff00", activebackground = "#00ff00", 
                activeforeground = "#000000", font = ("Z003", 35), 
                padx = 23, pady = 10, command = lambda: buttonPress("/"))
btnMultiply = Button(f, text = "*", bg = "#000000", 
                fg = "#00ff00", activebackground = "#00ff00", 
                activeforeground = "#000000", font = ("Z003", 35), 
                padx = 20, pady = 10, command = lambda: buttonPress("*"))
btnEquals = Button(f, text = "=", bg = "#000000", 
                fg = "#00ff00", activebackground = "#00ff00", 
                activeforeground = "#000000", font = ("Z003", 35), 
                padx = 19, pady = 10, command = equals)
btnDecimal = Button(f, text = ".", bg = "#000000", 
                fg = "#00ff00", activebackground = "#00ff00", 
                activeforeground = "#000000", font = ("Z003", 35), 
                padx = 26, pady = 10, command = lambda: buttonPress("."))
btnClear = Button(f, text = "Clear", bg = "#000000", 
                fg = "#00ff00", activebackground = "#00ff00", 
                activeforeground = "#000000", width = 11, font = ("Z003", 35), 
                padx = 19, pady = 10, command = clear)



# Display buttons on the frame.
btnOne.grid(row = 2, column = 0)
btnTwo.grid(row = 2, column = 1)
btnThree.grid(row = 2, column = 2)
btnFour.grid(row = 1, column = 0)
btnFive.grid(row = 1, column = 1)
btnSix.grid(row = 1, column = 2)
btnSeven.grid(row = 0, column = 0)
btnEight.grid(row = 0, column = 1)
btnNine.grid(row = 0, column = 2)
btnZero.grid(row = 3, column = 0)
btnPlus.grid(row = 0, column = 3)
btnMinus.grid(row = 1, column = 3)
btnDivide.grid(row = 2, column = 3)
btnMultiply.grid(row = 3, column = 3)
btnEquals.grid(row = 3, column = 2)
btnDecimal.grid(row = 3, column = 1)
btnClear.grid(row = 4, column = 0, columnspan = 4)


w.mainloop()