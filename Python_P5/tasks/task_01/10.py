import re 

text = input()

pattern = re.sub(r"[A-Z]", lambda a: "_" + a.group().lower(), text)

print(pattern)