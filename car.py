'''
Created on Feb 3, 2022

@author: kymo1
'''

class Car:
    
    def __init__(self, make, model, year, color):
        
        self.make = make
        self.model = model
        self.year = year
        self.color = color
    
    
    def drive(self):
        return "driving on the road!"
    
    
    def stop(self):
        return "stopped in the middle of the road!"
    
    