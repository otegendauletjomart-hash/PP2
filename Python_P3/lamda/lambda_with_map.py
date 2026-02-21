numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)

#My example
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(squared) 

numbers = [1, 2, 3, 4, 5]
as_strings = list(map(lambda x: f"Number {x}", numbers))
print(as_strings)  

numbers = [1, 2, 3, 4, 5]
indexed = list(map(lambda x: x * numbers.index(x), numbers))
print(indexed)  

numbers = [1, -2, 3, -4, 5]
opposite = list(map(lambda x: -x, numbers))
print(opposite)


