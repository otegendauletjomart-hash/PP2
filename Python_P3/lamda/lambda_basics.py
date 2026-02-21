x = lambda a : a + 10
print(x(5))

x = lambda a, b : a * b
print(x(5, 6))

def myfunc(n):
  return lambda a : a * n

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))

def myfunc(n):
  return lambda a : a * n

mytripler = myfunc(3)

print(mytripler(11))

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))

#My example
def power(n):
    return lambda x: x ** n
square = power(2)
cube = power(3)
print(square(5))  
print(cube(5))    

add_five = lambda x: x + 5
print(add_five(10)) 

multiply = lambda a, b: a * b
print(multiply(4, 7))  

def power(n):
    return lambda x: x ** n

square = power(2)
cube = power(3)

print(square(5))  
print(cube(2))    

def myfunc(string):
    return lambda x: string * x 

