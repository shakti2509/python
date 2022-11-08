def uniq(l1):
    l2=[]
    for i in l1:
        if i not in l2:
            l2.append(i)
            
    return l2
    
l=[1,2,3,4,3,2,1,7,8,5,3,9,3,0,23,45,88,98,100]   
print(uniq(l))
               
        