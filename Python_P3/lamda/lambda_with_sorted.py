students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)

words = ["apple", "pie", "banana", "cherry"]
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)

#My example
students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)  

words = ["apple", "pie", "banana", "cherry"]
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)  

students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]
sorted_by_name = sorted(students, key=lambda x: x[0])
print(sorted_by_name)  

words = ["apple", "pie", "banana", "cherry"]
sorted_by_last_letter = sorted(words, key=lambda x: x[-1])
print(sorted_by_last_letter)  

