s = input()

for i in s:
    if i.isupper() and i != s[0]:
        print(" "+i, end="")
        continue
    else:
        print(i, end="")