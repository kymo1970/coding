'''
Created on Feb 10, 2022

@author: kymo1
'''

class Vehicle:
    
    def __init__(self, vehicletype):
        
        self.vehicletype = vehicletype
        
        if vehicletype == "motorcycle":
                
            self.wheels = 2
            self.motor = 2
            
        elif vehicletype == "car":
                
            self.wheels = 4
            self.motor = 6
            
        elif vehicletype == "truck":
                
            self.wheels = 4
            self.motor = 8
            
        else:
            return "Your vehicle is broke down!!"