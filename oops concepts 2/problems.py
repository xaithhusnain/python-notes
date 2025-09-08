print("hello world")


class cirlce:
    def __init__(self,radius):
        self.radius = radius
    
    def area(self):
        A = (22/7 * (self.radius**2))  # A = πr2
        return A
    
    def perimeter(self):
        P = (2 * (22/7) * (self.radius)) # C = 2πr
        return P

c1 = cirlce(8)
print(c1.area())
print(c1.perimeter())




class employee:
    def __init__(self,dept,role,salary):
        self.dept = dept
        self.role = role
        self.salary = salary 

    def showdetails(self):
        print(f"dept = {self.dept}")
        print(f"role = {self.role}")
        print(f"salary = {self.salary}")

e1 = employee("finance","IT",60000)
e1.showdetails()




class engineer(employee):
    def __init__(self, dept, role, salary,name ,age ):
        self.name = name
        self.age = age 
        super().__init__(dept, role, salary)

    def info(self):
        print(f"name = {self.name}")
        print(f"age = {self.age}")
        self.showdetails()

eng1 = engineer("finance","IT",60000,"harry",28)
eng1.info()
eng1.showdetails()
print(eng1.role)




class engineer(employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age 
        super().__init__("finance","IT",60000,)

    def info(self):
        print(f"name = {self.name}")
        print(f"age = {self.age}")
        self.showdetails()

eng1 = engineer("harry",28)
eng1.info()
eng1.showdetails()
print(eng1.role)






# create a class called order which store item and its price 

# use dunder function __gt__() to convey that 
# oder 1 > order 2 if price of oder 1 > price of order 2


class order:
    def __init__(self,item,price):
        self.item = item
        self.price = price 
    
    def __gt__(self,order2):
        return self.price > order2.price
    
order1 = order("cake",100)
order2 = order("cold drinl",200)

print(order1>order2)