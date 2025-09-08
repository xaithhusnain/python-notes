print("hello world")

class account:
    def __init__(self,accno,password):
        self.accno = accno
        self.__password = password   #private a attribute just by adding 2 underscore(__)

    def resetpassword(self):
        print(self.__password)   # can access in the class


user1 = account(12345,"abcde")
print(user1.accno)
print(user1.__password)     #can't acess by the outside of the class
user1.resetpassword()





class person:
    __name = "anonymous"   # private attr

    def __hello(self):     # private method
        print("hello",self.__name)
    
    def wellcome(self):
        self.__hello()      # we can call a method into another 


p1 = person()
# print(p1.__name)        # can't acess bcz its private
# p1.__hello()
p1.wellcome()