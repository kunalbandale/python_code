class Test:
    def __init__(self):
        print("Test")
class T:
    def __init__(self):
        print("T")
class X(Test , T):
    def __init__(self):
        print("X")
x = X()
print(X.__mro__)