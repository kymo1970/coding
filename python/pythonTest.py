from tkinter import *
from time import *

w = Tk()
w.title("Kymo's Designs - File Counter")
w.geometry("500x350")

lblFiles = Label(w, text="Number of Files: ", font=("Harrington", "30"))
lblFiles.pack()

w.mainloop()