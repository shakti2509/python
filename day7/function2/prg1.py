def nubmatch(l,m):
     for i in l:
         if i in m:
             return True
     return False
a=[1,2,3,4,5]
b=[2,3,4,5,6]
c=[7,8,9,0]    
print(nubmatch(a,c))
         
             
