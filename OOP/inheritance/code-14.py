# hierarchy inheritance
"""
                    parent

                child1    child2

whenever we are working on depend on the children we want to
create objects like here two objects if three children three objects
"""

class Rbi:
    def money(self):
        print("take money")

class Sbi(Rbi):
    def take_loan(self):
        print("SBI -> money taken as loan")

class Hdfc(Rbi):
    def take_bonds(self):
        print("Hdfc -> bonds taken from the rbi")


# object 1
s = Sbi()
s.take_loan()
s.money()

# object 2
h = Hdfc()
h.take_bonds()
h.money()

