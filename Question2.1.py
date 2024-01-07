class Shape:
    def area(self):
        pass
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        print("The area of circle:",3.14*self.radius**2)
    def perimeter(self):
        print("The perimeter of circle:",2*3.14*self.radius)
class Square(Shape):
    def __init__(self,side):
        self.side=side
    def area(self):
        print("The area of square :",self.side**2)
    def perimeter(self):
        print("The perimeter of square: ",4*self.side)

class Triangle(Shape):
    def __init__(self,base,height):
        self.base=base
        self.height=height
    def area(self):
        print("The area of triangle :",0.5*self.base*self.height)
    def perimeter(self,side1,side2,side3):
        self.side1=side1
        self.side2=side2
        self.side3=side3
        print("The perimeter of the triangle :",self.side1+self.side2+self.side3)
p1=Circle(5)
p1.area()
p1.perimeter()
p2=Square(6)
p2.area()
p2.perimeter()
p3=Triangle(4,5)  
p3.area() 
p3.perimeter(4,5,6)