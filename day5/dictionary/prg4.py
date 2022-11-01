d={n:n*n*n for n in range(1,11)}
print(d)
v=1
for i in d.values():
   v*=i
   
   
print(v)
print(type(v))   