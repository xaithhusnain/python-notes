print("hello world")

class car:
    @staticmethod
    def start():
        print("car started...")
    
    @staticmethod
    def stop():
        print("car stopped....")

class toyota(car):

    colour = "black"

    def __init__(self):
        pass

c1 = toyota()
print(c1.colour)
c1.start()
c1.stop()







# types of inheritance

'''
single inheritance
there is only one parent class and only one child class

'''
class car:
    @staticmethod
    def start():
        print("car started...")
    
    @staticmethod
    def stop():
        print("car stopped....")

class toyota(car):

    colour = "black"

    def __init__(self,name):
        self.name = name


c1 = toyota("fortuner")
print(c1.name)
print(c1.colour)
c1.start()
c1.stop()






'''
multi level inheritance

in this we have a series of inheritance in which properties are inherited on after to the other
suppose a father have properties like grandfather e.g curly hair,
but father have also its unique properties e.g tall (but grandfather is not)
but son have the properties of both father and grandfather both e.g curly hair, tall
so every next class will the both its unique and all the pervious inherited classes

'''


class car:
    @staticmethod
    def start():
        print("car started...")
    
    @staticmethod
    def stop():
        print("car stopped....")

class toyota(car):
    def __init__(self,brand):
        self.brand = brand

class fortuner(toyota):
    def __init__(self, colour):
        self.colour = colour

c1 = fortuner("black")
print(c1.colour)        
c1.start()   
c1.stop()   









'''
multiple inheritance

in this we have multiple parents that drived a single chiled

'''

class animal:

    x = "wellcome to class A"

class birds:

    y = "wellcome to class B"

class sparrow(animal,birds):

    z = "wellcome to class C"

a = sparrow()
print(a.x)
print(a.y)
print(a.z)