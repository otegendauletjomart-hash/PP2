import re 

text = input()

pattern = r"a.*b"

if re.fullmatch(pattern, text):
    print("Yes")
else:
    print("No")