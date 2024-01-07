class Vehicle:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
class Car(Vehicle):
    def drive(self):
        print("The brand", self.brand, "is","The model",self.model, "standing in the road")

class Motorcycle(Vehicle):
    def drive(self):
        print(f"the model {self.model}  {self.brand} is driving on road")

p1=Car("skoda","SUVs")
p1.drive()
p2=Motorcycle("Yamaha","Yamaha MT 15")
p2.drive()
