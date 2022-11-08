#ass3 oops1
class demo:
    def __init__(self):
        pass
    def set_string(self,s):
        self.s=s
    def get_string(self,s):
        return s
    def upp(self,s):
        self.s=s
        v=s.upper()
        return v
m=demo()
l='India is my country                         '
#m.set_string(l)
print(m.upp(l))
        