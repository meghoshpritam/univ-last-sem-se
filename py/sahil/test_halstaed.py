# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 19:30:16 2020

@author: BILU
"""

U_OPERATER = [",","/","*","print","="]
U_OPERAND = ["a","b","c","c>10","c*b","avg","3"]
C_operator=0
C_operand=0
f = open("test.py","r")
l=0
while True:
    c = f.read(1)
    if not c:
      print("End of file")
      break
    if c in U_OPERATER:
        C_operator=C_operator+1
        U_OPERATER.remove(c)
f.close()

f = open("test.py","r")
for line in f.readlines():
    l=l+1
    print(l," : ",line)
    for w in line.split():
        if w in U_OPERAND:
            C_operand=C_operand+1
            U_OPERAND.remove(w)

f.close()
          
print("Unique operator : ", C_operator )        
print("Unique operand : ", C_operand)        
