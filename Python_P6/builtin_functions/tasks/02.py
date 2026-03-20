from functools import reduce

num = [1, 2, 3, 4]

a = reduce(lambda x, y: x * y, num)

print(a)