# enumerate example
fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits):
    print(index, fruit)

# enumerate with start index
for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)

# zip example
names = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 95]

for name, score in zip(names, scores):
    print(name, score)

# convert zip to dict
result = dict(zip(names, scores))
print(result)