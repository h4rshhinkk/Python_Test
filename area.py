from cmath import pi


class Area:
    def __init__(self,length,radius):
        self.length=length
        self.radius=radius

    def CalculateArea(self):
        area=self.length*self.radius
        print("Area of Rectangle =",area)


class Circle(Area):
    def __init__(self,radius):
        self.radius=radius

    def CalculateArea(self):
        area=pi*self.radius**2
        print('Area of Circle:',area)


a=Area(10,20)
a.CalculateArea()
b=Circle(10)
b.CalculateArea()