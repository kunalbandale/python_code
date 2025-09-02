class Person:
    def show(self):
        print("I am a Person")

class Employee(Person):
    def show(self):
        print("I am an Employee")

class Student(Person):
    def show(self):
        print("I am a Student")

class Intern(Employee, Student):
    pass

intern = Intern()
intern.show()
