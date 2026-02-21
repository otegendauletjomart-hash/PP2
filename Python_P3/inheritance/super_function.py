class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname


class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname) 
        self.graduationyear = year


x = Student("Mike", "Olsen", 2019)
print(x.firstname, x.lastname, x.graduationyear)

#My example
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.year = year

    def greet(self):
        print("Hi", self.firstname, "from class of", self.year)

s = Student("Anna", "Smith", 2024)
s.greet() 

class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.year = year

s = Student("Mike", "Olsen", 2019)
print(s.firstname, s.year)  

students = [
    Student("Tom", "White", 2022),
    Student("Lucy", "Brown", 2025)
]

for s in students:
    print(s.firstname, s.lastname, s.year)

class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.year = year

    def status(self):
        print(self.firstname, "is", "Alumni" if self.year < 2023 else "Student")

s = Student("Lucy", "Brown", 2025)
s.status() 