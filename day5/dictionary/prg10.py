#prg 10 dictionary
p={"arham":"blue","monika":"red","lisa":"yellow","vinod":"purple","jenny":"pink"}
print(p)
#1
print(len(p))
#2
p["lisa"]="black"
print(p)
#3
b=p.popitem()
print(b)
print(p)
#4
l=sorted(p.keys())
for i in l:
    print(i,p[i])
