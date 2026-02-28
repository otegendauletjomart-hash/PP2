#helloWorldPython

s = input()

x = s[0].lower()

for i in s[1:]:
    if i.isupper():
        x += "_" + i.lower()
    else:
        x += i.lower()

print(x)
