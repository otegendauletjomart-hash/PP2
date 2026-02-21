numbers = [1, 2, 3, 4, 5, 6, 7, 8]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)

#My example
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
greater_than_five = list(filter(lambda x: x > 5, numbers))
print(greater_than_five)  

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
multiples_of_three = list(filter(lambda x: x % 3 == 0, numbers))
print(multiples_of_three)  

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
less_than_four = list(filter(lambda x: x < 4, numbers))
print(less_than_four)  # [1, 2, 3]