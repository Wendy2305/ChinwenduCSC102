# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 11:41:06 2021

@author: Chinwendu Nweje
"""
#This is a class method
class Student:
    name = 'Student'
    def __init__(self,a,b):
        self.a = a
        self.b = b
        
    @classmethod
    def info(cls):
        return cls.name
    
print(Student.info())