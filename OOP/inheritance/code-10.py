class Qspider:
    def sql(self):
        print("SQL Part")
    def Manual(self):
        print("Manual Testing")
class PySpider:
    def python(self):
        print("Learning Python")
    def sql(self):
        print("SQL learning daily")

class Student(Qspider , PySpider):
    def study(self):
        print("Studying")
    def sql(self):
        print("projects on sql")
        super().sql()


s = Student()
s.sql()
s.study()
s.Manual()
s.python()

print(Student.__mro__)