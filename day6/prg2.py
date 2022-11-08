def fun1(*no):
    return no

print(fun1(2,3,4,5,6,7,))
def fun2(*n):
    for i in n:
      print(i)
fun2(1,2,3,4,5,6,7)   
def fun3(na,*p):
       print(na)   
       sum=0
       for i in p:
           sum+=i
       print(sum)      
       
fun3("shakti",2,3,4,5,6,7,8,9,10)       
      
      
      
