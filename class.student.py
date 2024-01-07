class Student:
    def __init__(self,name,phone_number,address):
        self.name=name
        self.phone_number=phone_number
        self.address=address
    def display(self):
        print("Name is :", self.name, ",Phone number is :", self.phone_number, ",Address is :", self.address)
p1= Student("sinan",8590305679,"rosewilla kochi")
p1.display()   