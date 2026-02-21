class Person:
    def __init__(self, name):
        self.name = name


class Athlete:
    def sport(self):
        print("Plays football")


class StudentAthlete(Person, Athlete):
    pass


x = StudentAthlete("Mike")
print(x.name)
x.sport()

#My example
class Person:
    def __init__(self, name):
        self.name = name

class Athlete:
    def sport(self):
        print(self.name, "plays basketball")

class StudentAthlete(Person, Athlete):
    pass

x = StudentAthlete("Anna")
print(x.name)  
x.sport()   

class Athlete:
    def sport(self):
        print(self.name, "runs track")

x = StudentAthlete("Mike")
x.sport()  

class Person:
    def greet(self):
        print("Hello,", self.name)

class StudentAthlete(Person, Athlete):
    pass

y = StudentAthlete("Lucy")
y.greet()  
y.sport()   

class Athlete:
    def sport(self):
        print(self.name, "swims")

z = StudentAthlete("Tom")
print(z.name)  
z.sport()      