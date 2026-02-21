def my_function(x, y):
  return x + y

result = my_function(5, 3)
print(result)

def my_function():
  return ["apple", "banana", "cherry"]

fruits = my_function()
print(fruits[0])
print(fruits[1])
print(fruits[2])

def my_function():
  return (10, 20)

x, y = my_function()
print("x:", x)
print("y:", y)

def my_function(name, /):
  print("Hello", name)

my_function("Emil")

def my_function(name):
  print("Hello", name)

my_function(name = "Emil")

def my_function(*, name):
  print("Hello", name)

my_function(name = "Emil")

def my_function(a, b, /, *, c, d):
  return a + b + c + d

result = my_function(5, 10, c = 15, d = 20)
print(result)

#My example
def calculate(a, b):
    return a + b, a * b

sum_result, multiply_result = calculate(4, 6)

print("Sum:", sum_result)
print("Product:", multiply_result)

def get_user_info():
    name = "Daulet"
    age = 20
    return name, age
user_name, user_age = get_user_info()
print("Name:", user_name)
print("Age:", user_age)

def create_user(*, username, age):
    print("Username:", username)
    print("Age:", age)

create_user(username="emil123", age=25)

def order(item, quantity, /, *, price, discount):
    total = quantity * price - discount
    return total

result = order("Laptop", 2, price=500, discount=100)
print("Total:", result)