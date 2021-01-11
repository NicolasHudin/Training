# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 15:04:35 2020

@author: Ares
"""

import random 

#data types reviewed

random_value = random.random()

print(random_value)

"""
print("hello")
print(1)
print(1.0)
"""

#Counts from 0!

#First entry will be 0
[1231,231423,31423,1234]
[1,2,3,4,5,6,7,8,9,10]

#lists can be mixed data types
list1 = [1,"two",3.0,4,"five"]         
#print(list1)

list1.append(1)
#print(list1)

"""
x=0

print(x)

x += 10

print(x)

x += 10

print(x)
"""

def xplus10(x_value):
    x_value +=10
    return(x_value)

value = xplus10(100)

value+=100
print(value)