print("hello world")

print(1+2) #3
print("hello" + "world") #concatenate (helloworld)
print([1,2,3] + [4,5,6]) #merge


print(len("hello"))   # 5 (counts characters in string)
print(len([1, 2, 3])) # 3 (counts items in list)
print(len({"a": 1, "b": 2})) # 2 (counts keys in dictionary)


'''
this shows the concept polymorphism
which multiple forms of a single entity

'''



class Complex:
    def __init__(self,real,imag):
        self.real = real
        self.imag = imag
    
    def showno(self):
        print(f"{self.real}i + {self.imag}j")
    
    def add(self,other):
        newreal = self.real+other.real
        newimag = self.imag+other.imag
        return Complex(newreal , newimag)


num1 = Complex(1,4)
num1.showno()

num2 = Complex(5,9)
num2.showno()

num3 = num1.add(num2)
print(num3)
num3.showno()











class Complex:
    def __init__(self,real,imag):
        self.real = real
        self.imag = imag
    
    def showno(self):
        print(f"{self.real}i + {self.imag}j")
    
    def __add__(self,other):
        newreal = self.real + other.real
        newimag = self.imag + other.imag
        return Complex(newreal , newimag)


num1 = Complex(1,4)
num1.showno()

num2 = Complex(5,9)
num2.showno()

num3 = num1+num2
num3.showno()






class Complex:
    def __init__(self,real,imag):
        self.real = real
        self.imag = imag
    
    def showno(self):
        print(f"{self.real}i + {self.imag}j")
    
    def __sub__(self,other):
        newreal = self.real - other.real
        newimag = self.imag - other.imag
        return Complex(newreal , newimag)


num1 = Complex(1,4)
num1.showno()

num2 = Complex(5,9)
num2.showno()

num3 = num1-num2
num3.showno()







class Dog:
    def speak(self):
        return "Woof!"


class Cat:
    def speak(self):
        return "Meow!"

# Using the same method name
animals = [Dog(), Cat()]

for animal in animals:
    print(animal.speak())









class Shape:
    def area(self):
        pass   # abstract method

class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side * self.side

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius * self.radius

shapes = [Square(4), Circle(3)]
for shape in shapes:
    print(shape.area())







class Car:
    def move(self):
        return "Driving"

class Bird:
    def move(self):
        return "Flying"

# Polymorphic function
def execute_movement(obj):
    return obj.move()

# Usage
car = Car()
bird = Bird()
print(execute_movement(car))   # Output: Driving
print(execute_movement(bird))  # Output: Flying