class add3:
    @staticmethod
    def add3(a,b,c):
        return a+b+c
class add2:
    @staticmethod
    def add2(a,b):
        return a+b
class add(add2,add3):
    pass
class sub2:
    @staticmethod
    def sub2(a,b):
        return a-b
class cal(add,sub2):
    pass
obj=cal()
obj.add3(4,5,6)
obj.add2(4,3)
obj.sub2(7,9)

