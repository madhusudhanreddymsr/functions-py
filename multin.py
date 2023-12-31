class Grand:
    def __init__(self,a,b):
       self.a=a
       self.b=b
class Parent:
    def __init__(self,a,b,c,d):
        super().__init__(a,b)
        self.c=c
        self.d=d
class Child:
    def __init__(self,a,b,c,d,e,f):
        super().__init__(a,b,c,d)
        self.e=e
        self.f=f
obj=Child(1,2,3,4,5,6)

