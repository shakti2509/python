# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 14:35:47 2022

@author: admin
"""
nsum=0
esum=0
osum=0
l=[1,2,3,4,5,6,7,-1,-2,-5,-3,8,10]
for i in l:
    if i<0:
        nsum+=i
    elif i%2==0:
        esum+=i
    elif i%2==1:
        osum+=i
print(nsum)
print(esum)
print(osum)        
        