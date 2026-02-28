s = input()

letters = []
cletter = ""

for i in s:
    if i.isupper():
        if cletter:
            letters.append(cletter)
        cletter = i
    else:
        cletter += i

if cletter:
    letters.append(cletter)

print(letters)