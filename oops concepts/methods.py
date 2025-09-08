print("hello world")

# Methods are functions that belong to objects.

class students:
    clg_name = "kips college"

    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    
    def wellcome(self):
        print("Well come",self.name)
    
    def get_marks(self):
        print(f"You get {self.marks} marks.")

    def result(self):
        if self.marks >= 80:
            print("Congratulations you are pass!")
        else:
            print("You are fail. Try again better next time.")


s1 = students("husnain",79)
print(s1.name)
s1.wellcome()
s1.get_marks()
s1.result()
