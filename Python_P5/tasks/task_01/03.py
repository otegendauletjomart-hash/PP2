import re 

text = input()

pattern = r"[a-z]+(_[a-z]+)+"

if re.fullmatch(pattern, text):
    print("Yes")
else:
    print("No")