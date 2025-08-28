"""
Abstraction : Hiding the implementation of the code
------------------------------------------------------
e.g. when we apply break in the car we don't know
the mechanism the  breaking of the car/bike
------------------------------------------------------
Step 1:
from abc import ABC, abstractmethod

abc -> module
ABC -> Class Name

--------------------
1) Abstract Class  | don't know implementation still we are declaring the class
2) Abstract Method |
--------------------
Note: if you want to achieve abstraction we need to take the
help of inheritance

"""
from abc import *

# case 1
# class Test:
#     pass
# t = Test()

# class Test(ABC):
#     def spam(self):
#         print("Test Class")
# t = Test()
# t.spam()

# case 3
# class Test:
#     @abstractmethod
#     def spam(self):
#         print("Test Class")


# class Test(ABC):
#     @abstractmethod
#     def spam(self):
#         print("Test class")
# t = Test()
# t.spam() # TypeError: Can't instantiate abstract class Test with abstract method spam
# for abstract class we cant create object












