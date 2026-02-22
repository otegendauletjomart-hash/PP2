import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))

print(json.dumps(x, indent=4, separators=(". ", " = ")))
print(json.dumps(x, indent=4, sort_keys=True))

#My example
import json

data = {
    "name": "Alice",
    "student": True,
    "employed": False,
    "pet": None
}

json_str = json.dumps(data)
print(json_str)



data = {
    "fruits": ("apple", "banana"),
    "vegetables": ["carrot", "tomato"]
}

json_str = json.dumps(data)
print(json_str)



person = {"name": "Bob", "age": 28, "city": "Berlin"}
print(json.dumps(person, indent=4))



person = {"city": "Paris", "age": 22, "name": "Lara"}
print(json.dumps(person, sort_keys=True, indent=4))