l=[10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
print("enter  the number ")
n =int(input())
for j in range(n+1):
    l[j]=int(input())
l1=[]
c=1
for i in l:
   if i in l :
       c=c+1
   elif c>2:
       l1.append(i)
print(l1)      


