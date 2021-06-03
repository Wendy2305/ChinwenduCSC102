# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Coffee:
#Coffeecupcounter is the class variable
    coffeeCupCounter =0 #nitialize class variable
    def __init__(self, themilk, thesugar, thecoffeemate):
        self.milk = themilk #intialize class variable
        self.sugar = thesugar #intialize class variable
        self.coffeemate = thecoffeemate #intialize class variable
        Coffee.coffeeCupCounter= Coffee.coffeeCupCounter +1
        print(f"you now have your coffee with {self.milk} milk, {self.sugar} sugar and {self.coffeemate} coffeemate")
              
mySugarFreeCoffee = Coffee(2,0,1) #instantation or object creation
print(mySugarFreeCoffee.sugar)        
myMuchSugarCoffee = Coffee(2,10,1)
print(myMuchSugarCoffee.sugar) #instantation or object creation
print(f"we have made {Coffee.coffeeCupCounter} coffee cups so far!")