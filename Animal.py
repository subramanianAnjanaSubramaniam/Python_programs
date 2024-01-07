#create a class Animal
class Animal:
    def __init__(self,name):
        self.name=name
        def makesound(self):
            print("Generic animal sound")
# define subclasses
class Dog(Animal):
    def makesound(self):
        print("Bow Bow")
class Cat(Animal):
    def makesound(self):
        print("meow meow")

#create object
p1=Dog("Rot")
p2=Cat("momu")

#define function for animal sound
def animalsound(animal):
    animal.makesound()

animalsound(p1)
animalsound(p2)