# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import math
userinput=input("enter file name")
myfile=open(userinput)
count=0
for line in myfile:
    print(line)
    count=count+1
print(count) 
myfile.close()
kloc=count/1000

n1=int(input("enter the no of unique operator"))
n2=int(input("enter no of operand"))
N1=int(input("total occurance of operator"))
N2=int(input("total occurance of  operand"))
count=N1+N2
print("length is",count)
volume=count*math.log2(n1+n2)
print("volume is",volume)