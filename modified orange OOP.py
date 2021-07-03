# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 10:07:32 2021

@author: Chinwendu Nweje
"""

#Constructor
class Supermarket:
    
    OrangeNumber = 100
    
    def __init__(self, name, fruitypap):
        self.name = name
        self.fruitypap = fruitypap
        
    def Stockcounter(self, pricetag):
       self.pricetag = (self.fruitypap)*5
       if (self.fruitypap) < (Supermarket.OrangeNumber):
           print(f"You have purchased {self.fruitypap} oranges, your total price is {self.pricetag} naira")
       else:
           print(f"Awfully sorry hun, but we only have {Supermarket.OrangeNumber} oranges avaliable")
       
      
           
    @classmethod
    def Farewell(cls):
        print("Thank you for shopping with us!")
        
   # @classmethod
    #def Stockloop(cls, fruitypap):
     #   while 
    
fruitypap =int(input("How many oranges will you be buying: ")) 
                     
                     
                     
custom1= Supermarket("James Kaka", fruitypap)

print(custom1.fruitypap)
custom1.Stockcounter(fruitypap)
Supermarket.Farewell()