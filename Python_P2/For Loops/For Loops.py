fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

for x in "banana":
  print(x)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break   
  
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

for x in range(6):
  print(x)

for x in range(2, 6):
  print(x)

for x in range(2, 30, 3):
  print(x)

for x in range(6):
  print(x)
else:
  print("Finally finished!")

for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")    

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

for x in [0, 1, 2]:
  pass

#My example
colors = ["red", "green", "blue"]
for color in colors:
  print("Color:", color)

word = "Python"
for letter in word:
  print(letter)

numbers = [1, 2, 3, 4, 5]
for n in numbers:
  if n == 4:
    break
  print("Number:", n)

numbers = [1, 2, 3, 4, 5]
for n in numbers:
  if n % 2 == 0:
    continue
  print("Odd number:", n)

sizes = ["small", "medium", "large"]
shapes = ["circle", "square"]

for size in sizes:
  for shape in shapes:
    print(size, shape)
