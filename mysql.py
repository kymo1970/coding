'''
Created on Mar 16, 2022

@author: kymo1
'''

from tkinter import *
import mysql.connector


mw = Tk()
mw.title("Kymo's Designs - CRMS")
mw.geometry("200x200")

customersDB = mysql.connector.connect(
        
        host = "localhost",
        user = "root",
        passwd = "DiscGolf1970"
    )

print(customersDB)

mw.mainloop()
