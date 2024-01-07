from abc import  ABC

# abstract method of base class
class Shape(ABC):
    def area(self):
        print("Area of the shape")

    def perimeter(self):
        print("perimeter of shape is")
# derived class of shape base class       
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return 3.14*self.radius*self.radius
    
    def perimeter(self):
        return 2*3.14*self.radius
    
class Square(Shape):
    def __init__(self,side_length):
        self.side_length=side_length

    def area(self):
        return self.side_length*self.side_length
    
    def perimeter(self):
        return 4*self.side_length
p1=Circle(4)
p2=Square(5)

print("The area of circle is :",p1.area())
print("The permeter of circle is ",p1.perimeter())
print("The area of square is :",p2.area())
print("The permeter of square is ",p2.perimeter())
    
    