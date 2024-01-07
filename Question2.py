class Shape:
    def area(self):
        pass
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        print("The area of circle:",3.14**self.radius**2)
class Rectangle(Shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        print("The area of rectangle :",self.length*self.width)
p1=Circle(5)
p1.area()
p2=Rectangle(4,5)
p2.area()
