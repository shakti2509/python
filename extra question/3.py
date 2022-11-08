l1= [12, 67,111, 34]
l2=[]
for i in l1:
    sum=0 
    while i>0:
        s=i%10
        i=i//10
        sum=sum+s
    l2.append(sum)
print(l2)    
        
