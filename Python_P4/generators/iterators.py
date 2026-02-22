mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

mytuple = ("apple", "banana", "cherry")

for x in mytuple:
  print(x)

mystr = "banana"

for x in mystr:
  print(x)

class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

#My example
mylist = [10, 20, 30]
myit = iter(mylist)

print(next(myit))
print(next(myit))
print(next(myit))

mystring = "Hello"
myit = iter(mystring)   

print(next(myit))
print(next(myit))
print(next(myit)) 
print(next(myit))
print(next(myit))

class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 5:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

myclass = MyNumbers()

for x in myclass:
    print(x)

mydict = {"name": "Alex", "age": 20}
myit = iter(mydict)

print(next(myit))
print(next(myit))