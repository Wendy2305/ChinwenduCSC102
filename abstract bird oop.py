# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 15:24:49 2021

@author: Chinwendu Nweje
"""

from abc import ABC, abstractmethod
class Bird(ABC):
    def defecate(self):
        print("Birds generally defecate through their anus")
        
    @abstractmethod
    def Move(self):
        pass
    
class Ostrich(Bird):
    def Move(self):
        print("Ostriches do not fly. They walk on land")
        
class Hen(Bird):
    def Move(self):
        print("Hens also cannot fly. They run on land.")
        
Ost = Ostrich()
Hen = Hen()

Ost.defecate()
Ost.Move()

Hen.defecate()
Hen.Move()
