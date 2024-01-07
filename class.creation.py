'''class Person:
    def __init__(self,name,age): # parameterised constructor
        self.name=name
        self.age=age
    def display(self):
        print("my name is :",self.name, ", my age is :", self.age)
# object creation        
p1=Person("Anjana",22)
p1.display()'''


'''class Person:
    def __init__(self): # non-parameterised constructor
        print("hello world")
    def display(self,name,age):
        self.name=name
        self.age=age
        print("my name is :",self.name, ", my age is :", self.age)
# object creation        
p1=Person()
#fuction calling using object
p1.display("Aditi",17)'''


class Person:
    #def __init__(self): # non-parameterised constructor
        #print("hello world")
    def display(self,name,age):
        self.name=name
        self.age=age
        print("my name is :",self.name, ", my age is :", self.age)
# object creation        
p1=Person()
#fuction calling using object
p1.display("ram",23)