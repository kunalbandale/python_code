# multi level inheritance
"""
grandfather
    ^
    |
father
    ^
    |
child

child will take the properties from
the parents |
parent will take properties form the grandfather
"""

class Grandpa:
    @staticmethod
    def tvs():
        print("TVS Bike")
class Father(Grandpa):
    @staticmethod
    def land():
        print("50 acres land")
class Child(Father):
    @staticmethod
    def job():
        print("Job")

# object
ch = Child()
ch.tvs()
ch.land()
ch.job()

# father
f = Father()
f.land()
f.tvs()

# grandpa
g = Grandpa()
g.tvs()

