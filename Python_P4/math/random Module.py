import random

print(random.random())

print(random.randint(1, 10))

fruits = ["apple", "banana", "cherry"]
print(random.choice(fruits))

numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)

print(numbers)

#My example
print(random.randint(100, 1000))

fruits = ["apple", "banana", "cherry", "date", "fig", "grape"]
print(random.sample(fruits, 3))

numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(numbers)

print(random.random())
