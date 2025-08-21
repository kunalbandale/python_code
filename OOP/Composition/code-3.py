class Test:
    def __init__(self):
        print("constructor class")
    def display(self):
        print("Test class")
class Fun:
    def __init__(self):
        print("constrcutor class 2")

    def demo(self):
        print("demo in class fun def demo")

    t = Test()
    t.display()


f = Fun()
f.demo()