print("enter the number")
a,b,c=input("no are").split()
a=int(a)
b=int(b)
c=int(c)
if a<b and a<c:
    print(a,"is minimum")
elif b<a and b<c:
    print(b,"is minimum")
else:
    print(c,"is minimum")
