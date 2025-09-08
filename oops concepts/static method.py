print("hello world")

#  Methods that don’t use the self parameter (work at class level)


class students:

    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
       
    @staticmethod    #decorator
    def hello():
        print("Hello sir!")
    
    def avg(self):
        self.sum = sum(self.marks)
        print(f"Hi {self.name}. Your average marks: {(self.sum/3)}")


s1 = students("ali",[34,5,77])
s1.hello()

