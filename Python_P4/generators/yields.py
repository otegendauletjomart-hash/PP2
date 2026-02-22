def my_generator():
  yield 1
  yield 2
  yield 3

for value in my_generator():
  print(value)

def count_up_to(n):
  count = 1
  while count <= n:
    yield count
    count += 1

for num in count_up_to(5):
  print(num)

def large_sequence(n):
  for i in range(n):
    yield i

# This doesn't create a million numbers in memory
gen = large_sequence(1000000)
print(next(gen))
print(next(gen))
print(next(gen))

def simple_gen():
  yield "Emil"
  yield "Tobias"
  yield "Linus"

gen = simple_gen()
print(next(gen))
print(next(gen))
print(next(gen))

#My example
def squares(n):
    for i in range(1, n + 1):
        yield i * i

for num in squares(5):
    print(num)

def even_numbers(n):
    for i in range(n):
        if i % 2 == 0:
            yield i

for num in even_numbers(10):
    print(num)

def letters(word):
    for letter in word:
        yield letter

for i in letters("HEllo"):
    print(i)

def big_numbers():
    for i in range(1000000000):
        yield i

gen = big_numbers()

print(next(gen))
print(next(gen))
print(next(gen))