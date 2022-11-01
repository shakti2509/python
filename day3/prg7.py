# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 15:13:15 2022

@author: admin
"""

s="""Bolo Bake Bihari Lal Ki"""
c=0
b=0
for i in s:
    if i.isupper():
        c=c+1
    elif i.islower():
       b=b+1    
    else:
      pass
print(c)
print(b)