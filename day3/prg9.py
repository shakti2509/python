# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 15:31:54 2022

@author: admin
"""
print("enter the string")
s=(input())
s1=s[:2]+s[:-3:-1]
if len(s1)==4:
   print("string lentgth is greater than are equal to 2")
else:
   print("string is empty")
   
