def prifun(n):
    f=0
    
    for i in range(2,n):
     if(n%i==0):
       f=1
       break
    if f==0:
       return n        


import numpy as np
a=np.random.randint(1,30,10)
print(a)
p=[j for j in a if prifun(j)!=None]
print(np.array(p))
"""p=[]
for j in a:
   if prifun(j)!=None:
       p.append(j)
print(np.array(p))
"""

