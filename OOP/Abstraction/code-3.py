from abc import *

class Test(ABC):
    @abstractmethod
    def subject(self):
        pass

    @abstractmethod
    def location(self):
        pass

    @abstractmethod
    def name(self):
        pass


# declaration as well as implementation
class Student(Test):
    def subject(self):
        print("SQL")

    def location(self):
        print("PUNE")

    def name(self):
        print("Patil")

s = Student()
s.subject()
s.location()
s.name()




