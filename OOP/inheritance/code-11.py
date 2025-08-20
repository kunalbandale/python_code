# dimond program
# MRO format it will work

# one super class that super class will take help of two sub class
"""
          A   super class
         B C  subclass
          D   child class
"""

class A:
    def spam(self):
        print("class ---> A")
class B(A):
    def demo(self):
        print("class---->B")
class C(A):
    def display(self):
        print("dispaly class -- >c ")

class D(B,C):
    def joy(self):
        print("Joy")

d = D()
print(D.__mro__)