# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 14:09:04 2021

@author: Chinwendu Nweje
"""

class Onlinestore:
    def __init__(self, numberOfitemsbought, totalcost):
        self.numberOfitemsbought = numberOfitemsbought
        self.totalcost = totalcost
        
    def Calculator(self, discount):
        self.discount = (self.totalcost)*0.9
        
        if (self.numberOfitemsbought) > 10 and (self.totalcost) > 100000:
            print(f"Customer purchased {self.numberOfitemsbought} goods with a total price of {self.totalcost} naira")
            print(f"Congrats customer has qualified for both discount and gift")
            print(f"Customer now has to pay {self.discount} naira")
            
        elif (self.numberOfitemsbought) < 10 and (self.totalcost) > 100000:
            print(f"Customer purchased {self.numberOfitemsbought} goods with a total price of {self.totalcost} naira")
            print(f"Congrats customer has qualified for only discount")
            print(f"Customer now has to pay {self.discount} naira")
            
        elif (self.numberOfitemsbought) > 10 and (self.totalcost) < 100000:
            print(f"Customer purchased {self.numberOfitemsbought} goods with a total price of {self.totalcost} naira")
            print(f"Congrats customer does not qualify for anything")
            
        elif (self.numberOfitemsbought) < 10 and (self.totalcost) < 100000:
            print(f"Customer purchased {self.numberOfitemsbought} goods with a total price of {self.totalcost} naira")
            print(f"Congrats customer does not qualify for anything")
            
            
            
numberOfitemsbought = int(input("How many items did the customer buy: "))   
totalcost =int(input("What was the total cost of items: "))

customer1 = Onlinestore(numberOfitemsbought, totalcost)     
customer1.Calculator(totalcost)  
