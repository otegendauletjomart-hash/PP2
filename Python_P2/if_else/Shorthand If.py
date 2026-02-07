a = 5
b = 2
if a > b: print("a is greater than b")

a = 2
b = 330
print("A") if a > b else print("B")

a = 10
b = 20
bigger = a if a > b else b
print("Bigger is", bigger)


a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

x = 15
y = 20
max_value = x if x > y else y
print("Maximum value:", max_value)

username = ""
display_name = username if username else "Guest"
print("Welcome,", display_name)

#My example
n = 8
print("Even") if n % 2 == 0 else print("Odd")

a = 7
b = 3
small = a if a < b else b
print("Smaller is", small)

isadmin = False
print("Access granted") if isadmin else print("Access denied")

email = ""
user_email = email if email else "No email provided"
print(user_email)

number = -5
result = "Positive" if number > 0 else "Not positive"
print(result)


