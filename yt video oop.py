# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 21:55:37 2021

@author: Chinwendu Nweje
"""

se1 = ["Data Scientist", "Wendy", 20, "Junior", 1600]
se2 = ["Motivational Speaker", "Olivia", 23, "Sophomore", 1420]

#Class
class SoftwareEngineer:
    #Class Attribute
    university= "Williams College"
    
    def __init__(self, job, name, age, year, satscore):
        #instance attributes
        self.job = job
        self.name =name
        self.age = age
        self.year = year
        self.satscore = satscore
        
se1 = SoftwareEngineer("Data Scientist","Wendy", 20, "Junior", 1600)
print(se1.name, se1.satscore)
        