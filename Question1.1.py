class Vehicle:
    def __init__(self,make,model):
        self.make=make
        self.model=model
    def start(self):
        pass
    def stop(self):
        pass
class Car(Vehicle):
        def __init__(self,make,model,num_door):
             self.make=make
             self.model=model
             self.num_door=num_door
        def display(self):
             print("\n","Car")
             print("\n","Make is :",self.make,"\n","model is :",self.model,"\n","num_door is :",self.num_door)
class Mototcycle(Vehicle):
     def __init__(self,make,model,two_wheels):
          self.make=make
          self.model=model
          self.two_wheels=two_wheels
     def display(self):
        print("\n","Motorcycle")
        print("\n","make is :",self.make,"\n","Model is:",self.model,"\n","two_wheels:",self.two_wheels)
p1=Car("Skoda","Slavia",4)
p1.start()
p1.display()
p1.stop()
p2=Mototcycle("Yamaha","MT 15",2)
p2.start()
p2.display()
p2.stop()