'''class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def speak(self):
        print("name is:",self.name,"age is:",self.age)
class Employee(Person):
    def __init__(self,name,age,employee_id):
        super().__init__(name,age)
        self.employee_id=employee_id
    #def speak(self):
        #print("name is:",self.name,"age is:",self.age)
    def speak(self):
        print("employee_id is:",super().speak(),self.employee_id)
p1=Person("Arun",22)
p2=Employee("Arun",22,"SOT19")'''
    

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class Employee(Person):
    def display(self,employee_id):
        self.employee_id=employee_id
        print("name of the person:",self.name,"\n","age of the person:",self.age,"\n","employee id:",self.employee_id)
p1=Employee("arun",22)

p1.display("SPT19")