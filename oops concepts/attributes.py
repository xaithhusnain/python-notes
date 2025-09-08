print("hello world")


class students:
    clg_name = "kips college"     # class attribute
    def __init__(self,fullname,marks):
        print("Adding new students to the database...")
        self.name = fullname     # object attributes
        self.marks = marks

s1 = students("ali",90)
print(s1.name)
print(s1.marks)
print(s1.clg_name)

print(students.clg_name)


s2 = students("husnain",97)
print(s2.name)
print(s2.marks)
print(s1.clg_name)

print(students.clg_name)





class students:
    clg_name = "kips college"
    name = "anonymous"  #class attr
    def __init__(self,name,):
        self.name = name  #object attr

s2 = students("husnain")
print(s2.name)    #but this will print the obj attr bcz obj attr > class attr


