class Employe:
    def __init__(self,name,code,salary):
        self.name=name
        self.code=code
        self.salary=salary
    def display(self):
        print("Name is :", self.name, "Code is: ", self.code, "Salary is :", self.salary)
p2=Employe("Rohini","SPT19",45000)
p2.display()
