class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello, my name is", self.name)

p1 = Person("Ellie")
p1.greet()

#My example
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi, I'm {self.name} and I'm {self.age} years old.")

s1 = Student("Alice", 20)
s1.introduce()

class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello, my name is", self.name)


class Student(Person):
    def study(self):
        print(self.name, "is studying")

s1 = Student("Ellie")
s1.greet()
s1.study()

class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello, my name is", self.name)


class Student(Person):
    def greet(self):
        print("Hi! I'm student", self.name)

s1 = Student("Ellie")
s1.greet()

class Person:
    species = "Human"   # переменная класса

    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello, my name is", self.name)

p1 = Person("Ellie")
p2 = Person("Mike")

print(p1.species)
print(p2.species)