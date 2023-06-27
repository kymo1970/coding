'''
Created on Feb 3, 2022

@author: kymo1
'''


from tkinter import *
from car import Car
from vehicle import Vehicle


veh1 = Vehicle("truck")

print(str(veh1.wheels) + " " + str(veh1.motor))


car1 = Car("Ford", "Mustang", 2022, "Purple")

win = Tk()
win.title("Kymo's Designs")

lblCar = Label(win, text = "Your " + car1.color + " " 
               + str(car1.year) + " " 
               + car1.make + " " 
               + car1.model 
               + " is a very cool car! And is also " 
               + car1.drive())
lblCar.pack(padx = 10, pady = 10)


win.mainloop()
