'''
Created on Feb 13, 2022

@author: kymo1
'''

from tkinter import *


def keyPress(event):
    lblResult.config(text = event.keysym)
    

w = Tk()

lblResult = Label(w, font = ("Harrington", 40))
lblResult.pack()

w.bind("<Key>", keyPress)

w.mainloop()
