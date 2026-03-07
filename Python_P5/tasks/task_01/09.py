import re 

text = input()

pattern = re.sub(r"[A-Z]", lambda a: " " + a.group(), text)

print(pattern)