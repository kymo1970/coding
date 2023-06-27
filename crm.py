'''
Created on Mar 9, 2022

@author: Kymo's Designs
'''

from tkinter import *
#import mysql.connector
import sqlite3

# Declaring variables.
fn = ""
ln = ""
addr = ""
city = ""
st = ""
zipCode = ""
email = ""

# Define the deleteRecord function.
def deleteRecord():
    
    # Define the delete function.
    def delete():
        
        # Connect to the database.
        conn = sqlite3.connect("customers.db")
    
        # Cursor for the database.
        cur = conn.cursor()
        cur.execute("DELETE FROM customer WHERE oid =" + entDelete.get())
        customers = cur.fetchall()
        print(customers)
        
        # Clear the entry box.
        entDelete.delete(0, END)
        
        conn.commit()
    
        conn.close()
        
        entDelete.focus()
    
    # Create a search window.
    dw = Tk()
    dw.title("Search by Name")
    
    # Labels for the search window.
    lblCustomerID = Label(dw, text = "Customer ID:", font = ("Arial", 15))
    lblCustomerID.grid(row  = 0, column = 0)
    
    # Entry box for the delete window.
    entDelete = Entry(dw, font = ("Arial", 15))
    entDelete.grid(row = 0, column = 1)
    
    # Button for deleting the record.
    btnDelete = Button(dw, text = "Delete the Record", font = ("Arial", 15), command = delete)
    btnDelete.grid(row = 1, column = 0, columnspan = 2)
    
    dw.mainloop()

# Define the search function.
def search():
    
    # Create a search window.
    sw = Tk()
    sw.title("Search by Name")
    
    # Connect to the database.
    conn = sqlite3.connect("customers.db")
    
    # Cursor for the database.
    cur = conn.cursor()
    
    # Labels for the search window.
    lblFirstName = Label(sw, text = "First Name:", font = ("Arial", 15))
    lblLastName = Label(sw, text = "Last Name:", font = ("Arial", 15))
    
    # Entry boxes for the search window.
    entFirstName = Entry(sw, font = ("Arial", 15))
    entLastName = Entry(sw, font = ("Arial", 15))
    
    # Place widgets on the search window.
    # Labels.
    lblFirstName.grid(row = 0, column = 0)
    lblLastName.grid(row = 1, column = 0)
    
    # Entry boxes.
    entFirstName.grid(row = 0, column = 1, padx = 5, pady = 2)
    entLastName.grid(row = 1, column = 1)
    
    fn = entFirstName.get()
    ln = entLastName.get()
    
    cur.execute("SELECT *, oid FROM customer")
    customers = cur.fetchall()
    #print(customers)
    
    # Create customer record variable.
    customerRecord = ""
    
    # Loop through customers and display them.
    for customer in customers:
        customerRecord += str(customer) + "\n"
        
    # Label to display the results.
    lblResults = Label(sw, text = customerRecord)
    lblResults.grid(row =2, column = 0, columnspan = 2)
    
    conn.commit()
    
    conn.close()
    
    sw.mainloop()

# Submit information function.
def submitInformation(fn, ln, addr, city, st, zipCode, email):
    
    conn = sqlite3.connect("customers.db")

    cur = conn.cursor()
    #print(conn)
    
    # Initializing variables.
    fn = fn
    ln = ln
    addr = addr
    city = city
    st = st
    zipCode = zipCode
    email = email    
    
    # Get information from entry boxes.
    fn = entFirstName.get()
    ln = entLastName.get()
    addr = entAddress.get()
    city = entCity.get()
    st = entState.get()
    zipCode = entZipCode.get()
    email = entEmail.get()
    
    
    # Input data into the customer table in the customers database.
    cur.execute("INSERT INTO customer values(:fn, :ln, :addr, :city, :st, :zipCode, :email)", 
                 
                    {
                        
                        "fn": fn,
                        "ln": ln,
                        "addr": addr,
                        "city": city,
                        "st": st,
                        "zipCode": zipCode,
                        "email": email
                        
                    })

    # Delete information from the entry boxes.
    entFirstName.delete(0, END)
    entLastName.delete(0, END)
    entAddress.delete(0, END)
    entCity.delete(0, END)
    entState.delete(0, END)
    entZipCode.delete(0, END)
    entEmail.delete(0, END)
    
    # Give the first name entry box the cursor.
    entFirstName.focus()
    
    conn.commit()

    conn.close()

# Create the window for the form.
mw = Tk()
mw.title("Kymo's Designs - CRMS")
#mw.geometry("377x300")
#mw.config(bg = "#666666")

# Labels for the form.
lblFirstName = Label(mw, text = "First Name:", font = ("Arial", 15))
lblLastName = Label(mw, text = "Last Name:", font = ("Arial", 15))
lblAddress = Label(mw, text = "Address:", font = ("Arial", 15))
lblCity = Label(mw, text = "City:", font = ("Arial", 15))
lblState = Label(mw, text = "State:", font = ("Arial", 15))
lblZipCode = Label(mw, text = "Zip Code:", font = ("Arial", 15))
lblEmail = Label(mw, text = "Email Address:", font = ("Arial", 15))

# Entry boxes for the form.
entFirstName = Entry(mw, font = ("Arial", 15))
entLastName = Entry(mw, font = ("Arial", 15))
entAddress = Entry(mw, font = ("Arial", 15))
entCity = Entry(mw, font = ("Arial", 15))
entState = Entry(mw, font = ("Arial", 15))
entZipCode = Entry(mw, font = ("Arial", 15))
entEmail = Entry(mw, font = ("Arial", 15))

# Buttons for form.
btnSubmit = Button(mw,text = "Submit Information", 
                      font = ("Arial", 15),  
                      command = lambda: submitInformation(fn, 
                                                          ln, 
                                                          addr, 
                                                          city, 
                                                          st, 
                                                          zipCode, 
                                                          email))

btnSearch = Button(mw, text = "Search by ID", 
                   font = ("Arial", 15), 
                   command = search)

btnDelete = Button(mw, text = "Delete a Record", 
                   font = ("Arial", 15), 
                   command = deleteRecord)

# Place the widgets on the window.
#Labels
lblFirstName.grid(row = 0, column = 0, sticky = "e")
lblLastName.grid(row = 1, column = 0, sticky = "e")
lblAddress.grid(row = 2, column = 0, sticky = "e")
lblCity.grid(row = 3, column = 0, sticky = "e")
lblState.grid(row = 4, column = 0, sticky = "e")
lblZipCode.grid(row = 5, column = 0, sticky = "e")
lblEmail.grid(row = 6, column = 0, sticky = "e")

#Entry
entFirstName.grid(row = 0 , column = 1, pady = (5, 0))
entLastName.grid(row = 1 , column = 1)
entAddress.grid(row = 2 , column = 1)
entCity.grid(row = 3 , column = 1)
entState.grid(row = 4 , column = 1)
entZipCode.grid(row = 5 , column = 1)
entEmail.grid(row = 6 , column = 1)

# Buttons
btnSubmit.grid(row = 7, column = 0,columnspan =2, padx = 5, pady = (5, 0), ipadx = 100)
btnSearch.grid(row = 8, column = 0,columnspan = 2, padx = 5, ipadx = 125)
btnDelete.grid(row = 9, column = 0,columnspan = 2, padx = 5, pady = (0, 5), ipadx = 110)

# Give first name entry box the cursor.
entFirstName.focus()

mw.mainloop()
