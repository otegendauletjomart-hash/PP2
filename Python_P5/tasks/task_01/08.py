import re 

text = input()

x = re.split(r"[A-Z]", text)

print(*x)