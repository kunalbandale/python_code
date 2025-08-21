# operator loading
# in python we can't directly achive

class Book:
    def __init__(self , pages):
        self.page = pages

    def __add__(self, other):
        return self.page + other.page
    def __sub__(self, other):
        return self.page - other.page

b = Book(100)
b1= Book(200)
b2 = Book(300)
# take help of __magic__ method
"""
Magic Method
# access specifiers 
a = 10  variable (public)
_a = 10 (protected)
__a = 10 (private)

magic method also known as dunder method
__magic__ 
__add__(s,other)
"""
print(b + b1)
print(b - b1)