'''
Created on Mar 7, 2022

@author: kymo1
'''

import tkinter as tk
import time as tm

def timeLoop():
    
    lblTime.config(text = tm.strftime("%I:%M:%S %p"))
    lblDay.config(text = tm.strftime("%A"))
    lblDate.config(text = tm.strftime("%B %d, %Y"))
        
    lblTime.after(500, timeLoop)

mw = tk.Tk()
mw.title("Kymo's Designs - Digital Clock")

lblTime = tk.Label(mw, font = ("Harrington", 60), 
                   bg = "#000000", fg = "#00ff00")
lblTime.pack(fill = "both")

lblDay = tk.Label(mw, font = ("Harrington", 60), 
                  bg = "#000000", fg = "#00ff00")
lblDay.pack(fill = "both")

lblDate = tk.Label(mw, font = ("Harrington", 60),
                    bg = "#000000", fg = "#00ff00")
lblDate.pack()

timeLoop()

mw.mainloop()