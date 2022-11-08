class rev:
    def __init__(self,s):
        self.s=s
        
    def rever(self,s):
        v=s.split()
        v=v[::-1]
        a=' '.join(str(i) for i in v) #covert list to string
         
        return a
l="i love my india"
r=rev(l)
print(r.rever(l))    
        
        
        