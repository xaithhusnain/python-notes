print("hello world")


# All classes have a function called __init__(), which is always executed when the object is being
#  initiated.

class students:
    name = "ali"
    def __init__(self):
        # print(self)
        print("Adding new students to the database...")


s1 = students()
print(s1)




# we can also give multiple parameters in the constructor


class students:
    def __init__(self,fullname,cls,marks,gender):
        print("Adding new students to the database...")
        self.name = fullname     # attributes
        self.cls = cls
        self.marks = marks
        self.gender = gender


s1 = students("Ali Husnain",1)
print(s1.name)
print(s1.marks)

s2 = students("Umer",2)
print(s2.name)
print(s2.marks)

s3 = students("Ahsan",3)
print(s3.name)
print(s3.marks)


name = input("enter you name: ")
marks = int(input("enter you marks: "))
cls = input("enter you cls: ")
Gender = input("enter you gener: ")

stdt = students(name,cls,marks,Gender)
print(stdt.name, stdt.cls, stdt.marks, stdt.gender)
print(stdt.cls)
print(stdt.marks)
print(stdt.gender)




class students:
    # default constructors
    def __init__(self):
        pass
    

    # parameterized constructors
    def __init__(self,fullname,cls,marks,gender):
        print("Adding new students to the database...")
        self.name = fullname     # attributes
        self.cls = cls
        self.marks = marks
        self.gender = gender
