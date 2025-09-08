print("hello world")

class student:
    def __init__(self,name,school):
        self.name = name
        self.school = school
        # print(f"He is {name} and reads in {school}")
    
s1 = student('ali',"abc")
print(s1.name)
del s1
print(s1.name)
