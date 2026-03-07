import re

text = input()

pattern = r"ab*"

if re.fullmatch(pattern, text):
    print("Yes")
else:
    print("No")