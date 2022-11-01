print('enter the number')
n=int(input())
t=n
p=0
while n!=0:
   r=n%10
   p=p*10+r
   n=n//10

if(t==p):
  print(t," is palindrom")
else:
    print(t,"is not palindrom")
