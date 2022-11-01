# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 15:56:50 2022

@author: admin
"""

print("enter  the  string")
s=input()
print("enter the character")
c=input()
for i in s[:1]:
    if c==i:
        print(c,"found")
        break
    else:
        print(c,"not found")