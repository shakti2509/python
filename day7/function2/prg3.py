def filter_long_words(l,n):
    l1=[] 
    for i in l:
        if len(i)>n:
            l1.append(i)
    print(l1)        
    
a=["adad","add","adfaf","as","bhgjhvbb ","hvhv"]
n=3
filter_long_words(a, n)    
    