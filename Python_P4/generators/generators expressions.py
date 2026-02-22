gen_exp = (x * x for x in range(5))
print(gen_exp)
print(list(gen_exp))

total = sum(x * x for x in range(10))
print(total)

def fibonacci():
  a, b = 0, 1
  while True:
    yield a
    a, b = b, a + b

# Get first 100 Fibonacci numbers
gen = fibonacci()
for _ in range(100):
  print(next(gen))

# My example
cubes = (x ** 3 for x in range(6))

print(cubes)          
print(list(cubes))    

total_even = sum(x for x in range(20) if x % 2 == 0)
print(total_even)

total_even = sum(x for x in range(20) if x % 2 == 0)
print(total_even)

def fibonacci_limited(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

for num in fibonacci_limited(10):
    print(num)