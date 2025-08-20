#step1
class Father:
    def Money(self):
        print("father money")
class Mother:
    def care(self):
        print("Mother-care")

class Child(Father,Mother):
    def joy(self):
        print("enjoy the day")

x=Child()
# x.Money()
# x.care()
# x.joy()
print(Child.__mro__)

"""
Through class_name
class Qspider:
    def sql(self):
        print("query_part from Qspider")

    def Manual(self):
        print("Testing from Qspider")
class Pyspider:
    def Python(self):
        print("Python from Pyspider")
    def sql(self):
        print("Sql from Pyspider")

class Student(Qspider,Pyspider):
    def Study(self):
        print("working")

    def sql(self):
        print("No---->query Part")
        Qspider.sql(x)  #Through class
        Pyspider.sql(x)

x=Student()
x.sql()
x.Manual()
x.Python()
x.Study()
'''

'''
Through super() function

class Qspider:
    def sql(self):
        print("query_part from Qspider")
        super().sql()
    def Manual(self):
        print("Testing from Qspider")

class Pyspider:
    def Python(self):
        print("Python from Pyspider")
    def sql(self):
        print("Sql from Pyspider")

class Student(Qspider,Pyspider):
    def Study(self):
        print("working")

    def sql(self):
        print("No---->query Part")
        super().sql()
x=Student()
x.sql()
x.Manual()
print(Student._mro_)
'''

'''
Diamond--> program in wrong format
class A:
    def spam(self):
        print("class--->A")

class B(A):
    def demo(self):
        print("Class--->B")
class C(A):
    def display(self):
        print("Class--->C")

class D(A,C):
    def Joy(self):
        print("Class-->D")

d=D()  #TypeError: Cannot create a consistent method resolution
# order (MRO) for bases A, C
d.spam()
d.demo()
d.display()
d.Joy()

print()

print(D._mro_)
'''

'''
#Diamond--> program in currect format
class A:
    def spam(self):
        print("class--->A")

class B(A):
    def demo(self):
        print("Class--->B")
class C(A):
    def display(self):
        print("Class--->C")

class D(B,C):
    def Joy(self):
        print("Class-->D")

d=D()
d.spam()
d.demo()
d.display()
d.Joy()
"""