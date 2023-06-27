'''
Created on Mar 14, 2022

@author: Kymo's Designs
'''


# Imports for program.
from tkinter import Tk, Entry, Label, Button
import sqlite3
#from PIL import Image, ImageTk


# Main Window for form.
mw = Tk()
mw.title("Kymo's Designs - DBS")

# Create and connect to customers database.
conn = sqlite3.connect("customers.db")

# Cursor for the database.
cur = conn.cursor()

'''
# Create customer table in database.
conn.execute("""CREATE TABLE customer (
            firstName text,
            lastName text,
            address text,
            city text,
            state text,
            zipCode integer,
            emailAddress text)""")
'''

# Commit Changes to the database.
conn.commit()

# Close connection to database(optional).
conn.close()

# Main window loop to keep window visible.
mw.mainloop()
