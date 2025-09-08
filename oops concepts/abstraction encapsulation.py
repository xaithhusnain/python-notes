print("hello world")

'''
Abstraction:

Hiding the implementation details of a class and only showing the essential features to the user.

Encapsulation:

Wrapping data and functions into a single unit (object).


'''

class car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    def start(self):
        self.acc = True
        self.clutch = True
        print("Car started!")

    def brake(self):
        self.brk = True
        print("Car stopped!")

dvr = car()
dvr.start()
dvr.brake()


"""
the above programme show the concepts of Abstraction 
it hides the all steps that how a car started like we press the acc clutch etc
it just shows that a car started it dose not matter how it started 
so in short we just hide the implementation steps in a class 

"""




"""
creating an object is basically encapsulation
bcz we wrap all data, variables, and all functions into a single unit which is called object
and we can acess all these through a single object

"""