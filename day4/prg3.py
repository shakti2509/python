# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 14:48:23 2022

@author: admin
"""

l=[1,2,3,4,5,6,7,8,9,10]
l1=[]
l2=[]
for i in l:
    if i%2==0:
        l1.append(i)
    else:
        l2.append(i)
#print(l1)
print(max(l2))
print(max(l1))        