def echo_generator():
  while True:
    received = yield
    print("Received:", received)

gen = echo_generator()
next(gen) # Prime the generator
gen.send("Hello")
gen.send("World")

def my_gen():
  try:
    yield 1
    yield 2
    yield 3
  finally:
    print("Generator closed")

gen = my_gen()
print(next(gen))
gen.close()

#My example
def accumulator():
    total = 0
    while True:
        value = yield total
        total += value

gen = accumulator()
print(next(gen))      
print(gen.send(10))   
print(gen.send(5))    
print(gen.send(20))   

def limited_echo():
    count = 0
    while count < 3:
        received = yield
        print("Received:", received)
        count += 1
    print("Done")

gen = limited_echo()
next(gen)

gen.send("A")
gen.send("B")
gen.send("C")

def test():
    try:
        yield 1
        yield 2
    finally:
        print("Генератор закрыт")

gen = test()

print(next(gen)) 
gen.close()      

def count_three():
    yield 1
    yield 2
    yield 3

gen = count_three()

print(next(gen))  
print(next(gen))  
print(next(gen))  