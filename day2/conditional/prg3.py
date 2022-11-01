   print("enter  the markas of five subject")
a,b,c,d,e=input("enter the number ").split()
a=int(a)
b=int(b)
c=int(c)
d=int(d)
e=int(e)
marks=a+b+c+d+e
per=(marks/5)
if per>60:
    print(" boy are first division")
elif per>50 and per<60:
    print("boys are second division")

elif per>40 and per<50:
    print("boys are third division")

elif per>33 and per<40:
    print("boys are just pass")
else:
    print("boys are fail")

