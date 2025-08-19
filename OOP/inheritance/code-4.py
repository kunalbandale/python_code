class Grandpa:
    def __init__(self):
        print("Grandpa")
class Father(Grandpa):
    def __init__(self):
        super().__init__()
        print("Father")
class Child(Father):
    def __init__(self):
        super().__init__()
        print("Child")
c = Child()

