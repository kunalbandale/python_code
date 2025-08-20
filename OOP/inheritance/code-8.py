# multiple inheritance

"""
Template for multiple inheritance
---------------------------------
class Dad:
    pass
class Mom:
    pass
class Child(Dad , Mom):
    pass

c = Child()
"""

class Father:
    def money(self):
        print("Father Money")
class Mother:
    def care(self):
        print("Monther care")
class Child(Father , Mother):
    def joy(self):
        print("enjoy!!")
c = Child()
# c.money()
print(Child.__mro__)
