class Cars:
    name="cars"
    def __init__(self,name,milage,price,color):
        self.name=name
        self.milage=milage
        self.price=price
        self.color=color
class Supra(Cars):
    pass
class Bmw(Cars):
    pass
c1=Supra("supra",10,500000,"black")
c2=Bmw("bmw",15,5000000,"white")
