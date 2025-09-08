class students:
    clg_name = "kips college"
    def __init__(self,name,marks_of_maths,marks_of_eng,marks_of_chem):
        self.name = name
        self.marksofmaths = marks_of_maths
        self.marksofeng = marks_of_eng
        self.marksofchem = marks_of_chem
            
    def avg(self):
        self.sum = self.marksofmaths + self.marksofeng + self.marksofchem
        print(f"Average marks: {(self.sum/3)}")
        print(f"Average marks: {round(self.sum/3,2)}")
        print(f"Average marks: {round(self.sum/3)}")




s1 = students("husnain",34,5,92)
s1.avg()




# use of round function

print(round(3.14159))       # Rounds to the nearest integer: 3
print(round(3.14159, 2))    # Rounds to 2 decimal places: 3.14
print(round(2.5))           # Rounds to the nearest even integer: 2
print(round(3.5))           # Rounds to the nearest even integer: 4




class students:

    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
       
    
    def avg(self):
        self.sum = sum(self.marks)
        print(f"Average marks: {(self.sum/3)}")
    
listofmarks = []

for i in range(3):
    a = int(input("enter your marks: "))
    listofmarks.append(a)

name = input("entr your name: ")

s1 = students(name,listofmarks)
print(s1.name)
s1.avg()








# class students:

#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks
       
    
#     def avg(self):
#         self.sum = sum(self.marks)
#         print(f"Hi {self.name}. Your average marks: {(self.sum/3)}")


# s1 = students("ali",[34,5,77])
# s1.avg()

# s1.name = "husnain"
# s1.avg()









class account:

    def __init__(self,balance,accountno):
        self.balance = balance
        self.accountno = accountno

    def debit(self,amount):
        self.amount = amount
        self.balance = self.balance - self.amount
        print(f"Rs: {amount} was debited from your account {self.accountno}.")
        print(f"your total balance is now {self.balance}.")
    
    def credit(self,amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print(f"Rs: {amount} credited in your account {self.accountno}")
        print(f"your total balance is now {self.balance}.")
    def totalbalance(self):

        print(f"Your account no is {self.accountno}. Your total balance is {self.balance}.")


user1 = account(1000,12345)
print(user1.balance)
print(user1.accountno)
user1.debit(700)
user1.credit(200)
user1.totalbalance()