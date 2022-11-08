l= [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
l1=[]
for i in l:
    k=1
    for  j in i:
      k*=j
    l1.append(k)
print(max(l1))    
    