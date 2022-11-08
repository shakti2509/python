def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def pow(a,b):
    return a**b
def div(a,b):
    return a/b
def ipos(a):
    return a>=0
def ineg(a):
    return a<0
def prime(a):
    f=0
    for i in range(2,a):
        if a%i==0:
            f=1
            break
    if f==1:
        return "it is not prime"
    else:
        return "it is prime"
def arm(a):
      temp=a
      sum=0
      i=0
      while i<3:
         i=i+1
         n=a%10
         sum=sum+n**3
         a=a//10
      if sum==temp:
          return "it is armstrong number "
      else:
          return "it is not armstrong number "