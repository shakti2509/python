def long(l):
    a=l[0]
    for i in range(0,len(l)):
        if len(a)<len(l[i]):
            a=l[i]
    print(a)     
    
m=["adaf","agfahse","rfbijabfjkb","qbdubnb","hsjg"]
long(m)    