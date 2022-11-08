def display(l):
    print(l)
def disr(l):
    print(l[::-1])
def disalt(l):
    print(l[::2])
def disup(l):
    print(l.upper)    
def dislo(l):
    print(l.lower)    
def disuniq(l):
    print(list(set(l)))
def disdub(l):
     l1=[]
     for i in l:
         if i in l[i+1:]:
             l1.append(i)
     print(l1) 

   