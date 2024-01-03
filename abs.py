from abc import ABC,abstractmethod


class car:
    def __init__(self,name,color,price,speed):
        self.name=name
        self.color=color
        self.price=price
        self.speed=speed
    @abstractmethod
    def stop():
        pass
    @abstractmethod
    def speed_up():
        pass
    def speed_down():
        pass


class bmw(car):
    def speed_up(self):
        self.speed+=5
    def speed_down(self):
        self.speed-=5
    def stop(self):
        self.speed=0

class tata(car):
    def speed_up(self):
        self.speed+=2
    def speed_down(self):
        self.speed+=2
    def stop(self):
        self.speed=0
bmw1=bmw('s4','black',45000,80)
nexon=tata('nexon ev','red',20000,150)