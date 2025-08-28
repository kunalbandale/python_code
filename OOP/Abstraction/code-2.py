from abc import ABC, abstractmethod

# concrete method / class
# declaration as well implementation -> concrete method
class Test(ABC):
    @abstractmethod
    def spam(self):
        pass

# for abstract class we cant use constructor

t = Test()
t.spam()