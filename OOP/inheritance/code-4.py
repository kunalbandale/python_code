class Grandpa:
    def __init__(self , age):
        print("Grandpa" , age)
class Father(Grandpa):
    def __init__(self , age):
        # super().__init__(age)
        print("Father" , age)
class Child(Father):
    def __init__(self,age):
        super().__init__(35)
        print("Child" , age)
c = Child(12)

