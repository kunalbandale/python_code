"""
Single Level Inheritance :-
2 class i.e. parent and child | child class will take the properties
from parents.
---------------------------------------------
                PARENT (BASE / SUPER)
                    ^
                    |
                    |
                    |
                CHILD (child will take the properties)
                (DERIVED / SUBCLASS)
--------------------------------------------
"""
class Dad:
    def villa(self):
        print("villa (Mumbai)")

class Child(Dad):
    def bike(self):
        print("the bike (bmw)")
# single inheritance
c = Child()
c.bike()
c.villa()