import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])

import json

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

#My example
import json

json_data = '{"fruit": "apple", "quantity": 5, "price": 3.5}'
data = json.loads(json_data)

print("Fruit:", data["fruit"])
print("Quantity:", data["quantity"])
print("Price:", data["price"])



person = {"name": "Lara", "age": 19, "city": "Paris"}
json_string = json.dumps(person)

print(json_string)



fruits = ["apple", "banana", "cherry"]
json_fruits = json.dumps(fruits)

print(json_fruits)



person = {"name": "Tom", "age": 25, "city": "London"}
print(json.dumps(person, indent=4))