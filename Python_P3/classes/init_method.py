class Person:
    def __init__(self, name):
        self.name = name

p1 = Person("Daulet")
print(p1.name)

#My example
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello, my name is", self.name)

p1 = Person("Daulet")
p1.greet()

class Person:
    species = "Human" 

    def __init__(self, name):
        self.name = name

p1 = Person("Daulet")
p2 = Person("Aruzhan")

print(p1.species)
print(p2.species)

class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def study(self):
        print(self.name, "is studying")

s1 = Student("Daulet")
print(s1.name)
s1.study()

class Person:
    def __init__(self, name):
        self.name = name

p1 = Person("Daulet")
p2 = Person("Aruzhan")

p1.name = "Dias"  

print(p1.name)
print(p2.name)