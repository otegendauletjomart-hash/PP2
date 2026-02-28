import math

n = int(input("n: "))
a = int(input("a: "))

area = n * (a ** 2) / (4 * math.tan(math.pi / n))
print(int(area))