import re 

text = input()

pattern = r"[A-Z][a-z]+"

if re.fullmatch(pattern, text):
    print("Yes")
else:
    print("No")