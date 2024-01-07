class Animal:
    def __init__(self,name):
        self.name=name
    def speak(self):
         print("Animal")
class Dog(Animal):
    def speak(self):
        print("The bread is ",self.name)
class Cat(Animal):
    def speak(self):
        print("The bread is ",self.name)
p1=Dog("Rotwiller")
p1.speak()

p2=Cat("persian cat")
p2.speak()