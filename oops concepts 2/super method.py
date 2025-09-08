print("hello world")

class car:
    def __init__(self,type):
        self.type = type

    @staticmethod
    def start():
        print("car started...")
    
    @staticmethod
    def stop():
        print("car stopped....")

class toyota(car):
    colour = "black"

    def __init__(self,name,type):
        super().__init__(type)
        self.name = name
        super().start()

c1 = toyota("fortuner","electric")
print(c1.type)
print(c1.name)
