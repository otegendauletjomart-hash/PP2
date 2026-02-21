class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def welcome(self):
        print("Welcome", self.firstname, self.lastname)


class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def welcome(self):
        print("Welcome", self.firstname, self.lastname,
              "to the class of", self.graduationyear)


x = Student("Mike", "Olsen", 2019)
x.welcome()

#My example
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def welcome(self):
        print("Hello", self.firstname, self.lastname)

class Student(Person):
    pass

s = Student("Anna", "Smith")
s.welcome() 

class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.year = year

    def welcome(self):
        print(self.firstname, "from class of", self.year)

s = Student("Mike", "Olsen", 2019)
s.welcome()

class Teacher(Person):
    def welcome(self):
        print("Hi Teacher", self.firstname)

t = Teacher("John", "Doe")
t.welcome() 

class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.year = year

    def welcome(self):
        status = "Alumni" if self.year < 2023 else "Student"
        print(self.firstname, "-", status)

s = Student("Lucy", "Brown", 2025)
s.welcome() 

