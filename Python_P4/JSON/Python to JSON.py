import json

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)

#My example
import json

person = {"name": "Alice", "age": 25, "city": "London"}
json_str = json.dumps(person)
print(json_str)



fruits = ["apple", "banana", "cherry"]
json_str = json.dumps(fruits)
print(json_str)



data = {
    "count": 10,
    "price": 3.5,
    "available": True,
    "sold_out": False,
    "owner": None
}

print(json.dumps(data))



person = {"name": "Tom", "age": 28, "city": "Berlin"}
print(json.dumps(person, indent=4))