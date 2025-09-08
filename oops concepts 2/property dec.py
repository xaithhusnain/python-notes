print("hello world")

class student:
    def __init__(self,phy,chem,math):
        self.phy = phy
        self.chem = chem
        self.math = math
        self.prcnt = ((self.phy + self.chem + self.math)/300)*100

    def percentage(self):
        return self.prcnt


s1 = student(89,34,78)
print(s1.percentage())

s1.phy = 56
print(s1.phy)
print(s1.percentage())


'''
in the above code we have change the value of the phy var 
it change the value but it dose not change the value of percentage 

'''




class student:
    def __init__(self,phy,chem,math):
        self.phy = phy
        self.chem = chem
        self.math = math

    def percentage(self):
        self.prcnt = ((self.phy + self.chem + self.math)/300)*100
        return self.prcnt


s1 = student(89,34,78)
print(s1.percentage())

s1.phy = 56
print(s1.phy)
print(s1.percentage())

s1.chem = 6
print(s1.chem)
print(s1.percentage())



'''
in the above code we have solve that issue by creating percentage in a method

but we can also make it more simple by @property decorater

property decorator will make it a property/attribute 

and we can acess it as a attribute

'''

class student:
    def __init__(self,phy,chem,math):
        self.phy = phy
        self.chem = chem
        self.math = math

    @property
    def percentage(self):
        self.prcnt = ((self.phy + self.chem + self.math)/300)*100
        return self.prcnt


s1 = student(89,34,78)
print(s1.percentage)

s1.phy = 56
print(s1.phy)
print(s1.percentage)

s1.chem = 6
print(s1.chem)
print(s1.percentage)



'''
in the above code now we can acess a method as a attr without any paranthesies

'''