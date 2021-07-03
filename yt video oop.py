# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 21:55:37 2021

@author: Chinwendu Nweje
"""
#The following are instances
se1 = ["Data Scientist", "Wendy", 20, "Junior", 1600]
se2 = ["Motivational Speaker", "Olivia", 23, "Sophomore", 1420]
se3 = ["Chef", "Oma","19","Freshman","1320"]

#def employ(se):
#    print(f"{se[1]} has just been employed")
#employ(se2)

#Class
class Career:
    #Class Attribute
    university= "Williams College"
    
    def __init__(self, job, name, age, year, satscore):
        #instance attributes
        self.job = job
        self.name =name
        self.age = age
        self.year = year
        self.satscore = satscore
     
    #Instance method
    def employ(self):
        print(f"{self.name} has just been employed")
        
    def worklocation(self, company):
        print(f"{self.name} is now working in {company}")
        
    def satretake(self, satretake):
        print(f" {self.name} took the SAT test {satretake} times to get a score of {self.satscore}")
        
    def database(self):
        database = f"name = {self.name}, satscore = {self.satscore}"
        return database

        
se1 = Career("Data Scientist","Wendy", 20, "Junior", 1600)
se2 = Career("Motivational Speaker", "Olivia", 23, "Sophomore", 1420)
se3 = Career("Chef", "Oma","19","Freshman","1320")
print(se1.name, se1.satscore)
print(Career.university)
print(se1.university)

se2.employ()
se2.worklocation("Google")
se3.worklocation("Chicken Republic")
se2.satretake(2)
print(se2.database())
