l=[1,2,3,4,12,4,3,5,6,7,8,9,12,1,3,9,13,14,1,5,4,0]
l1=list(set(l))
print(l1)
l2=[]
for i in l:
      if i not in l2:
          l2.append(i)
          
print(l2)          
          