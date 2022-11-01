t=(1,2,3,4,5,6,7,8,9)
print("enter  a number ")
f=int(input())
c=0
for i in t:
    if f is i:
        print("we found in tuple")
        c=1
        break
if c==0:
      print("we not found in tuple")