# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 11:10:11 2021

@author: Chinwendu Nweje
"""

#Instance method example in python

class Student:
    studentcounter=0
    def __init__(self,a,b):
        self.a = a
        self.b = b
        Student.studentcounter= Student.studentcounter+1
    
#This is acc the instance method
    def avg(self):
        return(self.a + self.b)/2
    
s1 = Student(10,30)
s2 = Student(2,4)
s3 = Student(12,24)
s4 = Student(400,200)
print( s4.avg())
print(f"we have calculated the scores of {Student.studentcounter} students so far!")
