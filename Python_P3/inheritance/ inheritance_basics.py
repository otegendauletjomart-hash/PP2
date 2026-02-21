class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

x = Person("John", "Doe")
x.printname()

class Student(Person):
    pass

x = Student("Mike", "Olsen")
x.printname()

#My example
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

class Student(Person):
    def welcome(self):
        print(f"Welcome, {self.firstname}!")

s = Student("Anna", "Smith")
s.printname()  
s.welcome()    

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

class Student(Person):
    def printname(self):
        print(f"Student Name: {self.firstname} {self.lastname}")

s = Student("Leo", "Brown")
s.printname()  

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

class Student(Person):
    def __init__(self, fname, lname, student_id):
        super().__init__(fname, lname)
        self.student_id = student_id

    def printinfo(self):
        print(f"{self.firstname} {self.lastname}, ID: {self.student_id}")

s = Student("Mia", "Lee", 12345)
s.printinfo()  

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

class Student(Person):
    pass

class Teacher(Person):
    def assign_homework(self):
        print(f"{self.firstname} assigns homework.")

s = Student("Tom", "Green")
t = Teacher("Mrs.", "White")

s.printname()  
t.printname()  
t.assign_homework() 