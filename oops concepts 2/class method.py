print("hello world")

class person:
    name = "anonymous"

    def chnagename(self,name):
        self.name = name

p1 = person()
p1.chnagename("ali")
print(p1.name)     # ali
print(person.name)   # anonymous


# how to change class attr in the whole class


class person:
    name = "anonymous"

    def chnagename(self,name):
        person.name = name

p1 = person()
p1.chnagename("ali")
print(p1.name)
print(person.name)
# both will prints ali






class person:
    name = "anonymous"

    def chnagename(self,name):
        self.name = name
        self.__class__.name = "harry"

p1 = person()
p1.chnagename("ali")
print(p1.name)
print(person.name)







class person:
    name = "anonymous"

    @classmethod
    def chnagename(cls,name):
        cls.name = name


p1 = person()
p1.chnagename("ali")
print(p1.name)
print(person.name)





"""
static methods: ()

class methods: (cls)

instance methods: (self)

"""